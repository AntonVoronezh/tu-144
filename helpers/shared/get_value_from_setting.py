def get_value_from_setting(file_path, setting_name):
    with open(file_path, encoding='utf-8') as f:
        settings_arr = f.readlines()

    for el in settings_arr:
        line = el.strip()
        if len(line) > 0:
            line_arr = line.split('#')
            key = line_arr[1].strip()
            value = line_arr[2].strip()

            if setting_name in key:
                return int(value)
