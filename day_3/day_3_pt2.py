import pandas as pd

def read_data(filepath, typ):
    my_file = open(filepath)
    data = []
    lines = my_file.readlines()
    # save in the list
    for line in lines: data.append(int(line)) if typ == 'int' else data.append(str(line))
    return data

def convert_data_to_df(data):
    list_of_lists = []
    # get the number of bits
    bits = len(data[0])-1
 
    
    for x in data: list_of_lists.append([int(x[bitidx]) for bitidx in range(bits)])
    df = pd.DataFrame(list_of_lists)
    return df

    

def calculate_oxygen_generator_rating(data):

    for idx in data.columns:
        if data[idx].mean() == 0.5:
            data = data[data[idx] == 1]   
        
        data = data[data[idx] == round(data[idx].mean())]
        
        if len(data) == 1:
            break
    return list(data.iloc[0])

def calculate_co2_scrubber_rating (data):

    for idx in data.columns:
        if 1-data[idx].mean() == 0.5:
            data = data[data[idx] == 0]
        else: 
            data = data[data[idx] == round(1-data[idx].mean())]
        if len(data) == 1:
            break
    return list(data.iloc[0])

def calculate_life_support_rating(data):
    ox_g_rating = calculate_oxygen_generator_rating(data)
    co2_s_rating = calculate_co2_scrubber_rating (data)
        
    ox_g_rating_dec = 0
    co2_s_rating_dec = 0
    
    n = 0
    
    for idx, i in reversed(list(enumerate(ox_g_rating))):
        ox_g_rating_dec += i*2**n
        n+=1

    
    n = 0
    for idx, i in reversed(list(enumerate(co2_s_rating))):
        co2_s_rating_dec += i*2**n
        n+=1
    
    return ox_g_rating_dec * co2_s_rating_dec
    
data = read_data('day_3_input.txt', 'str')
data = convert_data_to_df(data)
score = calculate_life_support_rating(data)
print('Life support rating of the submarine is: ',score)