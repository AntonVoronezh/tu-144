from datetime import datetime

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

from helpers.by_filter.get_links_from_file import get_links_from_result_file
from helpers.channel_data.get_data_by_chanel_name import get_data_by_chanel_name
from helpers.shared.ckeck_stages import check_stages
from helpers.shared.save_xlsx import save_xlsx
from helpers.shared.time_lambda import time_lambda

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# service = Service(executable_path="C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=chrome_options)

# service = Service(executable_path="C:\webdrivers\geckodriver.exe", service_args=['--marionette-port', '2828', '--connect-existing'])
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(service=service, options=options)


def get_channels_data_one_by_one(driver):
    start_time = datetime.now()

    channel_names = get_links_from_result_file(file_name='channel_names')

    for i, el in enumerate(channel_names):
        is_in_ready = check_stages(file_name='by_channel_name_ready', stage_name=el.replace('@', ''))
        if is_in_ready:
            print(Fore.YELLOW + f'Данные {channel_names[i]} уже есть' + Fore.RESET)
        else:
            get_data_by_chanel_name(driver=driver, channel_name=el)
            print(f'{i + 1} из {len(channel_names)}, {channel_names[i]}', flush=True)

    save_xlsx()
    time_lambda(start_time=start_time)

