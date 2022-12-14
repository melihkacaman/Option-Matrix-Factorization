import pandas as pd 
import numpy as np 
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