#!/usr/bin/python
import sys
import json
import urllib
import argparse
import socket

currencies = {
        "USD": "US dollar",
        "JPY": "Japanese yen",
        "BGN": "Bulgarian lev",
        "CZK": "Czech koruna",
        "DKK": "Danish krone",
        "GBP": "Pound sterling",
        "HUF": "Hungarian forint",
        "PLN": "Polish zloty",
        "RON": "Romanian leu",
        "SEK": "Swedish krona",
        "CHF": "Swiss franc",
        "ISK": "Icelandic krona",
        "NOK": "Norwegian krone",
        "HRK": "Croatian kuna",
        "RUB": "Russian rouble",
        "TRY": "Turkish lira",
        "AUD": "Australian dollar",
        "BRL": "Brazilian real",
        "CAD": "Canadian dollar",
        "CNY": "Chinese yuan renminbi",
        "HKD": "Hong Kong dollar",
        "IDR": "Indonesian rupiah",
        "ILS": "Israeli shekel",
        "INR": "Indian rupee",
        "KRW": "South Korean won",
        "MXN": "Mexican peso",
        "MYR": "Malaysian ringgit",
        "NZD": "New Zealand dollar",
        "PHP": "Philippine piso",
        "SGD": "Singapore dollar",
        "THB": "Thai baht",
        "ZAR": "South African rand"
    }



def main(args, currencies):
    shrt_cur = list(currencies.keys())
    if len(args) == 3:
        if sys.argv[1] in shrt_cur and sys.argv[3] in shrt_cur:
            BASE = sys.argv[1]
            AMT = sys.argv[2]
            TO = sys.argv[3]
            try:
                response = urllib.urlopen('https://api.exchangeratesapi.io/latest?base=%s' % (BASE))
                print 'you are online... geting online results'                 
                html = response.read().decode("utf-8")
                my_dict = json.loads(html)
                result = my_dict['rates'][TO] 
                result = round(result, 2)
                calc = int(AMT) * result
                print 'from:','1 ' + BASE
                print 'to:', AMT, TO
                print 'rate:', calc
                print 'downloading and storing latest results'
                for i in shrt_cur:
                    with open(i + ".dict", "w") as outf:
                        url = urllib.urlopen('https://api.exchangeratesapi.io/latest?base=%s' % i)
                        html = url.read().decode("utf-8")
                        cdict = json.loads(html)
                        outf.write(json.dumps(cdict))
            except IOError:
                print 'you are offline...getting latest offline results'
                if BASE in shrt_cur:
                    with open(BASE + '.dict', 'r') as f:
                        results = f.readlines()
                        for result in results:
                            user_dict = json.loads(result)
                        dict_results = user_dict['rates'][TO]
                        dict_results = round(dict_results, 2)
                        calc = int(AMT) * dict_results
                        print 'from:','1 ' + BASE
                        print 'to:', AMT, TO
                        print 'rate:', calc
                else:
                    print 'oops...something went wrong...'
        else:
            print 'currency not in list, Usage: python2 curry-conver-1.0.0.py list -- will list all available currencies'

    elif len(args) == 1 and sys.argv[1] == 'list':
        for key, val in currencies.items():
            print key + ' : ' + val
    else:
        print 'Usage: python2 curry-conver-1.0.0.py from amount to'
        print 'Example: python2 curry-conver-1.0.0.py ZAR 4 USD'
        print 'Usage: python2 curry-conver-1.0.0.py list -- will list all available currencies'
        sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:], currencies)
