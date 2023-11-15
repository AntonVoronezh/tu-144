import os

import pandas as pd

from get_path import result_path


def save_xlsx(columns, arr, file_name, sheet_name):
    # print(columns)
    # print(arr)
    df = pd.DataFrame(arr, columns=columns)

    # print(df)
    file_path = os.path.join(result_path, file_name)
    df.to_excel(excel_writer=f'{file_path}.xlsx', sheet_name=sheet_name)
# ['дата выхода', 'время выхода', 'название', 'комментарий', 'статистика', 'ссылка',
#                                'админ', 'кол подписчиков', 'просм на пост', 'вовлеченность ER', 'стоим подписч',
#                                'упоминания',
#                                'репосты', 'всего ссылок', 'плохих ссылок', 'стоимость рекламы']