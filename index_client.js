// Proxy URL (server will forward requests to OpenRouter and keep the API key secret)
// Use full backend URL when running the frontend with a dev server (e.g. Live Server on :5500)
const url = (window.location.port === '5500') ? 'http://localhost:3000/api/chat' : '/api/chat';

// Only send JSON content-type from the client; Authorization is handled on the server
const headers = {
    "Content-Type": "application/json"
};

// Warten bis DOM geladen ist
const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const output = document.getElementById("response-output");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    output.textContent = "Wird geladen...";

    const userPrompt = input.value;
        const payload = {
            model: "gpt-oss-120b",
            messages: [
                { role: "system", content: "Du bist ein asozialer, mürrischer Assistent, der kurz auf Fragen antwortet. Halte dich kurz und verwende keine Emojis." },
                { role: "user", content: userPrompt }
            ],
            temperature: 0.4,
            top_p: 0.8
        };

        try {
            const response = await fetch(url, {
                method: "POST",
                headers,
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                // forward server error message if available
                const errText = await response.text();
                throw new Error(`API-Fehler: ${response.status} ${errText}`);
            }

            const data = await response.json();
            
            if (data.choices && data.choices[0] && data.choices[0].message) {
                output.textContent = data.choices[0].message.content;
            } else {
                output.textContent = "Keine Antwort von der API erhalten.";
            }
        } catch (err) {
            output.textContent = "Fehler: " + err.message;
        }
    });
