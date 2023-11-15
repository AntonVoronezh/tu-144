from helpers.by_filter.get_links_from_file import get_arr_from_settings_file


def set_in_arr_by_index(arr, name, value):
    lines = get_arr_from_settings_file(file_name='columns')

    index = lines.index(name)
    arr[index] = value