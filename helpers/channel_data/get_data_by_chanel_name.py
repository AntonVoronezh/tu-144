from get_path import result_tmp_path, result_xlsx_path
from helpers.by_filter.get_links_from_file import get_arr_from_settings_file
from helpers.channel_data.contact_data import get_contact_data
from helpers.channel_data.er_data import get_er_data
from helpers.channel_data.get_advertising_cost import get_advertising_cost
from helpers.channel_data.get_mentions_data import get_mentions_data
from helpers.channel_data.get_reposts_data import get_reposts_data
from helpers.channel_data.get_view_per_post import get_view_per_post
from helpers.channel_data.name_data import get_name_data
from helpers.channel_data.participants_data import get_total_participants_data
from helpers.channel_data.user_cost_data import user_cost_data
from helpers.contact_data_extract import get_contact_data_extract
from helpers.shared.save_screenshot import save_channel_data_screenshots
from helpers.shared.save_txt_file import add_more_line_in_txt_file, save_arr_in_txt_file
from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_data_by_chanel_name(driver, channel_name):
    current_link = f'https://telemetr.me/{channel_name}'
    tg_link = channel_name.replace('@', '')
    columns = get_arr_from_settings_file(file_name='columns')

    driver.get(current_link)

    is_none_arr = []

    total_info_arr_for_i = [''] * len(columns)

    add_more_line_in_txt_file(line=tg_link, folder_path=result_tmp_path,
                              file_name='by_channel_name_ready')

    # название канала
    name = get_name_data(driver=driver, arr=total_info_arr_for_i)
    if name is not None:
        is_none_arr.append(name)

    # описание
    contact_data = get_contact_data(driver=driver, arr=total_info_arr_for_i)
    if contact_data is not None:
        is_none_arr.append(contact_data)

    # ссылка на статистику
    set_in_arr_by_index(arr=total_info_arr_for_i, name='статистика', value=current_link)

    # ссылка на канал
    set_in_arr_by_index(arr=total_info_arr_for_i, name='ссылка', value=f'http://t.me/{tg_link}')

    # подписчики
    participants = get_total_participants_data(driver=driver, arr=total_info_arr_for_i)
    if participants is not None:
        is_none_arr.append(participants)

    # просм на пост
    view_per_post = get_view_per_post(driver=driver, arr=total_info_arr_for_i)
    if view_per_post is not None:
        is_none_arr.append(view_per_post)

    # вовлеченность ER
    er = get_er_data(driver=driver, arr=total_info_arr_for_i)
    if er is not None:
        is_none_arr.append(er)

    # упоминания
    mentions = get_mentions_data(driver=driver, arr=total_info_arr_for_i)
    if mentions is not None:
        is_none_arr.append(mentions)

    # репосты
    reposts = get_reposts_data(driver=driver, arr=total_info_arr_for_i)
    if reposts is not None:
        is_none_arr.append(reposts)

    # стоим подписч
    user_cost = user_cost_data(driver=driver, arr=total_info_arr_for_i)
    if user_cost is not None:
        is_none_arr.append(user_cost)

    # стоимость рекламы
    advertising_cost = get_advertising_cost(driver=driver, arr=total_info_arr_for_i)
    if advertising_cost is not None:
        is_none_arr.append(advertising_cost)


    name_for_save = channel_name.replace('/', '--')

    if len(is_none_arr) == 0:
        set_in_arr_by_index(arr=total_info_arr_for_i, name='итог', value='Всё ok!')
        save_channel_data_screenshots(driver=driver, name=name_for_save,
                                      is_none=False)
        save_arr_in_txt_file(arr=total_info_arr_for_i, folder_path=result_xlsx_path, file_name=f'plus_{name_for_save}')
    else:
        itog = ", ".join(is_none_arr)
        set_in_arr_by_index(arr=total_info_arr_for_i, name='итог', value=itog)
        save_channel_data_screenshots(driver=driver, name=name_for_save,
                                      is_none=True)
        save_arr_in_txt_file(arr=total_info_arr_for_i, folder_path=result_xlsx_path,
                             file_name=f'minus_{name_for_save}')