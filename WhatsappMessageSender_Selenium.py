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
driver = webdriver.Chrome(options=options)

# Loop through each phone number and message
for i in range(len(numbers)):
    # Send the message
    tempmessage = message
    link = f'https://web.whatsapp.com/send?phone=977{numbers[i]}&text={tempmessage}'
    driver.get(link)
    input("Please scan the QR code and press enter to continue...")
    time.sleep(3)  # Wait for chat to load
    # Wait for the message input field to be visible
    message_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p"))
    )

    # Send the message
    message_box.send_keys(tempmessage)
    message_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for message to be sent

# Close the browser
driver.quit()

#/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p