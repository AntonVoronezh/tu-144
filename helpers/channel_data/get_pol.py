from bs4 import BeautifulSoup

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_pol(driver, arr):
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    m = soup.find_all('span', {'data-do': 'show_activities'})
    if len(m) > 0:
        one = m[0].text.strip()
        two = m[1].text.strip()
        out = f'{one}, {two}'
    else:
        out = '-'

    set_in_arr_by_index(arr=arr, name='пол', value=out)