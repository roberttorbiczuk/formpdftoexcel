import xlwt

book = xlwt.Workbook()
sh = book.add_sheet('results')
sh.write(0, 12, 'Nr WZ')
sh.write(0, 13, 'Nr Rejestracyjny')
sh.write(0, 0, 'Ilosc')


with open('temporary.csv', 'r') as out_file:
    for i, line in enumerate(out_file):
        line = line.strip().split(',')
        code, number, weight = line[0], line[1], line[2]
        sh.write(i+1, 12, code)
        sh.write(i+1, 13, number)
        sh.write(i+1, 0, weight)

book.save('results.xls')
