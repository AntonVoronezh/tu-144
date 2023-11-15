from bs4 import BeautifulSoup
from colorama import Fore

from get_path import result_tmp_path
from helpers.by_filter.get_links_from_file import get_arr_from_tmp_file
from helpers.by_filter.make_name_from_link import make_name_from_link
from helpers.shared.rand_sleep import rand_sleep
from helpers.shared.save_screenshot import save_by_filters_screenshots
from helpers.shared.save_txt_file import save_in_uniq_txt_file, add_more_line_in_txt_file


def get_data_from_link(input_link, driver):
    name_for_save = make_name_from_link(link=input_link)

    ready_arr = get_arr_from_tmp_file(file_name='ready')
    if name_for_save in ready_arr:
        print(Fore.YELLOW + f'уже было' + Fore.BLUE +f'{name_for_save}' + Fore.RESET)
        return


    print(Fore.BLUE + f'{name_for_save}' + Fore.RESET)
    driver.get(input_link)

    save_by_filters_screenshots(driver=driver, name=name_for_save, is_none=False)

    html_link = driver.page_source
    soup_link = BeautifulSoup(html_link, 'lxml')
    td_arr = soup_link.find_all('td', class_='text-center wd-100 pb-0')

    for j, td in enumerate(td_arr):
        link = td.find("a")
        href = link.get("href")
        add_more_line_in_txt_file(line=href[1:], folder_path=result_tmp_path, file_name='channel_names_not_uniq')

        print(j, href)

    add_more_line_in_txt_file(line=name_for_save, folder_path=result_tmp_path, file_name='ready')
    # rand_sleep(start=5, end=10)