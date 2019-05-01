'''This script prints BIN info in bulk'''
import re
import requests

#constant variables:
MAIN_API_URL = 'https://api.bincodes.com/bin/'
API_FORMAT = 'json/'
API_KEY = 'ec08fff1b4461e540285b25029cdd2b5/'

print('BulkBin')
print('Version: 1.0 --- API: ' + MAIN_API_URL)


while True:

    #put items in a list and split it based on ', ' (comma_space or just comma)

    INPUT_STRING = input(
        "\nEnter BINs or cardnumbers separated by comma_space:\n>>> ")

    CARD_LIST = [card[:6] for card in re.split(r',\s*', INPUT_STRING)]

    #card_list = input_string.split(', ')
    #bin_list = list(map(lambda i:i[0:6],card_list))
    #This was my previous way of doing it


    print('Removing possible duplicates...')
    NO_DUPS = list(set(CARD_LIST))
    #prefered way of removing duplicates according to Reddit

    try:
        print('Printing BIN data responses...')
        for BIN_ITEM in NO_DUPS:
            bin_search_url = MAIN_API_URL + API_FORMAT + API_KEY + BIN_ITEM
            response = requests.get(bin_search_url).json()
            print('-----------------------------------------')
            print(('BIN:\t\t') + response['bin'])
            print(('Card:\t\t') + response['card'])
            print(('Type:\t\t') + response['type'].title())
            print(('Subtype:\t') + response['level'].title())
            print(('Issuer:\t\t') + response['bank'].title())
            print(('Country:\t') + response['country'].title())
            print('-----------------------------------------')

    except KeyError: #this needs to be improved
        print('KeyError:\tAPI query limit might be exceeded for today.' +
              '\n\t\tCould not find correct dictionary key from json file' +
              '\n\t\tException handling in this program is not good yet')
