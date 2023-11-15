from bs4 import BeautifulSoup
from colorama import Fore

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_view_per_post(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    total = soup.find('span', {'data-num': 'views_per_post'}).text.strip().replace("'", '')
    total_int = int(total)

    set_in_arr_by_index(arr=arr, name='просм на пост', value=total_int)

    if total_int == 0:
        print(Fore.RED + f' нет просм на пост' + Fore.RESET)
        return False

    return True
