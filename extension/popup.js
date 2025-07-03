document.addEventListener("DOMContentLoaded", () => {
  const checkBtn = document.getElementById("checkBtn");
  const emailText = document.getElementById("emailText");
  const resultDiv = document.getElementById("result");
  const darkToggle = document.getElementById("darkToggle");

  // Load saved theme
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark" || (!savedTheme && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
    document.body.classList.add("dark");
    darkToggle.checked = true;
  }

  darkToggle.addEventListener("change", () => {
    if (darkToggle.checked) {
      document.body.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  });

  checkBtn.addEventListener("click", () => {
    const text = emailText.value;
    fetch("https://emailspamextension-git-main-alienminus-projects.vercel.app/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    })
    .then(res => res.json())
    .then(data => {
      resultDiv.style.display = "block";
      resultDiv.className = data.result === "spam" ? "spam" : "safe";
      resultDiv.textContent = data.result === "spam"
        ? "⚠️ This email is likely SPAM."
        : "✅ This email seems safe.";
    })
    .catch(() => {
      resultDiv.style.display = "block";
      resultDiv.className = "";
      resultDiv.textContent = "❌ Error: Could not connect to server.";
    });
  });
});
