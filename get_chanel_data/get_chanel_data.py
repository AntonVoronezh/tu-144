import os
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from get_path import result_path
from helpers.channel_data.name_data import get_name_data
from helpers.channel_data.contact_data import get_contact_data
from helpers.channel_data.participants_data import get_total_participants_data
from helpers.channel_data.get_view_per_post import get_view_per_post
from helpers.channel_data.er_data import get_er_data
from helpers.channel_data.get_mentions_data import get_mentions_data
from helpers.channel_data.get_reposts_data import get_reposts_data
from helpers.channel_data.get_advertising_cost import get_advertising_cost
from helpers.shared.make_zip import make_zip
from helpers.shared.rand_sleep import rand_sleep
from helpers.shared.save_screenshot import save_channel_data_screenshots
from helpers.shared.save_xlsx import save_xlsx
from helpers.shared.set_in_arr_by_index import set_in_arr_by_index
from helpers.channel_data.user_cost_data import user_cost_data
from helpers.shared.time_lambda import time_lambda
from settings.main import current_result_for

start_time = datetime.now()

link = f'https://telemetr.me'

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service(executable_path="C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

file_path = os.path.join(result_path, 'channel_names')

with open(f'{file_path}.txt') as file:
    channel_arr = [row.strip() for row in file]

# работа с выходным массивом
with open("columns.txt", encoding='utf-8') as file:
    lines = [row.strip() for row in file]

total_info_arr = []


def get_data_from_link(channel_name, i):
    current_link = f'{link}/{channel_name}'
    # print(f'{i + 1} из {len(channel_arr)}, {channel_name}', flush=True)
    driver.get(current_link)

    save_channel_data_screenshots(driver=driver, name=channel_name)

    rand_sleep(start=5, end=10)

    total_info_arr_for_i = [''] * len(lines)

    # название канала
    name = get_name_data(driver=driver, arr=total_info_arr_for_i)
    if not name:
        return

    # описание
    contact_data = get_contact_data(driver=driver, arr=total_info_arr_for_i)
    if not contact_data:
        return

    # ссылка на статистику
    set_in_arr_by_index(arr=total_info_arr_for_i, name='статистика', value=current_link)

    # ссылка на канал
    tg_link = channel_name.replace('@', '')
    set_in_arr_by_index(arr=total_info_arr_for_i, name='ссылка', value=f'http://t.me/{tg_link}')

    # подписчики
    participants = get_total_participants_data(driver=driver, arr=total_info_arr_for_i)
    if not participants:
        return

    # просм на пост
    view_per_post = get_view_per_post(driver=driver, arr=total_info_arr_for_i)
    if not view_per_post:
        return

    # вовлеченность ER
    er = get_er_data(driver=driver, arr=total_info_arr_for_i)
    if not er:
        return

    # упоминания
    mentions = get_mentions_data(driver=driver, arr=total_info_arr_for_i)
    if not mentions:
        return

    # репосты
    reposts = get_reposts_data(driver=driver, arr=total_info_arr_for_i)
    if not reposts:
        return

    # стоим подписч
    user_cost = user_cost_data(driver=driver, arr=total_info_arr_for_i)
    if not user_cost:
        return

    # стоимость рекламы
    advertising_cost = get_advertising_cost(driver=driver, arr=total_info_arr_for_i)
    if not advertising_cost:
        return

    # save_line_in_txt_file(line=total_info_arr_for_i, file_name=tg_link)
    # total_info_arr.append(total_info_arr_for_i)
# for i, row in enumerate(chanal_arr):


#
#     # контакты для рассылки
#     contact_data_extract = get_contact_data_extract(driver=driver, arr=total_info_arr_for_i, chanel_name=name, chanel_link=chanel_name)
#
#     # таблица упоминаний
#     # who_mentioned_table = get_who_mentioned(driver=driver)
#     # if who_mentioned_table is None:
#     #     continue
#     # else:
#     #     # плохие упоминания
#     #     danger_count = get_danger_count(table_arr=who_mentioned_table, arr=total_info_arr_for_i)
#     #     if not danger_count:
#     #         continue
#
#     # сред кол рекл в день
#     advertising_count = get_advertising_count(driver=driver, arr=total_info_arr_for_i)
#     if not advertising_count:
#         continue
#
#     print(total_info_arr_for_i)
#
#
#
#         # if advertising_count > advertising_count_setting:
#         #     print(Fore.RED + f' много рекламы в день {advertising_count}' + Fore.RESET)
#         #
#         # current_total_info = get_total_info(driver=driver, current_link=current_link, chanel_name=chanel_name)
#         # if current_total_info is not None:
#         #     data_table = get_data_table(driver=driver)
#         #     if data_table is not None:
#         #         danger_link_count = data_table[1]
#         #         if danger_link_count > danger_link_setting:
#         #             print(Fore.RED + f'много плохих ссылок {danger_link_count}' + Fore.RESET)
#         #
#         #
#         #         else:
#         #             all_link_count = data_table[0]
#         #
#         #             new_current_total_info = []
#         #
#         #             for el in current_total_info:
#         #                 new_current_total_info.append(el)
#         #
#         #             new_current_total_info.append(all_link_count)
#         #             new_current_total_info.append(danger_link_count)
#         #             total_info_arr.append(new_current_total_info)
#         #
#         #
#


for i, el in enumerate(channel_arr):
    get_data_from_link(channel_name=el, i=i)

save_xlsx(arr=total_info_arr, columns=lines, file_name='result', sheet_name='Прошли проверку')

time_lambda(start_time=start_time)

make_zip(folder_path=result_path, folder_name=current_result_for)
