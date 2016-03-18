import shodan
import sys
from sys import exit
import os
#import argparse

try:
    import shodan
except:
    print ('You need the Shodan Python module')
    sys.exit()

## Connect to SHODAN
SHODAN_API_KEY = "YOU_API_KEY_GOES_HERE"
shodan_object = shodan.Shodan(SHODAN_API_KEY)

## Prints title, version, contact info, etc.
def banner():
    title = "Shodan_Sarch.py"
    version = "Version 1.0"
    contact = "notify.mynews@gmail.com"
    print ("-" * 45)
    print (title.center(45))
    print (version.center(45))
    print (contact.center(45))
    print ("-" * 45)

# Input validation
if len(sys.argv) == 1:
    print ('Usage: %s <search query>' % sys.argv[0])
    sys.exit(1)

## Wrap the request in a try/ except block to catch errors
try:
    ## Show the banner
    banner() 

    # Generate a query string out of the command-line arguments
    query = ' '.join(sys.argv[1:])

    ## Setup Shodan the api and perform the search 
    #results = shodan_object.search('apache')
    results = shodan_object.search(query)

    # Show the results. Loop through the matches and print each IP
    print ('Results found:  %s' % results['total'])
    for result in results['matches']:
        print ('IP: %s'  % result['ip_str'])
        print (result['data'])
        print ('')
except (shodan.APIError, e):
    print ('Error: %s ' % e)
#except Exception as e:
#        print ('Error: %s' % e)
#        sys.exit(1)
