import subprocess
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

subprocess.run(["python", "testing.py"])

print("helloososn")

while True:
    time.sleep(10)
    r=requests.post("http://127.0.0.1:6969/")
    if r.status_code == 200:
        print("Reci")
    else:
        print("hmm")

    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Open the URL
    driver.get('http://127.0.0.1:6969/')

    # Wait for the page to load (adjust the time as needed)
    time.sleep(3)

    # Locate the button element you want to press (using an appropriate selector)
    button = driver.find_element(By.ID, 'component-395')  # You can change this to another selector like By.CLASS_NAME, By.NAME, etc.

    # Click the button
    button.click()

    # Alternatively, if you want to simulate a hover action before clicking
    # action = ActionChains(driver)
    # action.move_to_element(button).click().perform()

    # Wait to see the result (optional)
    time.sleep(3)

    # Close the browser after performing the action
    # driver.quit()