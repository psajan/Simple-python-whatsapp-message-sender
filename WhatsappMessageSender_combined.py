import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the phone numbers and messages to send
numbers = ["9848001399", "9848001399"]
message = "Hello, how are you?"

# Specify the path to the Chrome user profile directory
user_data_dir = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data"

# Create a new instance of the Chrome browser with the specified user profile directory
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + user_data_dir)

# Check if WhatsApp is already open in Chrome
driver = webdriver.Chrome(options=options)
try:
    driver.get("https://web.whatsapp.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._3RWII")))
    print("WhatsApp is already open in Chrome")
except:
    print("WhatsApp is not open in Chrome")
    driver.quit()
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    input("Please scan the QR code and press enter to continue...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._3RWII")))

# Loop through each phone number and message
for i in range(len(numbers)):
    # Search for the phone number and select it
    tempmessage=message
    link=f'https://web.whatsapp.com/send?phone=977{numbers[i]}&text={tempmessage}'
    driver.get(link)
    time.sleep(3)  # Wait for chat to load

    # Send the message
    message_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p"))
    )
    message_box.send_keys(tempmessage)
    message_box.send_keys(Keys.RETURN)
     # Wait for message to be sent

# Close the browser
driver.quit()
