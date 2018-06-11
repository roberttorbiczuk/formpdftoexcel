import re
import csv
import itertools


data = []
code, number, weight = "----", "", "-----"

with open('wzetka.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split() for line in stripped if line)
    elements = list(itertools.chain(*lines))
    with open('temporary.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for i, el in enumerate(elements):
            if len(data) == 3 or 'Binczarowa' in el:
                if data:
                    print('Kod: ', data.get('code', '----'), 'Numer: ', data.get('number', '-------'), 'Waga: ', data.get('weight', '-----'))
                    writer.writerow((data.get('code', ''), data.get('number', ''), data.get('weight', '')))
                data = {}
                code, number, weight = "----", "", "-----"

            match1 = re.fullmatch('\d+t\d+', el)
            match2 = re.fullmatch('\d+[t1\/]\d{4}', el)
            if match1 or match2:
                code = el[:4]
                data['code'] = code
            if el == 'Numer':
                number = "".join(elements[i+2:i+5])
                if elements[i+2] == 'Wydanie':
                    number = "".join(elements[i+4:i+7])
                if elements[i+3] == 'Wydanie':
                    number = "".join(elements[i+6:i+9])
                if 6 < len(number) < 10:
                    for sign in ['.', '-', "'", ',', '\\', '!']:
                        if sign in number:
                            number = '-------'
                            break
                    data['number'] = number
                else:
                    number = '----'
            for j in ['Netto', 'Wazyl']:
                if j.lower() == el.lower():
                    try:
                        _weight = int(elements[i + 1])
                        if _weight > 10000:
                            weight = _weight
                            data['weight'] = weight
                    except:
                        weight = '----'
                        data['weight'] = weight
        if data:
            print('Kod: ', code, 'Numer: ', number, 'Waga: ', weight)
            writer.writerow((code, number, weight))
