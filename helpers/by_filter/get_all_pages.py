import os

from bs4 import BeautifulSoup
from colorama import Fore

from get_path import result_tmp_path
from helpers.by_filter.make_name_from_link import make_name_from_link
from helpers.shared.save_screenshot import save_by_filters_screenshots
from helpers.shared.save_txt_file import add_more_line_in_txt_file


def get_all_pages(input_link, driver):
    driver.get(input_link)

    page_source_html = driver.page_source
    soup = BeautifulSoup(page_source_html, 'lxml')
    pag_ul = soup.find('ul', class_='kt-pagination__links')

    if pag_ul is None:
        name_for_save = make_name_from_link(link=input_link)
        save_by_filters_screenshots(driver=driver, name=name_for_save, is_none=True)
        return

    pag_li_arr = pag_ul.find_all('li')
    count = int(pag_li_arr[-1].text)

    for i in range(1, count + 1):
        line = f'{input_link}&page={i}'
        add_more_line_in_txt_file(line=line, folder_path=result_tmp_path, file_name='link_arr_with_pages')
