const DEFAULTS = {
  sink_url: "",
  sink_auth_header: "",
  schedule_local_time: "05:00",
  conversations: [],
  stale_after_hours: 48,
  notify_on_stale: true,
};

let conversations = [];

const $ = (id) => document.getElementById(id);

function renderConversations() {
  const container = $("conv-list");
  container.innerHTML = "";
  conversations.forEach((conv, i) => {
    const row = document.createElement("div");
    row.className = "conv-row";

    const idInput = document.createElement("input");
    idInput.type = "text";
    idInput.placeholder = "Conversation ID";
    idInput.value = conv.id;
    idInput.addEventListener("input", (e) => {
      conversations[i].id = e.target.value;
    });

    const labelInput = document.createElement("input");
    labelInput.type = "text";
    labelInput.placeholder = "Label";
    labelInput.value = conv.label;
    labelInput.addEventListener("input", (e) => {
      conversations[i].label = e.target.value;
    });

    const removeBtn = document.createElement("button");
    removeBtn.type = "button";
    removeBtn.textContent = "Remove";
    removeBtn.addEventListener("click", () => {
      conversations.splice(i, 1);
      renderConversations();
    });

    row.append(idInput, labelInput, removeBtn);
    container.appendChild(row);
  });
}

function showStatus(msg) {
  const status = $("status");
  status.textContent = msg;
  status.classList.add("visible");
  setTimeout(() => status.classList.remove("visible"), 2000);
}

function validate() {
  const url = $("sink_url").value.trim();
  if (url && !/^https?:\/\/.+/.test(url)) {
    return "Sink URL must be a valid HTTP(S) URL.";
  }
  if (!$("schedule_local_time").value) {
    return "Schedule time is required.";
  }
  const hours = Number($("stale_after_hours").value);
  if (!Number.isInteger(hours) || hours < 1) {
    return "Staleness threshold must be a whole number of hours, at least 1.";
  }
  for (let i = 0; i < conversations.length; i++) {
    if (!conversations[i].id.trim()) {
      return `Conversation #${i + 1} is missing an ID.`;
    }
  }
  return null;
}

function save() {
  const error = validate();
  if (error) {
    showStatus(error);
    return;
  }
  const config = {
    sink_url: $("sink_url").value.trim(),
    sink_auth_header: $("sink_auth_header").value.trim(),
    schedule_local_time: $("schedule_local_time").value,
    stale_after_hours: Number($("stale_after_hours").value),
    notify_on_stale: $("notify_on_stale").checked,
    conversations: conversations.map((c) => ({
      id: c.id.trim(),
      label: c.label.trim(),
    })),
  };
  chrome.storage.sync.set(config, () => showStatus("Saved"));
}

document.addEventListener("DOMContentLoaded", () => {
  chrome.storage.sync.get(DEFAULTS, (cfg) => {
    $("sink_url").value = cfg.sink_url;
    $("sink_auth_header").value = cfg.sink_auth_header;
    $("schedule_local_time").value = cfg.schedule_local_time;
    $("stale_after_hours").value = cfg.stale_after_hours;
    $("notify_on_stale").checked = cfg.notify_on_stale;
    conversations = cfg.conversations.map((c) => ({ ...c }));
    renderConversations();
  });

  $("toggle-auth").addEventListener("click", () => {
    const input = $("sink_auth_header");
    const btn = $("toggle-auth");
    if (input.type === "password") {
      input.type = "text";
      btn.textContent = "Hide";
    } else {
      input.type = "password";
      btn.textContent = "Show";
    }
  });

  $("add-conv").addEventListener("click", () => {
    conversations.push({ id: "", label: "" });
    renderConversations();
  });

  $("save").addEventListener("click", save);
});
