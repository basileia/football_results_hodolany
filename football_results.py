from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import time
import json


def create_json(file_name, data):
    """
    Createsjson file
    """
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def write_json(data, filename='tables.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


driver = webdriver.Chrome('C:\\webdrivers\\chromedriver')
driver.get("https://is.fotbal.cz/")

competitions_xpath = '//*[@id="TopMenu_liSoutez"]/a'
competition_number_field_xpath = '//*[@id="txtSearchCislo"]'
search_button_xpath = '//*[@id="btnSearch"]/span'
competition_name_xpath = '//*[@id="MainContent_gridData"]/tbody/tr[2]/td[2]/a'

competition_number = "2020712A1A"
driver.find_element_by_xpath(competitions_xpath).click()
time.sleep(1)
driver.find_element_by_xpath(competition_number_field_xpath).send_keys(competition_number)
time.sleep(2)
driver.find_element_by_xpath(search_button_xpath).click()
time.sleep(1)

while True:
    try:
        driver.find_element_by_xpath(competition_name_xpath).click()
        break
    except ElementClickInterceptedException:
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

url = driver.current_url
tables = pd.read_html(url)

for num in range(len(tables) - 1):
    result = tables[num].to_json()
    parsed = json.loads(result)
    create_json("table" + str(num) + ".json", parsed)


time.sleep(10)
driver.close()
