import os

import pandas as pd

from get_path import result_path, result_xlsx_path
from helpers.by_filter.get_links_from_file import get_arr_from_settings_file


def save_xlsx():
    columns = get_arr_from_settings_file(file_name='columns')
    sheet_name_good = 'Прошли проверку'
    sheet_name_bad = 'НЕ прошли проверку'
    files = os.listdir(result_xlsx_path)
    out_path = os.path.join(result_path, 'results.xlsx')

    good_arr = []
    bad_arr = []

    for file_name in files:
        file_path = os.path.join(result_xlsx_path, file_name)

        with open(file_path, encoding='utf-8') as file:
            lines_arr = [row.strip() for row in file]

        if 'plus_' in file_name:
            good_arr.append(lines_arr)

        if 'minus_' in file_name:
            bad_arr.append(lines_arr)

    df_good = pd.DataFrame(good_arr, columns=columns)
    df_bad = pd.DataFrame(bad_arr, columns=columns)

    with pd.ExcelWriter(out_path) as writer:
        df_good.to_excel(excel_writer=writer, sheet_name=sheet_name_good)
        df_bad.to_excel(excel_writer=writer, sheet_name=sheet_name_bad)


save_xlsx()
