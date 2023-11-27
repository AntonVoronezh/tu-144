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


    arr_all = []
    for file_name in files:
        file_path = os.path.join(result_xlsx_path, file_name)

        with open(file_path, encoding='utf-8') as file:
            lines_arr = [row.strip() for row in file]
            arr_all.append(lines_arr)

    from_500_to_5000 = 0
    from_5000_to_10000 = 0
    from_10000_to_15000 = 0
    from_15000_to_20000 = 0
    from_20000 = 0

    for line in arr_all:
        count_prosm = line[4]

        if 500 < int(count_prosm) < 5000:
            from_500_to_5000 = from_500_to_5000 + 1
        if 5000 < int(count_prosm) < 10000:
            from_5000_to_10000 = from_5000_to_10000 + 1
        if 10000 < int(count_prosm) < 15000:
            from_10000_to_15000 = from_10000_to_15000 + 1
        if 15000 < int(count_prosm) < 20000:
            from_15000_to_20000 = from_15000_to_20000 + 1
        if int(count_prosm) > 20000:
            from_20000 = from_20000 + 1

    print(f'Дата сбора - {current_date}')
    print(f'\t')

    print(f'    {title_about}')
    print(f'    {cpm_cost}')
    print(f'    - другие фильтры ###https://t.me/tu_144_parsing1/2838')

    print(f'\t')
    print(f'По текущим фильтрам  было найдено и внесено в таблицу {len(arr_all)} каналов:')
    print(f'- 0,5K-5K 👀 -> {from_500_to_5000}')
    print(f'- 5K-10K 👀 -> {from_5000_to_10000}')
    print(f'- 10K-15K 👀 -> {from_10000_to_15000}')
    print(f'- 15K-20K 👀 -> {from_15000_to_20000}')
    print(f'- более 20K 👀 -> {from_20000}')

    print(f'\t')
    print(f'На каждый канал заполнены поля: название, описание, линк на статистику, линк на канал, просмотры на пост, вовлеченность ER, стоим подписчика, подписчиков, кол упоминаний, кол репостов.')
    print(f'\t')
    print(f'Бонусы:')
    print(f'- поле высчитанная стоимость рекламы на канале')
    print(f'- убраны каналы без контактов')

    print(f'\t')
    sum = len(arr_all)
    print(f'Итого:')
    print(f'Экономия времени для Вас - {sum * 1.5} минут (из расчета проверки вручную 1 канала - 1.5 мин)')
    # print(f'Стоимость отчета для Вас -  {sum}₽  (из расчета 1₽ за канал)')
    print(f'\t')
    # print(f'Разве оно не стоит того❓')

    print(f'\t')

    print('Таблицу можно скачать бесплатно:')
    print(f'\t')
    print('Бесплатно будет таблица со всеми заполненными полями для всех каналов - скачать бесплатно сейчас ### tg://resolve?domain=tu_144_chat_get_file_bot&start=c1700155291592-ds')
    # print(f'\t')
    # print(f'Платно будет таблица со всеми заполненными полями для всех каналов - купить за {sum} ₽ сейчас')

    print(f'\t')

    print(f'Бот для связи###tg://resolve?domain=feedback_tu_144_chat_bot&start=c1700321954832-ds')

    # print(f'➕ Скачать бесплатно УЖЕ отфильтрованный список каналов для самостоятельной проверки + отчет с 10 каналами с заполненными данными ')
    # print(f'\t')
    # print(f'✅ Купить за {sum}₽ отчёт - {sum} каналов')


print_info()
