def make_name_from_link(link):
    spl = link.split('?')[1]
    arr = spl.split('&')
    arr_join = ', '.join(arr)

    return arr_join
