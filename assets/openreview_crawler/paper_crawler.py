import pandas

record_path = '~/Downloads/TSRML2022_paper_status.csv'

if __name__ == '__main__':
    accepted_papers = list()
    csv_file = pandas.read_csv(record_path)
    accepted_papers = csv_file[csv_file['decision'] == 'Accept']
    nice_typeset = ''
    for item in accepted_papers.iterrows():
        nice_typeset += f"""
        <li><b>{item[1]['title']}</b> <br /> {item[1]['authors'].replace('|', '; ')}</li>
        """
    print(nice_typeset)




