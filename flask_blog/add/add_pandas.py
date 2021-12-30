import pandas as pd

def make_sheet():
    index = ['2019-12-29', '2019-12-30', '2019-12-31', '2020-01-01']
    columns = ['最高気温', '最低気温', '天候']
    data = [[12.4, 5.1, '曇り'], [15.2, 12.0, '曇り'], [7.9, 7.2, '晴れ'], [9.8, 1.6, '晴れ']]
    df = pd.DataFrame(data=data, columns=columns, index=index)
    return df