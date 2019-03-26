import requests
import re

#constant variables:
main_api_url = 'https://lookup.binlist.net/'

#banner, API and version
print('BulkBin')
print('Version: 1.0 --- API: ' + main_api_url)

while True:

    #put items in a list and split it based on ', ' (comma_space)
    input_string = input("\nEnter BINs or cardnumbers separated by comma_space:\n>>> ")
    card_list = [card[:6] for card in re.split(r',\s*', input_string)]
    print('Removing possible duplicates...')
    no_dup = list(set(card_list)) 

    try:
        print('Printing BIN data responses...')
        for bin_item in no_dup:
            bin_search_url = main_api_url + bin_item
            response = requests.get(bin_search_url).json()
            print('-----------------------------------------')
            print('BIN:\t\t' + (bin_item))
            print(('Card:\t\t') + response['scheme'].upper())
            print(('Type:\t\t') + response['type'].title())
            print(('Brand:\t\t') + response['brand'].title())
            print(('Issuer:\t\t') + response['bank']['name'].title())
            print(('Country:\t') + response['country']['name'].title())
            print('-----------------------------------------')

    except KeyError:
        print('KeyError:\tAPI query limit might be exceeded.'
            + '\n\t\tCould not find correct dictionary key from json file')
