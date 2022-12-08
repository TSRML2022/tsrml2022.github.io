import pandas

record_path = '~/Downloads/TSRML2022_reviewer_status.csv'

if __name__ == '__main__':
    reviewers = list()
    csv_file = pandas.read_csv(record_path)
    nice_typeset = ''
    reviewer_list = list()
    for item in csv_file.iterrows():
        reviewer_list.append([item[1]['name'], item[1]['num submitted reviews']])
    # print(reviewer_list)
    reviewer_list = sorted(reviewer_list, key=lambda x: 'a' * x[1] + (x[0].rsplit(' ', maxsplit=1)[-1]) + (x[0].rsplit(' ', maxsplit=1)[0]))
    
    last_num = -1
    counter = 0
    for r in reviewer_list:
        if r[1] != last_num:
            last_num = r[1]
            counter = 0
            print('=======')
            print(last_num)
        if counter % 4 == 0:
            print('<tr>')
        print(f' <td>{r[0]}</td>')
        if counter % 4 == 3:
            print('</tr>')
        counter += 1




