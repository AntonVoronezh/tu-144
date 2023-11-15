import math
from datetime import datetime
from random import choice

import pandas as pd
from bs4 import BeautifulSoup
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

start_time = datetime.now()

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service(executable_path="C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
link = f'https://telemetr.me'

with open('chanel_arr.txt') as f:
    chanal_arr = f.readlines()
# print(current)


for i, row in enumerate(chanal_arr):
    chanel_name = row.replace('\n', '')
    current_link = f'{link}{chanel_name}'
    print(f'{i + 1} из {len(chanal_arr)}, {chanel_name}', flush=True)
    driver.get(current_link)
    driver.find_element(By.XPATH, "//a[@href='#tab_all_efficiency']").click()

    all_elements = driver.find_elements(By.XPATH, "//div[@class='kt-portlet__body p-4']")
    for el in all_elements:
        if 'Всего' in el.text:
            arr_out = el.text.split('\n')
            count = math.ceil(int(arr_out[1].strip()) / 30)
    print(f'{count} страниц')

    tr_arr_all = []
    tr_arr_all_out = []

    for j in range(1, count):
        # rand_sleep = choice([15, 16, 17, 18, 19, 20])
        # print(j, '--sleep-- ', rand_sleep)
        # time.sleep(rand_sleep)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        data_table = soup.find('div', id='table_efficiency')
        tbody = data_table.find('tbody')
        tr_arr = tbody.find_all('tr')

        for el in tr_arr:
            tr_arr_all.append(el)

        try:
            button = driver.find_element(By.XPATH, "//a[@data-do='load_efficiency_next']")
            driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", button)
            button.click()

        except:
            print('проблемы при прокрутке')
            break

    # название канала\ приход | кодичество такой рекламы
    for i, el in enumerate(tr_arr_all):
        name = el.find('h4')
        count_user = el.find('span', class_="kt-number kt-font-success")
        time = el.find('a', class_="text-underlined")
        count_rekl = el.find('a', class_="kt-number")

        if name is not None:
            n = name.text
            if count_user is not None:
                c_u = count_user.text.replace('пдп.', '').replace("'", "").strip()
                if time is not None:
                    t = time.text.strip()
                    if count_rekl is not None:
                        c_r = count_rekl.text.strip()

                        a = int(c_r) + 1
                        b = math.floor(int(c_u) / a)

                        tr_arr_all_out.append([n, b, a, t])

    df = pd.DataFrame(tr_arr_all_out, columns=['название', 'пдп', 'всего рекл', 'время'])
    # df.to_excel(f"{chanel_name}.xlsx")
    df2 = df.copy()
    with pd.ExcelWriter(f"out/{chanel_name}.xlsx") as writer:
        df.to_excel(writer, sheet_name='Sheet_name_1')
        df2.to_excel(writer, sheet_name='Sheet_name_2')

lambda_ = datetime.now() - start_time
lambda_sec = lambda_.total_seconds()
lambda_sec_out = f'{math.ceil(lambda_sec)} секунд' if lambda_sec < 60 else f'{math.ceil(lambda_sec / 60)} минут'

print(Fore.BLUE + f'\n время выполнения - {lambda_sec_out}' + Fore.RESET)
