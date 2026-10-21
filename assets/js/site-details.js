// Small progressive enhancements; every page remains readable without JavaScript.
const motionPreference = matchMedia("(prefers-reduced-motion: reduce)");
if ("IntersectionObserver" in window && !motionPreference.matches) {
  const targets = document.querySelectorAll(
    [
      ".home-intro-copy > *",
      ".section-heading",
      ".reve-overview",
      ".reve-contributions > .eyebrow",
      ".contribution",
      ".research-note",
      ".project-tile",
      ".post-header > *",
      ".publication-search",
      ".publications ol.bibliography > li",
      ".blog-page .header-bar > *",
      ".blog-page .post-list > li",
      "article.post-content > *",
      ".cv-intro > *",
      ".cv .card-title",
      ".cv .list-group > li",
      ".cv .skill-item",
      ".cv .language-item",
      ".cv .interest-item",
      ".cv #extra-curricular-activities + .card .card-text",
    ].join(",")
  );
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.replace("will-reveal", "is-revealed");
        observer.unobserve(entry.target);
      }
    },
    { threshold: 0.01 }
  );
  let entranceIndex = 0;
  targets.forEach((element) => {
    // Avoid nested entrances, which multiply opacity and movement.
    if (element.parentElement.closest(".will-reveal")) return;
    if (element.getBoundingClientRect().top < innerHeight) {
      element.style.setProperty("--reveal-delay", `${Math.min(entranceIndex++, 3) * 25}ms`);
    }
    element.classList.add("will-reveal");
    observer.observe(element);
  });
  document.addEventListener("focusin", (event) => {
    const block = event.target.closest(".will-reveal");
    if (!block) return;
    block.style.setProperty("--reveal-delay", "0ms");
    block.classList.replace("will-reveal", "is-revealed");
    observer.unobserve(block);
  });
  motionPreference.addEventListener("change", () => {
    if (!motionPreference.matches) return;
    observer.disconnect();
    document.querySelectorAll(".will-reveal").forEach((element) => element.classList.remove("will-reveal"));
  });
}

// The theme's existing disclosure logic handles clicks; add keyboard access
// and keep assistive state synchronized as the panels open and close.
document.querySelectorAll(".publications .links a.abstract, .publications .links a.bibtex").forEach((trigger) => {
  const scope = trigger.closest(".links").parentElement;
  const panel = scope.querySelector(trigger.classList.contains("bibtex") ? ".bibtex.hidden" : ".abstract.hidden");
  if (!panel) return;
  trigger.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;
    event.preventDefault();
    trigger.click();
  });
  new MutationObserver(() => trigger.setAttribute("aria-expanded", String(panel.classList.contains("open")))).observe(panel, {
    attributes: true,
    attributeFilter: ["class"],
  });
});
