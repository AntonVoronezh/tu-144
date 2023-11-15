from bs4 import BeautifulSoup
from colorama import Fore

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_er_data(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    desc = soup.find('span', {'data-num': 'er_per_post'}).text.strip().replace("'", '')

    if len(desc) == 0:
        print(Fore.RED + f' нет ER' + Fore.RESET)
        return False

    text = desc.replace('%', '')
    text_float = float(text)
    set_in_arr_by_index(arr=arr, name='вовлеченность ER', value=text_float)

    return True
