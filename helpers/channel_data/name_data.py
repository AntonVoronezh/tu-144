from bs4 import BeautifulSoup
from colorama import Fore

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_name_data(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    name = soup.find('a', class_='kt-widget__username').text.strip().replace("'", "")

    set_in_arr_by_index(arr=arr, name='название', value=name)

    if len(name) == 0:
        print(Fore.RED + f' нет имени канала' + Fore.RESET)
        return f'нет имени канала'

    return None
