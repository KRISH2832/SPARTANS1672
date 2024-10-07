// Initialize the verification code variable
let verificationCode = '';

// Function to fetch the CAPTCHA from the API and display it
function fetchCaptcha() {
    fetch('https://krishsharma0413.pythonanywhere.com/api/image-captcha')
        .then(response => response.json()) // Parse the JSON from the API
        .then(data => {
            // Log the JSON data to the console
            console.log("CAPTCHA JSON Response:", data);
            verificationCode = data.verify;
            const captchaImageUrl = `https://krishsharma0413.pythonanywhere.com${data.image}`;
            const captchaImage = document.getElementById('captcha-img');
            captchaImage.src = captchaImageUrl;
        })
        .catch(error => {
            console.error('Error fetching CAPTCHA:', error);
        });
}

// Function to validate the user's CAPTCHA input
function validateCaptcha(event) {
    event.preventDefault();  // Prevent form from submitting
    const userCaptchaInput = document.getElementById('captcha').value;

    // Compare the user input with the verification code
    if (userCaptchaInput === verificationCode) {
        alert('SUCCESS: CAPTCHA matched!');
        // Optionally submit the form if CAPTCHA matches
        document.getElementById('aadhaar-form').submit();
    } else {
        alert('FAILURE: CAPTCHA did not match. Try again.');
    }
}

// Fetch CAPTCHA when the page loads
window.onload = fetchCaptcha;
