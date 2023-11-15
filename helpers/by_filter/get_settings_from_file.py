import os

from get_path import setting_path
from helpers.shared.get_boolean_value_from_setting import get_boolean_value_from_setting

file_path = os.path.join(setting_path, 'channels_setting.txt')

save_screenshot_enable_setting = get_boolean_value_from_setting(file_path=file_path, setting_name='save_screenshot_enable_setting')
