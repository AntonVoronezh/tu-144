from bs4 import BeautifulSoup
from colorama import Fore
from selenium.webdriver.common.by import By

from helpers.channel_data.get_settings_from_file import reposts_enable_setting, reposts_count_setting
from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_reposts_data(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    desc = soup.find('span', {'data-original-title': 'Репостов'}).text.strip().replace("'", '')

    text_int = int(desc)

    if len(desc) == 0:
        print(Fore.RED + f' нет репостов' + Fore.RESET)
        return False

    if reposts_enable_setting:
        if text_int < reposts_count_setting:
            print(Fore.RED + f' мало репостов {text_int}' + Fore.RESET)
            return False

    set_in_arr_by_index(arr=arr, name='репосты', value=text_int)

    return True
