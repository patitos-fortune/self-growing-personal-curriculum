/*
 * Reading progress for the static curriculum site. No server, no accounts.
 *
 * Two sources of "read" state are combined:
 *   1. Browser storage (localStorage): what the reader marked with "Mark as read"
 *      in this browser. Per browser and per device; cleared if site data is cleared.
 *   2. curriculum/PROGRESS.json: the durable record committed to the repository.
 *      Read-only here; an AI assistant (or you) updates it through Git.
 *
 * Markup hooks:
 *   [data-lesson-id="slug/NN"]           a lesson (on <body>) or a lesson card
 *   [data-progress-toggle]               the Mark as read button (inside a lesson)
 *   [data-progress-count="slug"]         shows "X of N read"; N = data-total or cards on the page
 *   [data-progress-list]                 progress page: list of completed lessons
 *   [data-progress-export|import|reset]  progress page controls
 *   [data-progress-status]               progress page status line
 *
 * Record format (same as curriculum/PROGRESS.json):
 *   { "version": 1, "completed": [ { "lesson": "slug/NN", "completed": "YYYY-MM-DD" } ] }
 */
(() => {
  "use strict";
  const script = document.currentScript;
  const siteRoot = new URL("../../", script ? script.src : location.href);
  // Scope the key to this site's path so two curricula on the same
  // username.github.io origin do not share (and overwrite) progress.
  const LEGACY_KEY = "sgpc-progress-v1";
  const KEY = LEGACY_KEY + ":" + siteRoot.pathname;
  const ID_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*\/\d{2,}$/;
  const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;

  let storageOk = true;
  let repo = new Map(); // lesson id -> record, from PROGRESS.json
  let repoLoaded = false;

  const today = () => new Date().toISOString().slice(0, 10);
  const idOf = x => (typeof x === "string" ? x : x && x.lesson);

  function readStore() {
    try {
      let raw = localStorage.getItem(KEY);
      if (raw === null) {
        const legacy = localStorage.getItem(LEGACY_KEY); // pre-scoping versions
        if (legacy !== null) { localStorage.setItem(KEY, legacy); raw = legacy; }
      }
      const data = JSON.parse(raw);
      return data && Array.isArray(data.completed) ? data : { version: 1, completed: [] };
    } catch (_) {
      return { version: 1, completed: [] };
    }
  }
  function writeStore(data) {
    try { localStorage.setItem(KEY, JSON.stringify(data)); storageOk = true; }
    catch (_) { storageOk = false; }
  }
  function local() {
    const m = new Map();
    readStore().completed.forEach(x => { const id = idOf(x); if (id) m.set(id, typeof x === "string" ? { lesson: id } : x); });
    return m;
  }
  function all() {
    const m = new Map(repo);
    local().forEach((rec, id) => { if (!m.has(id)) m.set(id, rec); });
    return m;
  }
  const save = map => writeStore({ version: 1, completed: [...map.values()] });

  function toggle(id) {
    if (repo.has(id)) return; // recorded in Git; change it there
    const m = local();
    m.has(id) ? m.delete(id) : m.set(id, { lesson: id, completed: today() });
    save(m);
    render();
  }

  function mergeImport(data) {
    if (!data || data.version !== 1 || !Array.isArray(data.completed)) {
      throw new Error("Not a progress file (expected version 1 with a completed list).");
    }
    const m = local();
    let added = 0, skipped = 0;
    data.completed.forEach(x => {
      const id = idOf(x);
      if (!id || !ID_RE.test(id)) { skipped++; return; }
      const date = x && DATE_RE.test(x.completed || "") ? x.completed : undefined;
      const cur = m.get(id);
      if (!cur) { m.set(id, date ? { lesson: id, completed: date } : { lesson: id }); added++; }
      else if (date && (!cur.completed || date < cur.completed)) cur.completed = date; // keep earliest
    });
    save(m);
    render();
    return { added, skipped };
  }

  function exportFile() {
    const records = [...all().values()].sort((a, b) => a.lesson.localeCompare(b.lesson));
    const body = JSON.stringify({ version: 1, exported: new Date().toISOString(), completed: records }, null, 2);
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([body], { type: "application/json" }));
    a.download = "learning-progress.json";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  }

  function status(msg) {
    document.querySelectorAll("[data-progress-status]").forEach(el => { el.textContent = msg; });
  }

  function render() {
    const done = all();
    document.querySelectorAll("[data-lesson-id]").forEach(el => {
      const id = el.dataset.lessonId, complete = done.has(id);
      el.classList.toggle("is-complete", complete);
      const b = el.querySelector("[data-progress-toggle]");
      if (!b) return;
      b.setAttribute("aria-pressed", String(complete));
      if (repo.has(id)) {
        b.textContent = "✓ Read (recorded in PROGRESS.json)";
        b.setAttribute("aria-disabled", "true");
      } else {
        b.textContent = complete ? "✓ Read — tap to undo" : "Mark as read";
        b.removeAttribute("aria-disabled");
      }
    });
    document.querySelectorAll("[data-progress-count]").forEach(el => {
      const slug = el.dataset.progressCount;
      const prefix = slug ? slug + "/" : "";
      const cards = [...document.querySelectorAll(".lesson-card[data-lesson-id]")].filter(x => x.dataset.lessonId.startsWith(prefix));
      const total = el.dataset.total ? parseInt(el.dataset.total, 10) : cards.length;
      const count = el.dataset.total
        ? [...done.keys()].filter(id => id.startsWith(prefix)).length
        : cards.filter(x => done.has(x.dataset.lessonId)).length;
      el.textContent = total ? Math.min(count, total) + " of " + total + " read" : "";
      const card = el.closest(".course-card");
      if (card) card.classList.toggle("is-complete", total > 0 && count >= total);
    });
    document.querySelectorAll("[data-progress-list]").forEach(el => {
      el.textContent = "";
      const rows = [...done.values()].sort((a, b) => a.lesson.localeCompare(b.lesson));
      if (!rows.length) {
        const li = document.createElement("li");
        li.textContent = "Nothing marked as read yet.";
        el.appendChild(li);
      }
      rows.forEach(rec => {
        const [slug, nn] = rec.lesson.split("/");
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = new URL("courses/" + slug + "/lessons/" + nn + ".html", siteRoot).href;
        a.textContent = rec.lesson;
        li.appendChild(a);
        li.appendChild(document.createTextNode(
          (rec.completed ? " — " + rec.completed : "") + (repo.has(rec.lesson) ? " (repository)" : " (this browser)")));
        el.appendChild(li);
      });
    });
    if (!storageOk) status("This browser is blocking site storage, so marks will not be kept after you leave the page.");
  }

  document.addEventListener("click", e => {
    const t = e.target.closest("[data-progress-toggle],[data-progress-export],[data-progress-reset]");
    if (!t) return;
    if (t.hasAttribute("data-progress-toggle")) {
      const host = t.closest("[data-lesson-id]");
      if (host) toggle(host.dataset.lessonId);
    } else if (t.hasAttribute("data-progress-export")) {
      exportFile();
      status("Downloaded learning-progress.json.");
    } else if (t.hasAttribute("data-progress-reset")) {
      if (t.dataset.armed !== "1") { // two-step confirm without a blocking dialog
        t.dataset.armed = "1";
        t.textContent = "Tap again to clear this browser's progress";
        return;
      }
      delete t.dataset.armed;
      t.textContent = "Clear this browser's progress";
      writeStore({ version: 1, completed: [] });
      render();
      status("Cleared progress stored in this browser. Records in PROGRESS.json are unchanged.");
    }
  });

  document.addEventListener("change", e => {
    const input = e.target.closest("[data-progress-import]");
    if (!input || !input.files || !input.files[0]) return;
    input.files[0].text().then(text => {
      const r = mergeImport(JSON.parse(text));
      status("Imported " + r.added + " new record(s)" + (r.skipped ? ", skipped " + r.skipped + " invalid." : "."));
    }).catch(err => status("Import failed: " + err.message))
      .finally(() => { input.value = ""; });
  });

  function loadRepo() {
    // Works on GitHub Pages and any http(s) server; fails harmlessly on file://.
    return fetch(new URL("curriculum/PROGRESS.json", siteRoot), { cache: "no-cache" })
      .then(r => (r.ok ? r.json() : null))
      .then(data => {
        if (data && Array.isArray(data.completed)) {
          data.completed.forEach(x => { const id = idOf(x); if (id) repo.set(id, typeof x === "string" ? { lesson: id } : x); });
        }
      })
      .catch(() => {})
      .finally(() => { repoLoaded = true; render(); });
  }

  window.SGPCProgress = {
    completed: () => [...all().values()],
    isRepoLoaded: () => repoLoaded,
    export: exportFile,
    import: mergeImport,
    storageKey: KEY
  };

  const start = () => { render(); loadRepo(); };
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", start) : start();
})();
