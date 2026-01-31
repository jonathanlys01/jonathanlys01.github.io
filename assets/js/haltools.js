/* Sync HAL iframe theme with site theme */
(() => {
  const determineThemeSetting = () => {
    const themeSetting = localStorage.getItem("theme");
    return (themeSetting !== "dark" && themeSetting !== "light" && themeSetting !== "system") ? "system" : themeSetting;
  };

  const determineComputedTheme = () => {
    const themeSetting = determineThemeSetting();
    if (themeSetting !== "system") {
      return themeSetting;
    }
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  };

  const resolveTheme = () => {
    const htmlTheme = document.documentElement.getAttribute("data-theme");
    if (htmlTheme === "dark") {
      return "dark";
    }
    return determineComputedTheme();
  };

  const updateHaltoolsIframes = () => {
    const iframes = document.querySelectorAll("iframe.haltools-iframe");
    if (!iframes.length) {
      return;
    }

    const theme = resolveTheme();
    const cssKey = (theme === "dark") ? "haltoolsCssDark" : "haltoolsCssLight";

    iframes.forEach((iframe) => {
      const cssUrl = iframe.dataset[cssKey];
      const srcValue = iframe.getAttribute("src");
      if (!cssUrl || !srcValue) {
        return;
      }

      let src;
      try {
        src = new URL(srcValue, window.location.href);
      } catch (err) {
        return;
      }

      if (src.searchParams.get("css") === cssUrl) {
        return;
      }

      src.searchParams.set("css", cssUrl);
      iframe.setAttribute("src", src.toString());
    });
  };

  document.addEventListener("DOMContentLoaded", () => {
    updateHaltoolsIframes();

    const themeObserver = new MutationObserver(() => updateHaltoolsIframes());
    themeObserver.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-theme"],
    });

    const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    if (mediaQuery.addEventListener) {
      mediaQuery.addEventListener("change", () => updateHaltoolsIframes());
    } else if (mediaQuery.addListener) {
      mediaQuery.addListener(() => updateHaltoolsIframes());
    }
  });
})();

