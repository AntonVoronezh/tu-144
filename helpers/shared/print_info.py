import os
from get_path import result_xlsx_path, setting_path
from helpers.shared.get_today import get_today
from helpers.shared.get_value_from_setting import get_value_from_setting


def print_info():
    files = os.listdir(result_xlsx_path)
    current_date = get_today()

    file_path = os.path.join(setting_path, 'channels_setting.txt')
    with open(file_path, encoding='utf-8') as f:
        settings_arr = f.readlines()

    views = f'- просмотров на пост - от AAA до BBB'
    er = f'- ER - от AAA до BBB'
    mentions_week = f'- упоминаний от - AAA'
    title_about = f'- фразы - "AAA"'

    for el in settings_arr:
        line = el.strip()
        line_arr = line.split('#')
        key = line_arr[1].strip()
        value = line_arr[2].strip()

        if key == 'views_post_from':
            views = views.replace('AAA', value)
        if key == 'views_post_to':
            views = views.replace('BBB', value)

        if key == 'er_from':
            er = er.replace('AAA', value)
        if key == 'er_to':
            er = er.replace('BBB', value)

        if key == 'mentions_week_from':
            mentions_week = mentions_week.replace('AAA', value)

        if key == 'title':
            title_about = title_about.replace('AAA', value)

    file_path = os.path.join(setting_path, 'channel_data_setting.txt')
    with open(file_path, encoding='utf-8') as f:
        settings_arr_2 = f.readlines()

    participants_month_plus = f'- рост пдп за месяц -да'
    participants_week_plus = f'- рост пдп за неделю -да'
    cpm_cost = f'- СPM категории - AAA'
    user_cost = f'- цена пдп - AAA'

    for el in settings_arr_2:
        line = el.strip()
        if len(line) > 0:
            line_arr = line.split('#')
            key = line_arr[1].strip()
            value = line_arr[2].strip()

            if key == 'cpm_cost_setting':
                cpm_cost = cpm_cost.replace('AAA', value)
            if key == 'user_cost_setting':
                user_cost = user_cost.replace('AAA', value)

    good_arr = []
    bad_arr = []

    for file_name in files:
        file_path = os.path.join(result_xlsx_path, file_name)

        with open(file_path, encoding='utf-8') as file:
            lines_arr = [row.strip() for row in file]

        if 'plus_' in file_name:
            good_arr.append(lines_arr)

        if 'minus_' in file_name:
            bad_arr.append(lines_arr)


    from_500_to_5000 = 0
    from_5000_to_10000 = 0
    from_10000_to_15000 = 0
    from_15000_to_20000 = 0

    for line in good_arr:
        count_prosm = line[5]

        if 500 < int(count_prosm) < 5000:
            from_500_to_5000 = from_500_to_5000 + 1
        if 5000 < int(count_prosm) < 10000:
            from_5000_to_10000 = from_5000_to_10000 + 1
        if 10000 < int(count_prosm) < 15000:
            from_10000_to_15000 = from_10000_to_15000 + 1
        if 15000 < int(count_prosm) < 20000:
            from_15000_to_20000 = from_15000_to_20000 + 1

    # минус    подписчиков    за    месяц
    aaa = 0
    # минус    подписчиков    за    неделю
    bbb = 0
    # маленькая    стоим    подписч
    ccc = 0
    # нет контактных данных
    ddd = 0
    # мало    упоминаний
    fff = 0
    # мало    репостов
    eee = 0

    for line in bad_arr:
        err_arr = line[0].split(', ')
        for el_2 in err_arr:
            if 'минус подписчиков за месяц' in el_2:
                aaa = aaa + 1
            if 'минус подписчиков за неделю' in el_2:
                bbb = bbb + 1
            if 'маленькая стоим подписч' in el_2:
                ccc = ccc + 1
            if 'нет контактных данных' in el_2:
                ddd = ddd + 1
            if 'мало упоминаний' in el_2:
                fff = fff + 1
            if 'мало репостов' in el_2:
                eee = eee + 1


    print(f'Дата сбора - {current_date}')
    print(f'\t')

    print(f'    {title_about}')
    print(f'    {cpm_cost}')
    print(f'    - другие фильтры')

    print(f'\t')
    print(f'НЕ прошли проверку по текущим фильтрам - {len(bad_arr)} каналов:')
    print(f'   - минус пдп за месяц - {aaa}')
    print(f'   - минус пдп за неделю - {bbb}')
    print(f'   - маленькая стоим пдп - {ccc}')
    print(f'   - нет контактных данных - {ddd}')
    print(f'   - мало упоминаний - {fff}')
    print(f'   - мало репостов - {eee}')


    print(f'\t')
    print(f'Прошли проверку по текущим фильтрам - {len(good_arr)} каналов:')
    print(f'   - от 500 до 5000 просм - {from_500_to_5000}')
    print(f'   - от 5000 до 10000 просм - {from_5000_to_10000}')
    print(f'   - от 10000 до 15000 просм - {from_10000_to_15000}')
    print(f'   - от 15000 до 20000 просм - {from_15000_to_20000}')
    print(f'\t')
    print(f'Вы до сих пор хотите делать ☝️ всё ЭТО вручную????️')

    print(f'\t')

    print(f'Итого:')
    good_count = len(good_arr)
    bad_count = len(bad_arr)
    sum = good_count + bad_count
    print(f'Всего проверено - {sum} каналов')
    eco = sum * 5
    print(f'Экономия времени для Вас - {eco} минут (из расчета проверки вручную 1 канала - 5 мин)')
    rub = (good_count*5) + (bad_count*1)
    print(f'Стоимость отчета получается ({good_count}x5₽) + ({bad_count}x1₽) = {rub}₽ ')
    print(f'\t')
    print(f'Разве оно не стоит того❓')

    print(f'\t')
    print(f'\t')

    print(f'➕ Скачать бесплатно УЖЕ отфильтрованный список каналов для самостоятельной проверки + отчет с 10 каналами с заполненными данными ')
    print(f'\t')
    print(f'✅ Купить за {rub}₽ отчёт - {sum} каналов ({len(good_arr)} + / {len(bad_arr)} - )')


print_info()
