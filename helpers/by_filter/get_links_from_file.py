import os

from get_path import result_tmp_path, result_path, setting_path


def get_arr_from_tmp_file(file_name):
    file_path = os.path.join(result_tmp_path, f'{file_name}.txt')

    links_arr = []

    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            links_arr = [row.strip() for row in file]

    return links_arr


def get_links_from_result_file(file_name):
    file_path = os.path.join(result_path, f'{file_name}.txt')

    links_arr = []

    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            links_arr = [row.strip() for row in file]

    return links_arr


def get_arr_from_settings_file(file_name):
    file_path = os.path.join(setting_path, f'{file_name}.txt')

    links_arr = []

    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            links_arr = [row.strip() for row in file]

    return links_arr


def get_arr_from_tmp_file_for_lsx(file_name):
    file_path = os.path.join(result_tmp_path, f'{file_name}.txt')

    out_arr = []

    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            for el in file:
                el_r = el.replace('[', '').replace(']', '').replace('\n', '').replace('\t', '').replace("'", "")
                el_split = el_r.split(',')
                print(len(el_split))
                f = []
                for i in el_split:
                    f.append(i)

                out_arr.append(f)
    # print('out_arr', out_arr)
    return out_arr
