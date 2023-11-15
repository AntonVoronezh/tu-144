import time
from random import choice

from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from settings.chanel_data_settings import who_mentioned_enable_setting


def get_who_mentioned(driver):
    if who_mentioned_enable_setting:
        data_tables_div = driver.find_element(By.XPATH, '//table[@id="who_mentioned"]')
        ActionChains(driver).scroll_to_element(data_tables_div).perform()
        # driver.execute_script("document.getElementById('who_mentioned').scrollIntoView();")

        out_arr = []
        last_element = None

        while True:
            rand_sleep = choice([5, 6, 7, 8, 9, 10])
            print('прокрутка --sleep-- ', rand_sleep)
            time.sleep(rand_sleep)

            driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", data_tables_div)
            all_elements = driver.find_elements(By.CSS_SELECTOR, 'div.dataTables_scrollBody > table > tbody > tr')
            html = driver.page_source
            soup_for_tr = BeautifulSoup(html, 'lxml')
            data_tables_tr_arr_odd = soup_for_tr.find_all('tr', class_='odd')
            data_tables_tr_arr_even = soup_for_tr.find_all('tr', class_='even')

            for elem in data_tables_tr_arr_odd:
                out_arr.append(elem)
            for elem in data_tables_tr_arr_even:
                out_arr.append(elem)

            try:
                if all_elements[-1] == last_element:
                    break
                else:
                    last_element = all_elements[-1]
            except:
                break

        new_chanel_arr = []
        [new_chanel_arr.append(item) for item in out_arr if item not in new_chanel_arr]
        return new_chanel_arr

    else:
        return None
