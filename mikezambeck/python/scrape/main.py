import datetime
import json
from bs4 import BeautifulSoup
import os
import time
import csv
from dotenv import dotenv_values

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from RPA.Browser.Selenium import Selenium
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys

CURDIR = os.getcwd() + '/'
datalist = []
login_url = 'https://familysearch.org'
login_info = dotenv_values('.env')
# login_info = {'username': 'username',
#               'password': 'password'}


def load_urls():

    with open('./OH.json', 'r') as fp:
        contents = json.load(fp)

    # make list of urls
    url_list = [item.get('image_url') for item in contents['people']]

    # remove header row
    url_list.pop(0)
    return url_list


def parse_data(fp, source: str):
    global datalist
    # with open('./testRLCurl.html', 'r') as fp:
    #     soup = BeautifulSoup(fp, 'html.parser')

    soup = BeautifulSoup(markup=source, features='html.parser')
    tags = soup.find_all('td', class_='ng-scope')
    # print(tags)
    # print(tags[0].string.strip())

    dataline = []
    if len(tags) > 20:
        for i in range(20):
            dataline.append(tags[i].string.strip())
    else:
        for i in range(len(tags)):
            dataline.append(tags[i].string.strip())
        for i in range(20 - len(tags)):
            dataline.append('')

    # dataline = [tags[0].string.strip(), tags[1].string.strip(),
    #             tags[2].string.strip(), tags[3].string.strip(),
    #             tags[5].string.strip(), tags[8].string.strip()]
    print(dataline)

    fp.writerow(dataline)
    # datalist.append(dataline)

# Name 0
# Sex 1
# Age 2
# Date of Death 3
# Date of Birth 5
# Document Number 8


def scrape(records_to_get = 0):
    # global datalist

    print(f'Fetching {records_to_get} records, Ctrl-C to abort.')

    # initiate browser engine
    browser = Selenium()
    browser.set_download_directory(CURDIR)
    # set to True if you don't want to see the action (once working probably better to be headless)
    browser.open_available_browser(headless=False)


    driver: webdriver = browser.driver
    driver.get(login_url)
    driver.implicitly_wait(5)

    # click sign in
    wait = WebDriverWait(driver, 20)
    elem = wait.until(EC.element_to_be_clickable((By.ID, 'signInLink')))
    elem.click()

    # sign in
    elem = wait.until(EC.element_to_be_clickable((By.ID, 'userName')))
    elem.send_keys(login_info['username'])

    elem = driver.find_element(By.ID, 'password')
    elem.send_keys(login_info['password'])

    driver.find_element(By.ID, 'login').click()

    time.sleep(5)

    fp = open(CURDIR + 'data.csv', 'w')
    fplog = open(CURDIR + 'log.txt', 'a')
    write = csv.writer(fp)
    try:
        for i in range(records_to_get):
            try:
                now = datetime.datetime.now()
                print(urls[i])
                driver.get(urls[i])
                # waiting for a data table tag + 1 sec might be efficient
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'td.ng-scope')))
                time.sleep(1)
                # otherwise, fall back on 5 sec delay
                # time.sleep(5)
                parse_data(write, driver.page_source)
                fplog.writelines(f'{now:%Y-%m-%d %H:%M} {urls[i]}' + '\n')
            except KeyboardInterrupt:
                print('User terminated.')
                break
            except:
                fplog.writelines(f'{now:%Y-%m-%d %H:%M} Exception: {urls[i]}' + '\n')
    finally:
        fp.close()
        fplog.close()
        browser.close_browser()

    # save output
    # with open(CURDIR + 'data.csv', 'w') as fp:
    #     write = csv.writer(fp)
    #     write.writerows(datalist)


if __name__ == "__main__":

    # parse urls from json file
    urls = load_urls()

    # how many records to try to read (keep it low for now)
    scrape(2)

    print('fin')

# https://familysearch.org/ark:/61903/3:1:33S7-9PJ1-QY7J
# ['Feltner Horn', 'Male', '17', '09 Oct 1918', 'Single', 'Maranda Angel']
# https://familysearch.org/ark:/61903/3:1:33S7-9PJ1-S92D
# ['Clarence Vincent Buell', 'Male', '1', '05 Feb 1918', 'white', '05 Aug 1916']
# fin

# Name 0
# Sex 1
# Age 2
# Date of Death 3
# Date of Birth 5
# Document Number 8
