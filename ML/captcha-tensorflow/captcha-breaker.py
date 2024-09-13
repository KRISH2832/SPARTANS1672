from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from tensorflow.keras.saving import load_model
from PIL import Image
import numpy as np
import tensorflow as tf

H, W, C = 100, 120, 3
model = load_model("./final_model.keras")


def predict(filepath):
    # Load and preprocess the image
    im = Image.open(filepath)
    im = im.resize((W, H))  # Resize to match the model's expected input shape
    im = np.array(im) / 255.0  # Normalize the image
    im = np.expand_dims(im, 0)  # Add a batch dimension, making the shape (1, H, W, 3)

    # Predict using the model
    y_pred = model.predict(im)
    
    # Convert the predicted probabilities to class labels
    y_pred = tf.math.argmax(y_pred, axis=-1)
    
    # Convert numerical labels back to characters (assuming it's a character classification task)
    predicted_labels = ''.join([chr(i) for i in y_pred.numpy()[0]])
    
    return predicted_labels


chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://spartans-captcha.netlify.app/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "captcha-img"))
)

import time
time.sleep(10)

# put "krish" in input tag with id="name"
name_input = driver.find_element(By.ID, "name")
name_input.send_keys("krish")

number_input = driver.find_element(By.ID, "mobile")
number_input.send_keys("8287735005")

# download image that is stored in id="captcha-img" img tag within src
captcha_img = driver.find_element(By.ID, "captcha-img")
src = captcha_img.get_attribute("src")

import requests
response = requests.get(src)

with open("captcha.png", "wb") as f:
    f.write(response.content)

predicted_text = str(predict("captcha.png"))

captcha_input = driver.find_element(By.ID, "captcha")
captcha_input.send_keys(predicted_text)

# press submit button
submit_button = driver.find_element(By.ID, "send-otp")
submit_button.click()

time.sleep(5)


# with open("website.html", "w", encoding="utf-8") as f:
#     f.write(driver.page_source)