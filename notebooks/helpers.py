import pandas as pd 
import numpy as np 
import itertools
import pickle 
import pandas as pd 
import pyodbc 
import itertools




def findsubsets(s, n):
    return list(itertools.combinations(s, n))

def create_rating_matrix_OS(dataset):  
    """ 
    Input 
        dataset - includes bills and options only. It has to be ordered by bill, option. This is the requirement. 

    Output 
        combined options with ratings. 
    """
    comibined_option = {}
    bill_options = set() 
    bill = dataset.loc[0].bill 
    
    i = 0 
    for index, row in dataset.iterrows():                # O(n)
        if(row.bill == bill): 
            bill_options.add(row.option)
        else:
            if(len(bill_options) > 1):                      # len(bill_options) = O(1)
                subsets = list(findsubsets(bill_options, 2) )     # O(?)
                if(len(bill_options) >= 3): 
                    subsets += list(findsubsets(bill_options, 3))
                for subset in subsets: 
                    comibined_option[subset] = comibined_option.get(subset, 0) + 1 # avverage complexity O(1)
                    
                    i = i + 1 
                    if(i % 100000 == 0):
                        print(f"{i} th iteration for building. Size:", get_size_KB(comibined_option)) 
                        print()

            bill_options.clear() 
            bill_options.add(row.option)
            bill = row.bill

    return comibined_option  


def save_with_pickle(source, path):
    pickle_out = open(path,"wb")
    pickle.dump(source, pickle_out)
    pickle_out.close()

def read_with_pickle(path):  
    pickle_out = open(path,"rb")
    result = pickle.load(pickle_out) 
    pickle_out.close()

    return result

def open_connection():    
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=aydess;'
                        'Database=MIX;'
                        'Trusted_Connection=yes;')
    return conn

def close_connection(conn):
    if conn != None: 
        conn.close() 

def custom_query(query): 
    res = None 
    try: 
        conn = open_connection() 
        res = pd.read_sql(query, conn) 
    except: 
        print('error occured')
    finally: 
        close_connection(conn)
        return res 

def findsubsets(s, n):
    return list(itertools.combinations(s, n))


def create_rating_matrix_OS(dataset):  
    """ 
    Input 
        dataset - includes bills and options only. It has to be ordered by bill, option. This is the requirement. 

    Output 
        combined options with ratings. 
    """
    comibined_option = {}
    bill_options = set() 
    bill = dataset.loc[0].bill 
    
    i = 0 
    for index, row in dataset.iterrows():                # O(n)
        if(row.bill == bill): 
            bill_options.add(row.option)
        else:
            if(len(bill_options) > 1):                      # len(bill_options) = O(1)
                subsets = list(findsubsets(bill_options, 2) )     # O(?)
                if(len(bill_options) >= 3): 
                    subsets += list(findsubsets(bill_options, 3))
                for subset in subsets: 
                    comibined_option[subset] = comibined_option.get(subset, 0) + 1 # avverage complexity O(1)
                    
                    i = i + 1 
                    if(i % 100000 == 0):
                        print(f"{i} th iteration for building. Size:", get_size_KB(comibined_option)) 
                        print()

            bill_options.clear() 
            bill_options.add(row.option)
            bill = row.bill

    return comibined_option  