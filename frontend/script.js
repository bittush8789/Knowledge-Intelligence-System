document.getElementById('ask-btn').addEventListener('click', async () => {
    const question = document.getElementById('question').value;
    const responseContainer = document.getElementById('response-container');
    const responseText = document.getElementById('response-text');
    const askBtn = document.getElementById('ask-btn');

    if (!question) return alert('Please enter a question');

    askBtn.innerText = 'Thinking...';
    askBtn.disabled = true;

    try {
        const response = await fetch('/api/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });
        const data = await response.json();
        
        responseText.innerText = data.answer || 'No answer received.';
        responseContainer.style.display = 'block';
    } catch (err) {
        responseText.innerText = 'Error: Could not connect to the server.';
        responseContainer.style.display = 'block';
    } finally {
        askBtn.innerText = 'Ask AI';
        askBtn.disabled = false;
    }
});
