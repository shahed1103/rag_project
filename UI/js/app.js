const sendBtn = document.getElementById("send-btn");
const promptInput = document.getElementById("prompt");
const chatContainer = document.getElementById("chat-container");

sendBtn.addEventListener("click", sendMessage);

function sendMessage() {

    const message = promptInput.value.trim();

    if (!message) return;

    addMessage(message, "user");

    promptInput.value = "";

    fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: message
        })
    })
    .then(res => res.json())
    .then(data => {

        addMessage(data.answer, "ai");

        if (data.sources && data.sources.length > 0) {
            addSources(data.sources);
        }

    })
    .catch(error => {

        console.error(error);

        addMessage("حدث خطأ أثناء الاتصال بالخادم.", "ai");

    });

}

function addMessage(text, type){

    const div = document.createElement("div");

    div.classList.add("message");
    div.classList.add(type);

    div.textContent = text;

    chatContainer.appendChild(div);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}


function addSources(sources){

    const container = document.createElement("div");

    container.classList.add("message");
    container.classList.add("sources");

    let html = `
        <div class="sources-title">
            📚 المصادر المستخدمة
        </div>
    `;

    sources.forEach((source,index)=>{

        html += `
            <div class="source-card">

                <h4>${index+1}. ${source.chapter_title}</h4>

                <p>
                    <strong>الكتاب:</strong> ${source.book_id}<br>
                    <strong>الفصل:</strong> ${source.chapter_id}
                </p>

                <a href="${source.video_youtube_url}" target="_blank">
                    ▶ مشاهدة الدرس على YouTube
                </a>

            </div>
        `;

    });

    container.innerHTML = html;

    chatContainer.appendChild(container);

    chatContainer.scrollTop = chatContainer.scrollHeight;

}