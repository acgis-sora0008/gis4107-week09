# ------------------------------------------------------------------------------
# Name:        DictListUtils.py
#
# Purpose:     Various utility functions for working with dictionaries and lists
#
# Author:      David Viljoen
#
# Created:     18/12/2021
# Last update: 31/10/2022
# ------------------------------------------------------------------------------

def get_missing_keys(dict_ref, dict_to_compare):
    """Returns a list of missing keys.
       dict_to_compare is the dict that may have missing keys
       dict_ref is the dict to compare it to
       Example:  dict_ref = {1:1, 2:2, 3:3}, dict_to_compare = {2:2}
                 returns [1, 3]
    """

    missing_keys = []

    for key in dict_ref:
        if key not in dict_to_compare:
            missing_keys.append(key)
    
    return missing_keys

def get_missing_keys_with_count(dict_ref, dict_to_compare):
    """Returns a count and a list of missing keys.
       dict_to_compare is the dict that may have missing keys
       dict_ref is the dict to compare it to
       Example:  dict_ref = {1:1, 2:2, 3:3}, dict_to_compare = {2:2}
                 returns (2, [1, 3])
    """
    missing_keys = []

    for key in dict_ref:
        if key not in dict_to_compare:
            missing_keys.append(key)
    count_missing_keys = len(missing_keys)

    return ((count_missing_keys, missing_keys))

def get_unique(in_list):
    """Retuns a list of unique values from in_list
    Example:  in_list = [1, 2, 2, 3] returns [1, 2, 3]
    """
    unique_list = []

    for value in in_list:
        if value not in unique_list:
            unique_list.append(value)

    return unique_list

def flatten_list(in_list):
    """ This function will return a list that contains the items of
    in_list that are not lists or tuples as well as the items
    of the list(s) or tuples(s).  The lists and tuples of in_list 
    will be removed.  
    For example, if in_list = [1, (2,3), [4,5]], 
    the returned list would be [1, 2, 3, 4, 5]
    """
    flatten_list = []

    for item in in_list:
        if type(item) == list:
            for items in item:
                flatten_list.append(items)
        elif type(item) == tuple:
            for items in item:
                flatten_list.append(items)
        else:
            flatten_list.append(item)

    return flatten_list