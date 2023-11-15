from bs4 import BeautifulSoup
from colorama import Fore

from helpers.channel_data.get_settings_from_file import user_cost_enable_setting, user_cost_setting, cpm_cost_setting
from helpers.shared.set_in_arr_by_index import set_in_arr_by_index



def user_cost_data(driver, arr):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    data_views_subs = soup.find("span", attrs={"data-do": 'show_days_mentions'})
    p_views = data_views_subs.get('data-views')
    p_subs = data_views_subs.get('data-subs')
    p_summ = round((cpm_cost_setting / 1000) * int(p_views))
    p_pdp = round(100 * p_summ / int(p_subs)) / 100

    if str(p_pdp) == 0:
        print(Fore.RED + f' нет стоим подписч' + Fore.RESET)
        return False

    if user_cost_enable_setting:
        if p_pdp < user_cost_setting:
            print(Fore.RED + f' маленькая стоим подписч {p_pdp}' + Fore.RESET)
            return False

    set_in_arr_by_index(arr=arr, name='стоим подписч', value=p_pdp)

    return True
