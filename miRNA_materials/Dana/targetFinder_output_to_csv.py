import pandas as pd

if __name__ == '__main__':
    import pandas as pd

    f = open('combined.miRNA.target.report', 'r')
    lines = f.readlines()
    f.close()

    d = {'query': [], 'target': [], 'pacid': [], 'polypeptide': [], 'locus': [], 'ID': [], 'range': [], 'strand': [],
         'target_sequence': [], 'query_sequence': []}
    df = pd.DataFrame(data=d)

    for line in lines:
        words = line.split()
        if words and line[0] in ['q', 't', 'N']:
            if words[0] == 'No':
                df.loc[len(df.index)] = [words[3][:-1]] + [''] * 9
            elif words[0] == 'target':
                df.iat[len(df.index) - 1, 8] = words[2]
            elif words[0] == 'query':
                df.iat[len(df.index) - 1, 9] = words[2]
            else:
                current_query = words[0][6:-1]
                data = {'query': words[0][6:-1], 'target': words[1][7:],
                        'pacid': words[2][6:], 'polypeptide': words[3][12:],
                        'locus': words[4][6:], 'ID': words[5][3:-1],
                        'score': words[6][6:-1], 'range': words[7][6:-1],
                        'strand': words[8][7:], 'target_sequence': '', 'query_sequence': ''}
                df.loc[len(df.index)] = data

    df.to_csv('combined.miRNA.target.report.csv', index=False)
