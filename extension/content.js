// Run when Gmail is fully loaded

function checkEmailForSpam() {
  const emailBody = document.querySelector("div.a3s.aiL");
  if (emailBody && !emailBody.dataset.spamChecked) {
    const rawText = emailBody.innerText;
    emailBody.dataset.spamChecked = "true";
    fetch("https://emailspamextension-6m20m568p-alienminus-projects.vercel.app/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: rawText })
    })
    .then(res => res.json())
    .then(data => {
      const resultTag = document.createElement("div");
      resultTag.style.padding = "6px 12px";
      resultTag.style.margin = "10px 0";
      resultTag.style.fontWeight = "bold";
      resultTag.style.borderRadius = "6px";
      resultTag.style.width = "fit-content";
      if (data.result === "spam") {
        resultTag.innerText = "⚠️ SPAM Detected";
        resultTag.style.backgroundColor = "#f8d7da";
        resultTag.style.color = "#721c24";
        resultTag.style.border = "1px solid #f5c6cb";
      } else {
        resultTag.innerText = "✅ Safe Email";
        resultTag.style.backgroundColor = "#d4edda";
        resultTag.style.color = "#155724";
        resultTag.style.border = "1px solid #c3e6cb";
      }
      const target = document.querySelector("div.ajA");
      if (target) {
        target.parentNode.insertBefore(resultTag, target);
      } else {
        emailBody.appendChild(resultTag);
      }
    })
    .catch(err => console.error("Spam check failed:", err));
  }
}

// Observe DOM changes to detect when a new email is opened
const observer = new MutationObserver(checkEmailForSpam);
observer.observe(document.body, { childList: true, subtree: true });

// Initial check in case email is already open
checkEmailForSpam();