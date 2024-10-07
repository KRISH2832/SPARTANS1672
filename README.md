# SPARTANS1672

## Retrieve Aadhaar Number Web Forms and CAPTCHA API Integration

**Disclaimer:** These web forms and APIs are not intended to mock or replicate the official Unique Identification Authority of India (UIDAI) website. They are created solely for the purpose of testing machine learning solutions that may be used to enhance or replace captcha solutions/challenges. The forms' design, functionality, and APIs are for experimental use only.

### Overview

This project contains multiple web forms that allow users to enter their Aadhaar Number or Enrolment ID to receive an OTP. Each form includes various input fields for user details and a captcha challenge, which is essential for testing purposes. Additionally, a custom API generates CAPTCHA images for testing captcha validation, which is consumed by the JavaScript in the forms.

### Features (Common Across Forms)

- **Radio Buttons:** Allows users to select between Aadhaar Number or Enrolment ID.
- **Input Fields:** 
  - Name
  - Mobile Number
  - Email Address (optional)
- **Captcha Verification:** A placeholder for captcha image generation and validation.
- **ReCAPTCHA Integration:** Each form includes a script to integrate Google’s ReCAPTCHA for additional security (requires a site key).
- **Custom CAPTCHA API Integration:** A custom Python-based API is used to dynamically generate CAPTCHA images, which are fetched and validated using JavaScript.

### Folders and Files Included

#### 1. **ML Folder**
   - This folder contains the necessary API code to generate CAPTCHA images.
   - The API is hosted externally, and its URL is used in the forms to fetch CAPTCHA images dynamically.

##### Key Details for the API:
   - **API Endpoint**: `https://krishsharma0413.pythonanywhere.com/api/image-captcha`
   - **Response Format**: JSON containing:
     - `image`: The CAPTCHA image URL.
     - `verify`: The verification code for matching the CAPTCHA.
   - **Usage in JS**: The form uses the API to display a CAPTCHA image and compares the user’s input with the server-provided verification code.

#### 2. **Uidai-alphanumeric**
   - `index.html`: Main HTML file containing the form structure.
   - `styles.css`: External CSS file for styling the form.
   - `script.js`: External JavaScript file for handling form interactions and CAPTCHA validation.
   - `README.md`: Instructions for usage and setup.

#### 3. **Uidai-clone**
   - `index.html`: Main HTML file containing the form structure.
   - `styles.css`: External CSS file for styling the form.
   - `script.js`: External JavaScript file for handling form interactions and CAPTCHA validation.
   - `README.md`: Instructions for usage and setup.

#### 4. **Uidai-friendly**
   - `index.html`: Main HTML file containing the form structure.
   - `styles.css`: External CSS file for styling the form.
   - `script.js`: External JavaScript file for handling form interactions and CAPTCHA validation.
   - `README.md`: Instructions for usage and setup.

### JavaScript Example Using the API:

```javascript
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
```

#### 5. **Global Files**
   - `.gitignore`: Lists files and folders to be ignored by Git.
   - `README.md`: This combined README.

### Usage

1. Open any of the web forms (`Uidai-alphanumeric`, `Uidai-clone`, or `Uidai-friendly`) in a web browser.
2. Fill out the form by selecting the ID type, entering your name, mobile number, and optionally your email address.
3. Complete the CAPTCHA challenge fetched dynamically from the API.
4. Submit the form to send an OTP (functionality for sending OTP is not implemented in this demo).

### Notes

- These forms use placeholder captcha solutions. Replace the captcha generation and validation logic with a suitable implementation as needed.
- Ensure compliance with data protection regulations when handling user information.

### License

This project is intended for testing and development purposes. It does not carry any license, and use is solely for personal or research purposes. Redistribution or commercial use is not permitted.

---

For any issues or contributions, please refer to the [issues page](https://github.com/M-DEV-1/uidai-clone/issues) or contact the repository maintainer.


