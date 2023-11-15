from colorama import Fore

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index
from settings.chanel_data_settings import who_mentioned_bad_enable_setting, danger_link_setting


def get_danger_count(table_arr, arr):
    count = 0

    if who_mentioned_bad_enable_setting:
        for el in table_arr:
            if 'table-danger' in str(el):
                count = count + 1

        if count > danger_link_setting:
            print(Fore.RED + f' много плохих упоминаний {count}' + Fore.RESET)
            return False

    else:
        set_in_arr_by_index(arr=arr, name='плохие упоминания', value=count)
        return True