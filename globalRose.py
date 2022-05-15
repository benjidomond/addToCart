# Importing webdriver API to control the browser
from selenium import webdriver
# Service object handles browser driver, used to pass ChromeDriverManager config as chrome webdriver is initialized
from selenium.webdriver.chrome.service import Service
# Options instance defines what the browser must support and how it should behave
from selenium.webdriver.chrome.options import Options
# ChromeDriverManager automatically fetches the most recent version of chrome webdriver and installs it
from webdriver_manager.chrome import ChromeDriverManager
# Importing By functionality to use when finding elements with driver
from selenium.webdriver.common.by import By
# Importing the Keys class to use keys such as tab, enter, escape, etc. within webdriver
from selenium.webdriver.common.keys import Keys

# Configure and initializes the instance of chrome webdriver, options and service behavior defined above
chrome_options = Options()
# Session start
driver = webdriver.Chrome(options = chrome_options, service=Service(ChromeDriverManager().install()))

# Function to access webpage
def getStoreFront():
    # Important note on implicit waits
    # Second duration argument is the max amount of time the driver will wait to find your element or object
    # As soon as the object or element is found, the action will be performed. It won't wait the full second duration unless necessary!
    # Polling interval is 500ms, it'll keep polling every 500ms until the max second duration is reached
    driver.implicitly_wait(5)
    driver.get("https://www.google.com")
    driver.find_element(By.NAME, "q").send_keys("automation step by step" + Keys.ENTER)
    driver.close()
    driver.quit()
# Calling getStoreFront to access the main page
getStoreFront()