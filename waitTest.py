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
# Importing exceptions to access them for fluent waits
from selenium.common import exceptions;

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
    #Explicit Wait
    siteLink = WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Automation Step by Step: Never Stop Learning')))
    siteLink.click()
    #Fluent Wait
    fluentWait = WebDriverWait(driver, timeout = 10, poll_frequency = 1, ignored_exceptions=[exceptions.NoSuchElementException])
    fluentWait.until(expected_conditions.element_to_be_clickable((By.XPATH, '')))
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
# It doesn't seem necessary in Python to give elements the WebElement class to use webelement functionality but it seems crucial in Java
# Python function order DOES matter, there's no hoisting of names like other languages (JavaScript etc.)
# Python tuples are a collection type that lets you hold multiple values in a single variable. Tuples are zero indexed, allow duplicates and different data types, are ordered and unchangeable.
# For element_to_be_clickable() to work, it takes one positional argument and not 2. 2 being BY.PARTIAL_LINK_TEXT, 'Automation Step By Step'.
# These 2 arguments can be made one if put inside a tuple
# Element_to_be_clickable() does use find_element internally!
# The two arguments are made into a tuple by throwing parens around them! (Parens are used for tuples!)
# Example: element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Automation Step by Step'))
# So many conditions you can check with explicit waits

# Other points about explicit waits:
# Just like implicit waits, the polling frequency is also 500ms
# Big deal: Mixing implicit and explicit waits can cause unpredictable wait times
# Example: Implicit wait for 10 seconds, Explicit wait for 15 seconds can cause a timeout to occur after 25 seconds
# If you have an implicit wait for 10 seconds and wait to explicit wait for 15 seconds, the best way to do this would to set your explicit wait to 5 and use the 10 of the implicit wait alongside it

# Fluent waits
# Similar to explicit waits in that it waits for a certain duration until a certain condition is true
# Differences
# Polling frequency can be changed as needed
# Fluent waits can ignore exceptions. In the event that an element is not found, such as 'NoElementException', fluent waits can ignore them
# Fluent wait syntax: Very similar to explicit wait and requires WebDriverWait class
# Difference is that after targeting driver and timeout, you can list your poll_frequency and the value you desire
    # poll_frequency = 1
# as well as the ignored exception(s) that you'd like to include. if you include multiple exceptions you'd like to ignore, it's done as an iterable bracket [] structure
# By default, the polling frequency (sleep interval between calls) is 0.5 seconds
# Lastly, utilize until with your fluent waits! (Just like explicit)