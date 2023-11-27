from bs4 import BeautifulSoup
from colorama import Fore
from selenium.webdriver.common.by import By

from helpers.channel_data.get_settings_from_file import mentions_enable_setting, mentions_count_setting
from helpers.shared.set_in_arr_by_index import set_in_arr_by_index



def get_mentions_data(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    desc = soup.find('span', {'data-do': 'show_days_mentions'}).text.strip().replace("'", '')

    text_int = int(desc)

    set_in_arr_by_index(arr=arr, name='упоминания', value=text_int)

    return None
