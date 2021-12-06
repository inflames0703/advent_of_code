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

def calculate_power_consumption (data):
    
    bits  = len(data.columns)
    
    gamma = [0 for i in range(bits)]
    epsilon = [0 for i in range(bits)]
    
    gamma_rate = 0
    epsilon_rate = 0
    
    for idx, i in enumerate(gamma): gamma[idx] = 1 if data[idx].mean() >= 0.5 else 0 
    for idx, i in enumerate(epsilon): epsilon[idx] = 1 if data[idx].mean() < 0.5 else 0
    


    # this should be written as special function to calculate decimal from binary number
    n = 0
    
    for idx, i in reversed(list(enumerate(gamma))):
        gamma_rate += i*2**n
        n+=1

    
    n = 0
    for idx, i in reversed(list(enumerate(epsilon))):
        epsilon_rate += i*2**n
        n+=1
    
    
    return gamma_rate * epsilon_rate
            
def calculate_power_consumption (data):
    
    bits  = len(data.columns)
    
    gamma = [0 for i in range(bits)]
    epsilon = [0 for i in range(bits)]
    
    gamma_rate = 0
    epsilon_rate = 0
    
    for idx, i in enumerate(gamma): gamma[idx] = 1 if data[idx].mean() >= 0.5 else 0 
    for idx, i in enumerate(epsilon): epsilon[idx] = 1 if data[idx].mean() < 0.5 else 0
    


    # this should be written as special function to calculate decimal from binary number
    n = 0
    
    for idx, i in reversed(list(enumerate(gamma))):
        gamma_rate += i*2**n
        n+=1

    
    n = 0
    for idx, i in reversed(list(enumerate(epsilon))):
        epsilon_rate += i*2**n
        n+=1
    
    
    return gamma_rate * epsilon_rate

data = read_data('day_3_input.txt', 'str')
data = convert_data_to_df(data)
score = calculate_power_consumption(data)
print('Power consumption of submarine is: ', score)