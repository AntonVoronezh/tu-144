import os

from get_path import setting_path, result_tmp_path
from helpers.shared.save_txt_file import save_arr_in_txt_file


def make_links():
    file_path = os.path.join(setting_path, 'channels_setting.txt')
    link = 'https://telemetr.me/channels/?'

    with open(file_path, encoding='utf-8') as f:
        settings_arr = f.readlines()

    settings_arr_out = []
    settings_about_title_out = []

    for el in settings_arr:
        line = el.strip()
        line_arr = line.split('#')
        key = line_arr[1].strip()
        value = line_arr[2].strip()

        if not '_enable_' in key:
            if key == 'title' or key == 'about':
                value_arr = value.split(',')
                for elem in value_arr:
                    res = f'{key}={elem.strip()}'
                    settings_about_title_out.append(res)
            else:
                res = f'{key}={value.replace(" ", "")}'
                settings_arr_out.append(res)

    set_join = '&'.join(settings_arr_out)

    links_arr = []

    for el in settings_about_title_out:
        res = f'{link}{el}&{set_join}&lang_code=any&page=1'
        links_arr.append(res)

    save_arr_in_txt_file(arr=links_arr, folder_path=result_tmp_path, file_name='generated_links_arr')

