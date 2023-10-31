#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
# Last update: 31/10/2022
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_pop

# Key = country name and 
# Value = population as a number (i.e. not text containing commas)
#
country_to_pop = dict()


def get_country_count():
    """Return the number of countries in country_pop.  
    NOTE:  Assume data (country_pop) will always have a header"""
    country_count = country_pop.splitlines()
    total_count = len(country_count)-1
    return total_count
    
    # print(total_count)
    
# get_country_count()    
    

def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    original_number = int(number_text.replace(",", ""))
    return original_number 
    
    
# conv_num_with_commas("1,000")    
    


def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    country_count = country_pop.splitlines()
    top_five_list = []
    # print(country_count[1:6]) 
    for top_five in country_count[1:6]:
        # xyz = []
        # top_five = country_count[2]
        # print(top_five)
        top_five_split = top_five.split("\t")
        top_five_list.append(top_five_split[1])
    return top_five_list
    
# get_top_five_countries()    

def set_country_to_pop():
    """Sets the global country_to_pop dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
#     """


# def get_population(country_name):
#     """Given the name of the country, return the population as of 01Jul2017
#        from country_to_pop.  If the country_to_pop is
#        empty (i.e. no keys or values), then run set_country_to_pop
#        to initialize it."""


# def get_continents():
#     """Return the list of continents"""


# def get_continent_populations():
#     """Returns a dict where the key is the name of the continent and
#        the value is the total population of all countries on that continent"""

