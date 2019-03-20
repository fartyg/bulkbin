import requests

#constant variables:
main_api_url = 'https://api.bincodes.com/bin/'
api_format = 'json/'
api_key = 'yourapikeyfrombincodes' #if you dont have an API code, you can test this program using the bulkbin_binlist.py file instead

#banner and version
from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('BulkBin'))
print('Version: 1.0 --- API: ' + main_api_url)


while True:

    #put items in a list and split it based on ', ' (comma_space)
    input_string = input("\nEnter BINs or cardnumbers separated by comma_space:\n>>> ")

    card_list = input_string.split(' , ')
    bin_list = list(map(lambda i:i[0:6],card_list))
    print('Removing possible duplicates...')
    no_dup_bin_list = list(dict.fromkeys(bin_list)) 

    try:
        print('Printing BIN data responses...')

        for bin_item in no_dup_bin_list:
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