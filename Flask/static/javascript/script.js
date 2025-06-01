
  window.addEventListener("scroll", () => {
    const nav = document.getElementById("navbar");
    if (window.scrollY > 10) {
      nav.classList.add("backdrop-blur-md", "bg-white/30", "shadow-md");
    } else {
      nav.classList.remove("backdrop-blur-md", "bg-white/30", "shadow-md");
    }
  });

