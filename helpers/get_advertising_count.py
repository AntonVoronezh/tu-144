import math

from colorama import Fore
from selenium.webdriver.common.by import By

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index
# from settings.chanel_data_settings import advertising_count_enable_setting, advertising_count_setting


def get_advertising_count(driver, arr):
    if advertising_count_enable_setting:
        driver.find_element(By.XPATH, "//a[@href='#tab_all_efficiency']").click()
        all_elements = driver.find_elements(By.XPATH, "//div[@class='kt-portlet__body p-4']")

        average_count = 0

        for el in all_elements:
            if 'За неделю' in el.text:
                arr_out = el.text.split('\n')
                count = int(arr_out[1].strip())
                average_count = math.floor(count / 7)

        if average_count > advertising_count_setting:
            print(Fore.RED + f' много сред кол рекл в день {average_count}' + Fore.RESET)
            return False
        else:
            set_in_arr_by_index(arr=arr, name='сред кол рекл в день', value=average_count)
            return True
    else:
        return False
