const container = document.getElementById("keyContainer");

container.innerHTML = generateHTML("-", "-", "-");

window.addEventListener("keydown", (e) => {
    container.innerHTML = generateHTML(
        e.key === " " ? "Space" : e.key, e.code, e.keyCode);
});

function generateHTML(key, code, keycode) {
    return `
    <div class="key-container">
        <h4>Key</h4>
        <div class="key-content">${key}</div>
    </div>

    <div class="key-container">
        <h4>Code</h4>
        <div class="key-content">${code}</div>
    </div>

    <div class="key-container">
        <h4>Key Code</h4>
        <div class="key-content">${keycode}</div>
    </div>
    `;
}