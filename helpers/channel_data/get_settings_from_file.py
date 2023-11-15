import os

from get_path import setting_path
from helpers.shared.get_boolean_value_from_setting import get_boolean_value_from_setting
from helpers.shared.get_value_from_setting import get_value_from_setting

file_path = os.path.join(setting_path, 'channel_data_setting.txt')

save_screenshot_enable_setting = get_boolean_value_from_setting(file_path=file_path, setting_name='save_screenshot_enable_setting')
participants_month_plus_enable_setting = get_boolean_value_from_setting(file_path=file_path, setting_name='participants_month_plus_enable_setting')
participants_week_plus_enable_setting = get_boolean_value_from_setting(file_path=file_path, setting_name='participants_week_plus_enable_setting')
mentions_enable_setting = get_boolean_value_from_setting(file_path=file_path, setting_name='mentions_enable_setting')
reposts_enable_setting = get_boolean_value_from_setting(file_path=file_path, setting_name='reposts_enable_setting')
user_cost_enable_setting = get_boolean_value_from_setting(file_path=file_path, setting_name='user_cost_enable_setting')
advertising_count_enable_setting = get_boolean_value_from_setting(file_path=file_path, setting_name='advertising_count_enable_setting')


mentions_count_setting = int(get_value_from_setting(file_path=file_path, setting_name='mentions_count_setting'))
reposts_count_setting = int(get_value_from_setting(file_path=file_path, setting_name='reposts_count_setting'))
cpm_cost_setting = int(get_value_from_setting(file_path=file_path, setting_name='cpm_cost_setting'))
user_cost_setting = int(get_value_from_setting(file_path=file_path, setting_name='user_cost_setting'))
# advertising_count_setting = int(get_value_from_setting(file_path=file_path, setting_name='advertising_count_setting'))