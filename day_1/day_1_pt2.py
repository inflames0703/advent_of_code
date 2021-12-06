import pandas as pd

def read_data(filepath, typ):
    my_file = open(filepath)
    data = []
    lines = my_file.readlines()
    # save in the list
    for line in lines: data.append(int(line)) if typ == 'int' else data.append(str(line))
    return data

def create_rolling_windows (data, window_len):
    df = pd.DataFrame({'Measurements': data})
    df = df.rolling(window_len).sum().dropna()
    return df.Measurements.tolist()

def count_measurements_higher_than (data):
    
    cnt_h = 0
    for idx, i in enumerate(data):
        if idx == 0:
            pass
        else:
            if i > data[idx-1]:
                cnt_h += 1
                
    return (cnt_h)

data = read_data ('day_1_input.txt', 'int')
data_rolling = create_rolling_windows (data, 3)
score = count_measurements_higher_than(data_rolling)

print('Number of measurements higher than rolling window: ', score)