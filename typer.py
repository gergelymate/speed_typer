
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

import re

def main():
    url = 'http://10fastfingers.com/typing-test/hungarian'
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@id='words']")))

    s_webpage = str(
        (driver.find_element_by_xpath("//body").get_attribute('innerHTML').replace('\n', '')).encode('utf-8'),
        encoding='utf-8')

    pattern = re.compile('span wordnr="\d*" class="\w*">([^<]+)<')
    words_regex = pattern.findall(s_webpage)

    print(words_regex)

    circle = 0
    last_length = 0
    start_time = time.time()

    for i in range(len(words_regex)-last_length):
        driver.find_element_by_xpath("//input[@id='inputfield']").send_keys('{} '.format(words_regex[i + last_length]))
    last_length = len(words_regex)
    print(last_length)
    
    time.sleep(70)
    driver.quit()

    return

if __name__ == '__main__':
    main()