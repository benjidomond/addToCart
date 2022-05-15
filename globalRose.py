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
# Importing WebDriverWait class to gain access to explicit waits
from selenium.webdriver.support.ui import WebDriverWait
# Importing ExpectedConditions class to verify element conditions / general conditions during explicit waits
from selenium.webdriver.support import expected_conditions

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
    # The implicit wait is applied to each action following it after it's set until the driver performs close() and quit()
    driver.implicitly_wait(5)
    driver.get("https://www.google.com")
    driver.find_element(By.NAME, "q").send_keys("automation step by step" + Keys.ENTER)
    WebDriverWait(driver, timeout=10).until()
    driver.close()
    driver.quit()
# Calling getStoreFront to access the main page
getStoreFront()

# Important note on explicit waits
# Explicit waits are used to make webdriver wait until a certain condition is true to perform a task
# Must import WebDriverWait class to access
# from selenium.webdriver.support.ui import WebDriverWait
# To test explicit waits, after googling automation step by step we plan to wait until the link to the website is clickable
# An immensely helpful class for verifying element conditions / general conditions is the ExpectedConditions class. Super helpful to import!
# ExpectedConditions help with verifying element conditions, general conditions and help make testing explicit waits easier
# from selenium.webdriver.support import expected_conditions
# When checking element conditions, remember to use the By class to target the elements

def explicitWaitTest():
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable(By.PARTIAL_LINK_TEXT, 'Automation Step by Step: Never Stop Learning'))