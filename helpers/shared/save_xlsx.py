import os

import pandas as pd

from get_path import result_path, result_xlsx_path
from helpers.by_filter.get_links_from_file import get_arr_from_settings_file
from helpers.shared.get_today import get_today


def save_xlsx():
    columns = get_arr_from_settings_file(file_name='columns')
    sheet_name_good = 'Результат'
    files = os.listdir(result_xlsx_path)

    current_date = get_today()

    out_path = os.path.join(result_path, f'results_{current_date}.xlsx')
    out_arr = []

    for file_name in files:
        file_path = os.path.join(result_xlsx_path, file_name)

        with open(file_path, encoding='utf-8') as file:
            lines_arr = [row.strip() for row in file]
            out_arr.append(lines_arr)
        # print(lines_arr)


    df_good = pd.DataFrame(out_arr, columns=columns)

    with pd.ExcelWriter(out_path) as writer:
        df_good.to_excel(excel_writer=writer, sheet_name=sheet_name_good)


# save_xlsx()
