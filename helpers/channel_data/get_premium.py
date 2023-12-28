from bs4 import BeautifulSoup

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_premium(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    try:
        premium_count_div = soup.find('div', class_="kt-portlet portlet-channel-common-info")
        premium_count_div_2 = premium_count_div.find('div', class_="kt-widget__bottom")
        premium_count_div_3 = premium_count_div_2.find_all('div', class_="kt-widget__item")
        premium_div = premium_count_div_3[-1]
        span_arr = premium_div.find_all('span')

        premium_count = span_arr[-1].text.strip().replace('%', '')
        set_in_arr_by_index(arr=arr, name='премиум', value=premium_count)
    except:
        set_in_arr_by_index(arr=arr, name='премиум', value='нет данных')

    return None