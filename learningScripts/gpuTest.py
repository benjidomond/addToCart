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
# Importing the Select class to create an object that references select elements
from selenium.webdriver.support.select import Select

# Function that configures and initializes the instance of chrome webdriver, options and service behavior defined above
def chromeDriverInit():
    chrome_Options = Options()
    # Session start
    driver = webdriver.Chrome(options = chrome_Options, service=Service(ChromeDriverManager().install()))
    # Send browser commands to navigate to webpage
    driver.get("https://www.newegg.com/gigabyte-geforce-rtx-3090-ti-gv-n309taorusx-w-24gd/p/N82E16814932510?Item=N82E16814932510&Description=rtx%203090&cm_re=rtx_3090-_-14-932-510-_-Product&quicklink=true")
    driver.implicitly_wait(5)
    buy_button = driver.find_element(By.XPATH, '//*[@id="ProductBuy"]/div[1]/div[2]/button')
    buy_button.click()
    driver.implicitly_wait(5)
    no_thanks_button = driver.find_element(By.XPATH, '//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]')
    no_thanks_button.click()
    view_cart_button = driver.find_element(By.XPATH, '//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[1]')
    view_cart_button.click()
    secure_checkout_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button')
    secure_checkout_button.click()
    email_box = driver.find_element(By.NAME, 'signEmail').send_keys("benjidurdenn@gmail.com" + Keys.ENTER)
    email_box.clear()
    state_select_element = driver.find_element(By.NAME, 'state')
    stateObject = Select(state_select_element)
    driver.quit()
chromeDriverInit()