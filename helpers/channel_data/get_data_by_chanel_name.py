from get_path import result_tmp_path
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
from helpers.shared.save_screenshot import save_channel_data_screenshots
from helpers.shared.save_txt_file import add_more_line_in_txt_file
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
    if not name:
        is_none_arr.append(True)

    # описание
    contact_data = get_contact_data(driver=driver, arr=total_info_arr_for_i)
    if not contact_data:
        is_none_arr.append(True)

    # ссылка на статистику
    set_in_arr_by_index(arr=total_info_arr_for_i, name='статистика', value=current_link)

    # ссылка на канал
    set_in_arr_by_index(arr=total_info_arr_for_i, name='ссылка', value=f'http://t.me/{tg_link}')

    # подписчики
    participants = get_total_participants_data(driver=driver, arr=total_info_arr_for_i)
    if not participants:
        is_none_arr.append(True)

    # просм на пост
    view_per_post = get_view_per_post(driver=driver, arr=total_info_arr_for_i)
    if not view_per_post:
        is_none_arr.append(True)

    # вовлеченность ER
    er = get_er_data(driver=driver, arr=total_info_arr_for_i)
    if not er:
        is_none_arr.append(True)

    # упоминания
    mentions = get_mentions_data(driver=driver, arr=total_info_arr_for_i)
    if not mentions:
        is_none_arr.append(True)

    # репосты
    reposts = get_reposts_data(driver=driver, arr=total_info_arr_for_i)
    if not reposts:
        is_none_arr.append(True)

    # стоим подписч
    user_cost = user_cost_data(driver=driver, arr=total_info_arr_for_i)
    if not user_cost:
        is_none_arr.append(True)

    # стоимость рекламы
    advertising_cost = get_advertising_cost(driver=driver, arr=total_info_arr_for_i)
    if not advertising_cost:
        is_none_arr.append(True)

    if len(is_none_arr) == 0:
        save_channel_data_screenshots(driver=driver, name=channel_name.replace('/', '--'),
                                      is_none=False)
        add_more_line_in_txt_file(line=total_info_arr_for_i, folder_path=result_tmp_path,
                                  file_name='total_info_arr_for_i')
    else:
        save_channel_data_screenshots(driver=driver, name=channel_name.replace('/', '--'),
                                      is_none=True)