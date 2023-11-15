def get_boolean_value_from_setting(file_path, setting_name):
    with open(file_path, encoding='utf-8') as f:
        settings_arr = f.readlines()

    for el in settings_arr:
        line = el.strip()
        line_arr = line.split('#')
        key = line_arr[1].strip()
        value = line_arr[2].strip()

        if setting_name in key:
            if 'true' in value.lower():
                return True
            elif 'false' in value.lower():
                return False
            else:
                return False
