from datetime import datetime

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from get_path import result_tmp_path, clear_tmp_dir, result_path
from helpers.by_filter.get_all_pages import get_all_pages
from helpers.by_filter.get_data_from_link import get_data_from_link
from helpers.by_filter.get_links_from_file import get_arr_from_tmp_file
from helpers.by_filter.make_links import make_links
from helpers.shared.ckeck_stages import check_stages
from helpers.shared.make_uniq_arr import make_uniq_arr
from helpers.shared.save_txt_file import add_more_line_in_txt_file, save_arr_in_txt_file

from helpers.shared.time_lambda import time_lambda

# username = "telemetr.obucheniye@mail.ru"
# password = "obuchTG123"

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# service = Service(executable_path="C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=chrome_options)

# service = Service(executable_path="C:\webdrivers\geckodriver.exe", service_args=['--marionette-port', '2828', '--connect-existing'])
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(service=service, options=options)

# pageSource = driver.page_source
# print(pageSource)


def get_channels_by_filter(driver):
    start_time = datetime.now()

    make_links()
    generated_links_from_file = get_arr_from_tmp_file(file_name='generated_links_arr')

    is_in_stages_1 = check_stages(file_name='by_filter_stages', stage_name='generated_links_from_file')
    if is_in_stages_1:
        print(Fore.YELLOW + f'Данные generated_links_from_file уже есть' + Fore.RESET)
    else:
        for el in generated_links_from_file:
            get_all_pages(input_link=el, driver=driver)
        add_more_line_in_txt_file(line='generated_links_from_file', folder_path=result_tmp_path,
                                      file_name='by_filter_stages')

    link_arr_with_pages_from_file = get_arr_from_tmp_file(file_name='link_arr_with_pages')

    is_in_stages_2 = check_stages(file_name='by_filter_stages', stage_name='link_arr_with_pages_from_file')
    if is_in_stages_2:
        print(Fore.YELLOW + f'Данные link_arr_with_pages_from_file уже есть' + Fore.RESET)
    else:
        for el in link_arr_with_pages_from_file:
            get_data_from_link(input_link=el, driver=driver)
        add_more_line_in_txt_file(line='link_arr_with_pages_from_file', folder_path=result_tmp_path, file_name='by_filter_stages')

    not_uniq_arr = get_arr_from_tmp_file(file_name='channel_names_not_uniq')
    uniq_arr = make_uniq_arr(arr=not_uniq_arr)
    save_arr_in_txt_file(arr=uniq_arr, folder_path=result_path, file_name='channel_names')
    # clear_tmp_dir()

    time_lambda(start_time=start_time)
