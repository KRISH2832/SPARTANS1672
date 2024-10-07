/*
    NOTE:

    - replace current mechanism with recaptcha/captchav3 api
    
*/

// Captcha configuration
const captchaText = "eTnr9hn"; // Static captcha text for demonstration
const captchaCanvas = document.getElementById('captcha-canvas');
const ctx = captchaCanvas.getContext('2d');

captchaCanvas.width = 100;
captchaCanvas.height = 40;

// Draw captcha text on canvas
ctx.font = "30px Arial";
ctx.fillStyle = "#000000";
ctx.fillText(captchaText, 10, 30);

// Validate Captcha
function validateCaptcha() {
    const userInput = document.getElementById('captcha-input').value;
    if (userInput === captchaText) {
        alert("SUCCESS: Captcha verified successfully!");
        // Proceed with form submission or any other logic
    } else {
        alert("FAILURE: Captcha verification failed. Please try again.");
        // Clear the captcha input for retry
        document.getElementById('captcha-input').value = '';
    }
}
