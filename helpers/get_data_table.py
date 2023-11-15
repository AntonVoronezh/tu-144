import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from helpers.get_data_table_info import get_data_table_info


def get_data_table(driver):
    data_tables_div = driver.find_element(By.CLASS_NAME, 'dataTables_scrollBody')
    ActionChains(driver).scroll_to_element(data_tables_div).perform()

    out_arr = []
    out_arr_danger = []
    last_element = None

    while True:
        print(f'прокрутка')

        driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", data_tables_div)
        all_elements = driver.find_elements(By.CSS_SELECTOR, 'div.dataTables_scrollBody > table > tbody > tr')
        html = driver.page_source
        get_data_table_info(html=html, out_arr=out_arr, out_arr_danger=out_arr_danger)
        time.sleep(10)

        try:
            if all_elements[-1] == last_element:
                break
            else:
                last_element = all_elements[-1]
        except:
            pass

    out_arr_set = list(set(out_arr))
    # print('all', len(out_arr_set))
    # for i, elem in enumerate(out_arr_set):
    #     link = elem.find('a')
    # print(i, link.get('href'), flush=True)

    out_arr_danger_set = list(set(out_arr_danger))
    # print('danger', len(out_arr_danger_set))
    return [len(out_arr_set), len(out_arr_danger_set)]
