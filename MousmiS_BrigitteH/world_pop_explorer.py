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

country_to_pop = dict()

def get_country_count():
    """Return the number of countries in country_pop.  
    NOTE:  Assume data (country_pop) will always have a header"""
    
    country_count = country_pop.splitlines()
    
    total_count = len(country_count)-1
    
    return total_count
     
def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    
    original_number = int(number_text.replace(",", ""))
    
    return original_number 


def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    
    country_count = country_pop.splitlines()
    
    top_five_list = []

    for country in country_count[1:6]:
        top_five_split = country.split("\t")
        top_five_list.append(top_five_split[1])
    
    return top_five_list

def set_country_to_pop():
    """Sets the global country_to_pop dictionary where key is country name
        and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
   """
    dataset_count = country_pop.splitlines()

    country_list = []
    pop_list= []
    change_list = []
    
    for data in dataset_count[1:]:
        data_split = data.split("\t")
        country_list.append(data_split[1])
        pop_list.append(data_split[5])
        change_list.append(data_split[6])

    pop_list_integer = []

    for pop in pop_list:
        pop_integer = int(pop.replace(",", ""))
        pop_list_integer.append(pop_integer)
    
    change_list_float = []

    for change in change_list:
        change1 = change.replace("%", "")
        change = float(change1.lstrip('-'))
        change_list_float.append(change)

    population_change = tuple(zip(pop_list_integer,change_list_float))

    global country_to_pop

    country_to_pop = dict(zip(country_list, population_change))

def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
    from country_to_pop.  If the country_to_pop is
    empty (i.e. no keys or values), then run set_country_to_pop
    to initialize it."""

    dataset_count = country_pop.splitlines()

    for data in dataset_count[1:]:
        data_split = data.split("\t")
        if country_name == data_split[1]:
            population = int(data_split[5].replace(",", ""))
            return population
    
def get_continents():
    """Return the list of continents"""
   
    dataset_count = country_pop.splitlines()

    continent_list = []

    for data in dataset_count[1:]:
        data_split = data.split("\t")
        continent_list.append(data_split[2])

    unique_continent_list = []
    
    for continent in continent_list:
        if continent not in unique_continent_list:
            unique_continent_list.append(continent)
    
    unique_continent_list.sort()
    
    return unique_continent_list
            

def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
    the value is the total population of all countries on that continent"""

    dataset_count = country_pop.splitlines()

    continent_list = []

    for data in dataset_count[1:]:
        data_split = data.split("\t")
        continent_list.append(data_split[2])
    
    unique_continent_list = []

    for continent in continent_list:
        if continent not in unique_continent_list:
            unique_continent_list.append(continent)
    
    continent_to_population = {}

    for continent in unique_continent_list:
        pop_counter = 0
        for data in dataset_count[1:]:
            data_split = data.split("\t")
            if continent == data_split[2]:
                population = int(data_split[5].replace(",", ""))
                pop_counter= pop_counter + population
        continent_to_population[continent] = pop_counter
    
    return continent_to_population

