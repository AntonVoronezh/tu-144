import os

from get_path import result_tmp_path


def check_stages(file_name, stage_name):
    file_path = os.path.join(result_tmp_path, f'{file_name}.txt')

    if not os.path.exists(file_path):
        return False

    with open(file_path, encoding='utf-8') as file:
        stages_arr = [row.strip() for row in file]

    if stage_name in stages_arr:
        return True

    return False
