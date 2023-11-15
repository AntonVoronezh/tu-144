from bs4 import BeautifulSoup
from colorama import Fore
from selenium.webdriver.common.by import By

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_contact_data(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    desc = soup.find('div', class_='kt-widget__info').text.strip().replace('Показать еще...', '').replace(',', '')

    if '@' not in desc:
        print(Fore.RED + f' нет контактных данных' + Fore.RESET)
        return False

    set_in_arr_by_index(arr=arr, name='описание', value=desc)
    return True

