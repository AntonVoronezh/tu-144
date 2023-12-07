from bs4 import BeautifulSoup

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_forwarding(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    try:
        forwarding_count_ex = soup.find('a', {'data-sort': 'forwards'})
        forwarding_count = forwarding_count_ex.text.replace('\n','').strip().split(' ')[0]
        set_in_arr_by_index(arr=arr, name='пересылок', value=forwarding_count)
    except:
        set_in_arr_by_index(arr=arr, name='пересылок', value=0)

    return None