from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import json

# Paths and configuration
print("This assumes you are using the latest chrome browser, you may experience issues if its otherwise")
chromedriver_path = "C:\\Users\\Tee\\Documents\\whatsapp automation\\chromedriver.exe"  # Path to ChromeDriver
user_data_dir = r"C:\Chromedebug"  # Path to Chrome user data directory
profile_directory = "Default"  # Profile directory
url_to_open = "https://web.whatsapp.com"  # URL to open (WhatsApp Web)


def load_config():
    config_file_path = "config.json"
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            config = json.load(f)
        return config
    else:
        # Return default values if the config file doesn't exist
        return {
            "timeout": 180,
            "message": str(input("Enter your name. \t")),
            "contact": str(input("Enter your staff bus name. \t"))
        }

# Get configuration settings
config = load_config()
timeout = config["timeout"]
message = config["message"]
contact = config["contact"]



# Contact and message details
# contact = str(input("Enter your staff bus name. \t"))
# message = str(input("Enter your name. \t"))

# Chrome options to use the existing user profile
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_directory}")

# Service for WebDriver
service = Service(executable_path=chromedriver_path)

try:
    print("Launching Chrome with existing user profile...")
    driver = webdriver.Chrome(service=service, options=options)
    print("Chrome launched successfully!")

    # Open the desired URL
    driver.get(url_to_open)
    print(f"Opened URL: {url_to_open}")

    # Wait for WhatsApp Web to load
    print ("Get ready to link whatsapp web if you haven\'t done so recently")
    print("Waiting for WhatsApp Web to load...")
    time.sleep(15)  # Adjust based on your internet speed and QR codescan time

    # Find the search box and enter the contact name
    print(f"Searching for contact: {contact}")
    search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    search_box.clear()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    print(f"Opened chat for {contact}.")

    # Wait up to 3 minutes (180 seconds) for the message box element to appear
    print("Waiting for the message box to appear...")
    timeout = 180  # Total timeout in seconds (3 minutes)
    interval = 1  # Interval to check for the element (1 second)

    elapsed_time = 0
    message_box = None

    while elapsed_time < timeout:
        try:
            message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]')
            print("Message box appeared!")
            break
        except:
            print(f"Message box not found. Retrying in {interval} second(s)... ({elapsed_time}/{timeout} seconds elapsed)")
            time.sleep(interval)
            elapsed_time += interval

    if message_box:
        # Send the message
        print(f"Sending message to {contact}...")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Message sent to {contact} successfully!")
        time.sleep(10)  #allow message to be sent before closing the browser
    else:
        print("Message box did not appear within the timeout period.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser session
    if 'driver' in locals():
        driver.quit()
        print("Browser session ended.")


import os
import time
import json
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Paths and configuration
chromedriver_path = "C:\\Users\\Tee\\Documents\\whatsapp automation\\chromedriver.exe"  # Path to ChromeDriver
default_user_data_dir = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data")  # Default user data directory path
profile_directory = "Default"  # Profile directory
url_to_open = "https://web.whatsapp.com"  # URL to open (WhatsApp Web)

# Load configuration from the config file
def load_config():
    config_file_path = "config.json"
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            config = json.load(f)
        return config
    else:
        # Return default values if the config file doesn't exist
        return {
            "timeout": 180,
            "message": "Hello, this is a scheduled message.",
            "contact": "Names_bot"
        }

# Get configuration settings
config = load_config()
timeout = config["timeout"]
message = config["message"]
contact = config["contact"]

# Function to get user data directory, either the default or by prompting the user
def get_user_data_dir():
    if os.path.exists(default_user_data_dir):
        return default_user_data_dir  # Return default path if exists
    else:
        # If the default path does not exist, prompt the user to select a folder
        print(f"Default Chrome user data directory not found. Please select your Chrome user data directory.")
        
        # Use tkinter to open a file dialog for selecting a folder
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        user_data_dir = filedialog.askdirectory(title="Select Chrome User Data Directory")
        return user_data_dir

# Get the Chrome user data directory
user_data_dir = get_user_data_dir()

# Chrome options to use the existing user profile
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_directory}")

# Service for WebDriver
service = Service(executable_path=chromedriver_path)

try:
    print("Launching Chrome with existing user profile...")
    driver = webdriver.Chrome(service=service, options=options)
    print("Chrome launched successfully!")

    # Open the desired URL
    driver.get(url_to_open)
    print(f"Opened URL: {url_to_open}")

    # Wait for WhatsApp Web to load
    print("Waiting for WhatsApp Web to load...")
    time.sleep(15)  # Adjust based on your loading speed and QR scan time

    # Find the search box and enter the contact name
    print(f"Searching for contact: {contact}")
    search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    search_box.clear()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    print(f"Opened chat for {contact}.")

    # Wait up to the configured timeout for the message box element to appear
    print(f"Waiting for the message box to appear within {timeout} seconds...")
    interval = 1  # Interval to check for the element (1 second)

    elapsed_time = 0
    message_box = None

    while elapsed_time < timeout:
        try:
            message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]')
            print("Message box appeared!")
            break
        except:
            print(f"Message box not found. Retrying in {interval} second(s)... ({elapsed_time}/{timeout} seconds elapsed)")
            time.sleep(interval)
            elapsed_time += interval

    if message_box:
        # Send the message
        print(f"Sending message to {contact}...")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Message sent to {contact} successfully!")
        time.sleep(10)
    else:
        print("Message box did not appear within the timeout period.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser session
    if 'driver' in locals():
        driver.quit()
        print("Browser session ended.")
