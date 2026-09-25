(() => {
  const KEY = "sgpc-progress-v1";
  const load = () => {
    try { return JSON.parse(localStorage.getItem(KEY)) || {version:1, completed:[]}; }
    catch (_) { return {version:1, completed:[]}; }
  };
  const save = data => localStorage.setItem(KEY, JSON.stringify(data));
  const ids = data => new Set((data.completed || []).map(x => typeof x === "string" ? x : x.lesson));

  function mark(id) {
    const data=load(), done=ids(data);
    if (!done.has(id)) data.completed.push({lesson:id, completed:new Date().toISOString().slice(0,10)});
    save(data); render();
  }
  function unmark(id) {
    const data=load();
    data.completed=(data.completed||[]).filter(x => (typeof x === "string" ? x : x.lesson)!==id);
    save(data); render();
  }
  function render() {
    const done=ids(load());
    document.querySelectorAll("[data-lesson-id]").forEach(el => {
      const id=el.dataset.lessonId, complete=done.has(id);
      el.classList.toggle("is-complete", complete);
      const b=el.querySelector("[data-progress-toggle]");
      if (b) { b.textContent=complete ? "✓ Read" : "Mark as read"; b.setAttribute("aria-pressed", String(complete)); }
    });
    document.querySelectorAll("[data-progress-count]").forEach(el => {
      const course=el.dataset.progressCount;
      const lessonEls=[...document.querySelectorAll("[data-lesson-id]")].filter(x=>!course || x.dataset.lessonId.startsWith(course+"/"));
      const count=lessonEls.filter(x=>done.has(x.dataset.lessonId)).length;
      el.textContent=count+" / "+lessonEls.length+" read";
    });
  }
  document.addEventListener("click", e => {
    const b=e.target.closest("[data-progress-toggle]");
    if (!b) return;
    const host=b.closest("[data-lesson-id]");
    if (!host) return;
    ids(load()).has(host.dataset.lessonId) ? unmark(host.dataset.lessonId) : mark(host.dataset.lessonId);
  });
  window.SGPCProgress={
    export() {
      const blob=new Blob([JSON.stringify(load(),null,2)],{type:"application/json"});
      const a=document.createElement("a"); a.href=URL.createObjectURL(blob); a.download="learning-progress.json"; a.click(); URL.revokeObjectURL(a.href);
    },
    import(data) {
      const current=load(), merged=new Map((current.completed||[]).map(x=>[(typeof x==="string"?x:x.lesson),x]));
      (data.completed||[]).forEach(x=>{const id=typeof x==="string"?x:x.lesson;if(id&&!merged.has(id))merged.set(id,x);});
      save({version:1,completed:[...merged.values()]}); render();
    }
  };
  document.readyState==="loading" ? document.addEventListener("DOMContentLoaded",render) : render();
})();
