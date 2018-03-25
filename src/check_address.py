import time
from selenium import webdriver
import re
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"


def get_speed(address):
    address_to_send = address.split(",")[0:2]
    print("Checking address {0}".format(address_to_send))
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    # options.add_argument("headless")
    # options.add_argument("disable-gpu")
    options.add_argument("window-size=1024x600")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://shop.centurylink.com/MasterWebPortal/freeRange/shop/guidedShoppingStart?bones#module=start")
    try:

        time.sleep(4)
        driver.find_element_by_id("ctam_addressLine").send_keys("{0}, {1}, MN".format(address_to_send[0], address_to_send[1]))
        driver.find_elements_by_css_selector("#ul-0 > li:nth-child(1) > md-autocomplete-parent-scope > span")[0].click()
    except:
        time.sleep(4)
        driver.find_element_by_id("ctam_addressLine").clear()
        driver.find_element_by_id("ctam_addressLine").send_keys("{0}, {1}, MN".format(address_to_send[0], address_to_send[1]))
        time.sleep(1)
        if driver.find_elements_by_css_selector("#ul-0 > li:nth-child(1) > md-autocomplete-parent-scope"):
            driver.find_elements_by_css_selector("#ul-0 > li:nth-child(1) > md-autocomplete-parent-scope")[0].click()
        else:
            driver.find_element_by_css_selector("#getStarted_addressForm > div.ctam_entry.transform-parent > div > span > button:nth-child(1)").click()
    try_count = 0
    time.sleep(1)
    if driver.find_elements_by_css_selector("#getStarted_addressForm > div.ctam_entry.transform-parent > div > span > button:nth-child(1)"):
        try:
            driver.find_element_by_css_selector("#getStarted_addressForm > div.ctam_entry.transform-parent > div > span > button:nth-child(1)").click()
            while not driver.find_elements_by_id("secUnitList_0") and not driver.find_elements_by_css_selector("#getStarted_addressForm > div.secUnitNearMatchCase > div > div.secUnitMatch_button > button"):
                time.sleep(1)
        except:
            time.sleep(1)
    time.sleep(3)
    if driver.find_elements_by_id("secUnitList_0"):
        driver.find_element_by_id("secUnitList_0").click()
        driver.find_element_by_css_selector("#getStarted_addressForm > div.secUnitNearMatchCase > div > div.secUnitMatch_button > button").click()
    if driver.current_url in "https://www.centurylink.com/home/calltoorder/page.CallToOrder.dtvLoopQual.html":
        print("CL error page displayed")
        return 0
    if driver.find_elements_by_id("addrTryAgain"):
        if driver.find_element_by_id("addrTryAgain").is_displayed():
            return -1
    while not driver.find_elements_by_id("choiceModule") and try_count < 5:
        try_count += 1
        time.sleep(1)
    try_count = 0
    while not driver.find_element_by_id("choiceModule").is_displayed() and try_count < 5:
        try_count += 1
        time.sleep(1)
    try_count = 0
    while not driver.find_element_by_css_selector("#choiceModule > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > div.innerBox > div.hidden-xs.buttonWrap.bonesButton > button").is_displayed() and try_count < 5:
        try_count += 1
        time.sleep(1)
    if driver.find_elements_by_xpath('//*[@id="choiceModule"]/div[2]/div/div[3]/button'):
        if "Shop For Other Services" in driver.find_element_by_xpath('//*[@id="choiceModule"]/div[2]/div/div[3]/button').text:
            return -1
    if driver.find_elements_by_xpath('//*[@id="mainoffer"]/p[1]'):
        if driver.find_element_by_xpath('//*[@id="mainoffer"]/p[1]'):
            print("debug")

    if not driver.find_elements_by_css_selector("#choiceModule > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > div.innerBox > div.hidden-xs.buttonWrap.bonesButton > button"):
        return -1.5
    try:
        driver.find_element_by_css_selector("#choiceModule > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > div.innerBox > div.hidden-xs.buttonWrap.bonesButton > button").click()
    except:
        time.sleep(5)
        try:
            driver.find_element_by_css_selector("#choiceModule > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > div.innerBox > div.hidden-xs.buttonWrap.bonesButton > button").click()
        except:
            return -1
    try_count = 0
    while not re.findall("thisProd\['downDisplay'\].*", driver.page_source):
        try_count += 1
        time.sleep(2)
        if try_count > 4:
            return -1
    found_speeds = re.findall("thisProd\['downDisplay'\].*", driver.page_source)
    highest_speed = 0
    for speed in found_speeds:
        curr_speed = float(re.sub(r'[a-zA-Z\'\[\]\"\;=\s]+', r'', speed))
        if curr_speed > highest_speed:
            highest_speed = curr_speed
    print("Highest speed found: {0} Mbps".format(highest_speed))
    driver.close()
    return highest_speed