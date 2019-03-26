import requests
import re

#constant variables:
main_api_url = 'https://api.bincodes.com/bin/'
api_format = 'json/'
api_key = 'yourapikeyfrombincodes' #if you dont have an API code, you can test this program using the bulkbin_binlist.py file instead

#banner and version
print('BulkBin')
print('Version: 1.0 --- API: ' + main_api_url)


while True:

    #put items in a list and split it based on comma_space
    input_string = input("\nEnter BINs or cardnumbers separated by comma_space:\n>>> ")
    card_list = [card[:6] for card in re.split(r',\s*', input_string)]
    print('Removing possible duplicates...')
    no_dup = list(set(card_list))

    try:
        print('Printing BIN data responses...')

        for bin_item in no_dup:
            bin_search_url = main_api_url + api_format + api_key + bin_item
            response = requests.get(bin_search_url).json()
            print('-----------------------------------------')
            print(('BIN:\t\t') + response['bin'])
            print(('Card:\t\t') + response['card'])
            print(('Type:\t\t') + response['type'].title())
            print(('Subtype:\t') + response['level'].title())
            print(('Issuer:\t\t') + response['bank'].title())
            print(('Country:\t') + response['country'].title())
            print('-----------------------------------------')

    except KeyError:
        print('KeyError:\tAPI query limit might be exceeded for today.'
            + '\n\t\tCould not find correct dictionary key from json file')
