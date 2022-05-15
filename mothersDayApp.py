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
# Import Select class to interact with select list to choose delivery date etc.
from selenium.webdriver.support.select import Select
# Importing WebDriverWait class to gain access to explicit waits
from selenium.webdriver.support.ui import WebDriverWait
# Importing ExpectedConditions class to verify element conditions / general conditions during explicit waits
from selenium.webdriver.support import expected_conditions


# Configure and initializes the instance of chrome webdriver, options and service behavior defined above
chrome_options = Options()
# Session start
driver = webdriver.Chrome(options = chrome_options, service=Service(ChromeDriverManager().install()))

#Retrieving the GlobalRose storefront
def getMomRoses():
    driver.get("https://www.globalrose.com")
    # Using the search bar to search for Mother's Day flowers
    driver.find_element(By.NAME, "q").send_keys("Mother's Day" + Keys.ENTER)
    #Finding and retrieving roses
    #Text is inside a div <a> <div> text </div> </a>
    roseLink = WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'div#qty-roses > div.flag > a')))
    # qty roses div id -> div with class flag -> a tag to access qty roses
    roseLink.click()
    # Implicit wait is your best solution to make sure that the calendar gets the right dates and shipping time, selecting span difficult
    driver.implicitly_wait(0.5)
    deliveryDateSelect = driver.find_element(By.ID, "selectdate")
    deliveryDateObject = Select(deliveryDateSelect)
    # Selects the earliest available date to get the flowers!
    deliveryDateObject.select_by_index(1)
    # Selecting the quantity of Roses
    driver.find_element(By.ID, "cyq-qty-input").send_keys("value", "3")
    # Picking the location of the pink selector and clicking it
    driver.find_element(By.CSS_SELECTOR, "[aria-label='pink']").click()
    # Adding flowers to cart
    driver.find_element(By.ID, "topA2C").click()
    driver.quit()
getMomRoses()