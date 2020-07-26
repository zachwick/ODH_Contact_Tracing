#!/usr/local/bin/python3

'''
This script generates an ODH COVID-19 self reporting URLs for the given ODH case ID and date

Copyright 2020 zach wick <zach@zachwick.com>
Licensed under the GNU GPLv3 or later
'''
import sys
import base64
from urllib.parse import urlencode, quote_plus

BASE_URL = 'https://octs.odh.ohio.gov/symptom-tracker?'
CASE_ID_FIELD = 'p='
DATE_FIELD = '&d='
LANGUAGE_FIELD = '&language='
SUPPORTED_LANGUAGES = ['en','es']

def generate_url():
  if len(sys.argv) < 3:
    print("USAGE: ./generator.py ODH-NNNNN MM/DD/YYYY")
    exit(0)
  encoded_case_id = base64.b64encode(sys.argv[1].encode('utf-8')).decode('ascii')
  encoded_date = base64.b64encode(sys.argv[2].encode('utf-8')).decode('ascii')
  print(BASE_URL + CASE_ID_FIELD + encoded_case_id + DATE_FIELD + encoded_date + LANGUAGE_FIELD + SUPPORTED_LANGUAGES[0])

if __name__ == '__main__':
  generate_url()
