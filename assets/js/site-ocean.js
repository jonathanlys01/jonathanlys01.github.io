import { AsciiRenderer, World } from "./ascii-sharks/ocean.min.js";

// Decorative only: no pointer tracking or click effects across the site.
const canvas = document.getElementById("site-ocean");
if (canvas && canvas.getContext("2d")) {
  const world = new World([
    { kind: "classic", size: 0.8 },
    { kind: "hammerhead", size: 0.65 },
  ]);
  const renderer = new AsciiRenderer(canvas);
  renderer.setFontFamily(getComputedStyle(canvas).fontFamily);
  const motion = matchMedia("(prefers-reduced-motion: reduce)");
  const frameInterval = 1000 / 24;
  const step = 1 / 60;
  let frame = 0;
  let last = 0;
  let accumulated = 0;

  function drawStill() {
    // Settle the initial positions before displaying the reduced-motion frame.
    if (world.time < 4) {
      for (let i = 0; i < 240; i++) world.step(step);
    }
    renderer.render(world, step);
  }

  function resize() {
    const { width, height } = canvas.getBoundingClientRect();
    renderer.resize(width, height, Math.min(devicePixelRatio || 1, 1.5));
    world.resize(width, height, renderer.cellWidth, renderer.cellHeight);
    drawStill();
  }

  function animate(now) {
    if (now - last >= frameInterval) {
      // Original swimming speed, independent of the drawing frame rate.
      const elapsed = Math.min((now - last) / 1000, 0.1);
      accumulated += elapsed;
      while (accumulated >= step) {
        world.step(step);
        accumulated -= step;
      }
      renderer.render(world, elapsed);
      last = now;
    }
    frame = requestAnimationFrame(animate);
  }

  function updateMotion() {
    cancelAnimationFrame(frame);
    if (document.hidden || motion.matches) {
      if (!document.hidden) drawStill();
      return;
    }
    last = performance.now();
    accumulated = 0;
    frame = requestAnimationFrame(animate);
  }

  new ResizeObserver(resize).observe(canvas);
  document.addEventListener("visibilitychange", updateMotion);
  motion.addEventListener("change", updateMotion);
  window.addEventListener("pagehide", () => cancelAnimationFrame(frame));
  window.addEventListener("pageshow", updateMotion);
  resize();
  updateMotion();
}
