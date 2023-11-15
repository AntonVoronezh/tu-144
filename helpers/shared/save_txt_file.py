import os

from get_path import result_tmp_path


def save_arr_in_txt_file(arr, folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)

    with open(f'{file_path}.txt', 'w', encoding='utf-8') as f:
        for line in arr:
            f.write(f"{line}\n")


# def save_arr_in_txt_file(arr, file_name):
#     file_path = os.path.join(result_path, file_name)
#
#     with open(f'{file_path}.txt', 'w') as f:
#         for line in arr:
#             f.write(f"{line}\n")


def save_in_uniq_txt_file(line, file_name):
    file_path = os.path.join(result_tmp_path, str(file_name))

    with open(f'{file_path}.txt', 'w') as f:
        f.write(f"{line}\n")


def add_more_line_in_txt_file(line, folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)

    with open(f'{file_path}.txt', 'a+', encoding='utf-8') as f:
        f.write(f"{line}\n")
        f.close()