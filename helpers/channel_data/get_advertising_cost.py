import math

from bs4 import BeautifulSoup
from colorama import Fore
from selenium.webdriver.common.by import By

from helpers.channel_data.get_settings_from_file import cpm_cost_setting
from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_advertising_cost(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    desc = soup.find('span', {'data-num': 'views_per_post'}).text.strip().replace("'", '')
    total_int = int(desc)

    if str(total_int) == 0:
        print(Fore.RED + f' нет стоимость рекламы' + Fore.RESET)
        return f' нет стоимость рекламы'

    cost = math.floor((total_int * cpm_cost_setting) / 1000)

    set_in_arr_by_index(arr=arr, name='стоимость рекламы', value=cost)

    return None
