from selenium import webdriver
import src.db
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"


def get_speed():
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    # options.add_argument("headless")
    # options.add_argument("disable-gpu")
    options.add_argument("window-size=1200x600")
    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.Chrome()
    driver.close()

get_speed()
