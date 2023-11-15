import os

from get_path import result_path
from helpers.by_filter.get_settings_from_file import save_screenshot_enable_setting as save_screenshot_enable_setting_by_filters
from helpers.channel_data.get_settings_from_file import save_screenshot_enable_setting as save_screenshot_enable_setting_channel_data


def save_by_filters_screenshots(driver, name, is_none):
    if is_none:
        folder_name = 'screenshots_by_filters_NO_data'
    else:
        folder_name = 'screenshots_by_filters_YES_data'

    screenshots_folder_path = os.path.join(result_path, folder_name)

    if save_screenshot_enable_setting_by_filters:
        if not os.path.isdir(screenshots_folder_path):
            os.mkdir(screenshots_folder_path)

        driver.save_screenshot(f'{screenshots_folder_path}/{name}.png')


def save_channel_data_screenshots(driver, name, is_none):
    if is_none:
        folder_name = 'screenshots_channel_data_BAD'
    else:
        folder_name = 'screenshots_channel_data_GOOD'

    screenshots_folder_path = os.path.join(result_path, folder_name)

    if save_screenshot_enable_setting_channel_data:
        if not os.path.isdir(screenshots_folder_path):
            os.mkdir(screenshots_folder_path)

        driver.save_screenshot(f'{screenshots_folder_path}/{name}.png')
