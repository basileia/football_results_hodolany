from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import json


def download_results(competition_number):
    """
    Downloads FC Hodolany match results from is.fotbal.cz found by competition
    number
    """
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\\webdrivers\\chromedriver', options=options)
    driver.get("https://is.fotbal.cz/")
    competitions_xpath = '//*[@id="TopMenu_liSoutez"]/a'
    competition_number_field_xpath = '//*[@id="txtSearchCislo"]'
    search_button_xpath = '//*[@id="btnSearch"]/span'
    competition_name_xpath = '//*[@id="MainContent_gridData"]/tbody/tr[2]/td[2]/a'
    elements = [competitions_xpath, competition_number_field_xpath,
                search_button_xpath]
    wait = WebDriverWait(driver, 10)
    for elem in elements:
        wait.until(EC.element_to_be_clickable((By.XPATH, elem))).click()
        if elem == competition_number_field_xpath:
            driver.find_element_by_xpath(competition_number_field_xpath).send_keys(competition_number)
    while True:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, competition_name_xpath))).click()
            break
        except ElementClickInterceptedException:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    tables = pd.read_html(driver.current_url)
    driver.close()
    info_to_json = []
    for table in tables:
        result = table.to_json()
        parsed = json.loads(result)
        info_to_json.append(parsed)
    return info_to_json


def write_json(data, filename='tables.json'):
    """
    Writes given data to json file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


competition_number = "2020712A1A"
write_json(download_results(competition_number))
