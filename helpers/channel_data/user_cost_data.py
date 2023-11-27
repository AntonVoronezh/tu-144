from bs4 import BeautifulSoup

from helpers.channel_data.get_settings_from_file import  cpm_cost_setting
from helpers.shared.set_in_arr_by_index import set_in_arr_by_index



def user_cost_data(driver, arr):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    data_views_subs = soup.find("span", attrs={"data-do": 'show_days_mentions'})
    p_views = data_views_subs.get('data-views')
    p_subs = data_views_subs.get('data-subs')
    p_summ = round((cpm_cost_setting / 1000) * int(p_views))
    p_pdp = round(100 * p_summ / int(p_subs)) / 100

    set_in_arr_by_index(arr=arr, name='стоим подписч', value=p_pdp)

    return None
