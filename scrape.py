from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import chain, zip_longest

with open('html\\page1.html', 'r')as html_file:
    html_doc = html_file.read()

soup = BeautifulSoup(html_doc, "lxml")

def read_stock_table(soup_obj, table_class, header_class):
    headers = [i.text for i in soup_obj.find_all('tr', class_=header_class)[1]][1:]

    _t_c1 = table_class[0]
    _t_c2 = table_class[1]

    _t_1 = soup_obj.find_all('tr', class_=_t_c1['name'])[_t_c1['index']:]
    _t_2 = soup_obj.find_all('tr', class_=_t_c2['name'])[_t_c2['index']:]

    _iter_t = [x for x in chain.from_iterable((zip_longest(_t_1, _t_2))) if x]

    rows = []

    for i, table in enumerate(_iter_t):
            strings = [string for string in table.stripped_strings]
            del strings[3], strings[4]
            _obj = OrderedDict(zip(headers, strings))
            _obj['row'] = i
            rows.append(dict(_obj))

    return rows

data = read_stock_table(soup,
                        [{'name': 'GKCQ-U1BIM','index': 6},
                         {'name': 'GKCQ-U1BJM','index': 5}],
                        'GKCQ-U1BCO')

print(len(data))