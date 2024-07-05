import copy
import numpy as np

def mean_dict(dictionaries):
    result = {} 
    #copy.deepcopy(dictionaries[0])
    for key in dictionaries[0].keys():
        result[key] = np.mean([dic[key] for dic in dictionaries], axis=0)
    return result