from selenium.webdriver.common.by import By

from helpers.shared.set_in_arr_by_index import set_in_arr_by_index


def get_contact_data_extract(driver, arr, chanel_name, chanel_link):
    try:
        desc = driver.find_element(By.XPATH, "//div[@class='kt-widget__info']")
        text_content = desc.get_attribute("textContent")

        out_arr = []
        text_content_arr = text_content.split(' ')

        for el in text_content_arr:
            if '@' in el:
                en = set('1234567890qwertyuiopasdfghjklzxcvbnm@_')
                conv_text = lambda mas_in: [''.join([j for j in i if j.lower() in en]) for i in mas_in]
                conv_text_el = conv_text(el)
                out = ''.join(conv_text_el)
                out_arr.append(out.strip())



        # text = ' '.join(out_arr)
        # set_in_arr_by_index(arr=arr, name='контакты', value=text)
        #
        # for el in out_arr:
        #     rus = set('йцукенгшщзхъэждлорпавыфячсмитьбю ')
        #     conv_text = lambda mas_in: [''.join([j for j in i if j.lower() in rus]) for i in mas_in]
        #     conv_text_el = conv_text(chanel_name)
        #     out = ''.join(conv_text_el)
        #     print(33333333333, out)
        #     ff = open('contacts_for_send.txt', 'a')
        #     ff.write(f"{el}|{out}|{chanel_link}\n")
        #     # ff.write(f"{el}|{chanel_name}|{chanel_link}\n")
        #     ff.close()

    except:
        pass

