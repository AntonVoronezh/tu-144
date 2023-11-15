from bs4 import BeautifulSoup


def get_data_table_info(html, out_arr, out_arr_danger):
    soup_for_tr = BeautifulSoup(html, 'lxml')
    data_tables_tr_arr_odd = soup_for_tr.find_all('tr', class_='odd')
    data_tables_tr_arr_even = soup_for_tr.find_all('tr', class_='even')
    data_tables_tr_arr_danger = soup_for_tr.find_all('tr', class_='table-danger')

    for elem in data_tables_tr_arr_danger:
        out_arr_danger.append(elem)

    for elem in data_tables_tr_arr_even:
        out_arr.append(elem)

    for elem in data_tables_tr_arr_odd:
        out_arr.append(elem)
