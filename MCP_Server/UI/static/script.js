let websocket = new WebSocket(`ws://${window.location.host}/ws/chat`);

websocket.onopen = function(event) {
    console.log("WebSocket connection opened.");
};

websocket.onmessage = function(event) {
    const messagesDiv = document.getElementById("messages");
    const msg = document.createElement("div");
    msg.className = "bot-message";
    msg.textContent = "Bot: " + event.data;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
};

websocket.onclose = function(event) {
    console.log("WebSocket closed.");
};

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (message === "") return;
    // display user message
    const messagesDiv = document.getElementById("messages");
    const msg = document.createElement("div");
    msg.className = "user-message";
    msg.textContent = "You: " + message;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    // send to server
    websocket.send(message);
    input.value = "";
}

document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});