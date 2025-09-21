document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'https://encurtador.nadson.dev'; 

    const urlForm = document.getElementById('url-form');
    const submitButton = document.getElementById('submit-button');
    const buttonText = document.querySelector('.button-text');
    const spinner = document.querySelector('.spinner');

    const resultSection = document.getElementById('result-section');
    const shortUrlLink = document.getElementById('short-url-link');
    const qrCodeImg = document.getElementById('qr-code-img');
    const copyButton = document.getElementById('copy-button');

    const errorSection = document.getElementById('error-section');
    const errorMessage = document.getElementById('error-message');

    urlForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        setLoading(true);
        resultSection.classList.add('hidden');
        errorSection.classList.add('hidden');

        const originalUrl = document.getElementById('original-url').value;
        const utm_source = document.getElementById('utm-source').value;
        const utm_medium = document.getElementById('utm-medium').value;
        const utm_campaign = document.getElementById('utm-campaign').value;
        const utm_term = document.getElementById('utm-term').value;
        const utm_content = document.getElementById('utm-content').value;

        const requestBody = {
            original_url: originalUrl,
        };
        if (utm_source) requestBody.utm_source = utm_source;
        if (utm_medium) requestBody.utm_medium = utm_medium;
        if (utm_campaign) requestBody.utm_campaign = utm_campaign;
        if (utm_term) requestBody.utm_term = utm_term;
        if (utm_content) requestBody.utm_content = utm_content;

        try {
            const response = await fetch(`${API_URL}/urls`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestBody),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Ocorreu um erro desconhecido.');
            }

            const data = await response.json();

            displayResults(data);

        } catch (error) {
            displayError(error.message);
        } finally {
            setLoading(false);
        }
    });
    
    copyButton.addEventListener('click', () => {
        navigator.clipboard.writeText(shortUrlLink.href).then(() => {
            copyButton.textContent = 'Copiado!';
            setTimeout(() => {
                copyButton.textContent = 'Copiar';
            }, 2000);
        });
    });

    function setLoading(isLoading) {
        submitButton.disabled = isLoading;
        buttonText.classList.toggle('hidden', isLoading);
        spinner.classList.toggle('hidden', !isLoading);
    }

    function displayResults(data) {
        shortUrlLink.href = data.short_url;
        shortUrlLink.textContent = data.short_url;
        qrCodeImg.src = `${API_URL}/${data.short_code}/qrcode`;
        resultSection.classList.remove('hidden');
    }

    function displayError(message) {
        errorMessage.textContent = `Erro: ${message}`;
        errorSection.classList.remove('hidden');
    }
});