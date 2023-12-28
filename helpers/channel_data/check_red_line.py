from bs4 import BeautifulSoup
from colorama import Fore

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def check_red_line(driver):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    alert_div = soup.find('div', class_='alert')

    if alert_div is not None:
        print(Fore.RED + f' есть метка ботовода' + Fore.RESET)
        return f'есть метка ботовода'

    return None
