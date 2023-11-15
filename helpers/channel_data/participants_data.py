from bs4 import BeautifulSoup
from colorama import Fore

from helpers.channel_data.get_settings_from_file import participants_month_plus_enable_setting, \
    participants_week_plus_enable_setting
from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_total_participants_data(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    total = soup.find('span', {'data-num': 'participants'}).text.strip().replace("'", '')
    total_int = int(total)

    if total_int == 0:
        print(Fore.RED + f' нет подписчиков' + Fore.RESET)
        return False

    set_in_arr_by_index(arr=arr, name='подписчиков', value=total_int)

    if participants_month_plus_enable_setting:
        new_week = soup.find('div', id='new_week')
        span_arr = new_week.find_all('span')

        if '-' in span_arr[1].text:
            print(Fore.RED + f' минус подписчиков за месяц {span_arr[1].text}' + Fore.RESET)
            return False

    if participants_week_plus_enable_setting:
        total_week = soup.find('span', {'data-num': 'participants_week'}).text.strip().replace("'", '')

        if '-' in total_week:
            print(Fore.RED + f' минус подписчиков за неделю {total_week}' + Fore.RESET)
            return False

    return True
