# Importing webdriver API to control the browser
from selenium import webdriver
# Service object handles browser driver, used to pass ChromeDriverManager config as chrome webdriver is initialized
from selenium.webdriver.chrome.service import Service
# Options instance defines what the browser must support and how it should behave
from selenium.webdriver.chrome.options import Options
# ChromeDriverManager automatically fetches the most recent version of chrome webdriver and installs it
from webdriver_manager.chrome import ChromeDriverManager

#Function that configures and initializes the instance of chrome webdriver, options and service behavior defined above
def chromeDriverInit():
    chrome_Options = Options()
    # Session start
    driver = webdriver.Chrome(options = chrome_Options, service=Service(ChromeDriverManager().install()))
    # Send browser commands to navigate to webpage
    driver.get("http://www.google.com")
    driver.title # Receiving info from the browser on the website title, property so no ()
    driver.implicitly_wait(0.5) # Waiting 0.5 seconds for the element to be available - better ways to handle waiting. Syncs code w/ webpage contents
    # Session end
    driver.quit()