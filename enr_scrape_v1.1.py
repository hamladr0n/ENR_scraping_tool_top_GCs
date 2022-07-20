'''
ENR_Scraping tool

use "auto-py-to-exe" to create the exe


'''

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import urllib
# import string
import requests

headers = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Max-Age': '3600',
  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
  }

enr_list = [
        'https://www.enr.com/California/Toplists/2020-Top-Contractors',
        'https://www.enr.com/Mid-Atlantic/toplists/2019-Top-Contractors',
        'https://www.enr.com/newyork/Toplists/2019-Top-Contractors',
        'https://www.enr.com/midwest/Toplists/2019-Top-Contractors',
        'https://www.enr.com/MountainStates/toplists/2019-Top-Contractors-Colorado-Wyoming',
        'https://www.enr.com/New-England/Toplists/2019-Top-Contractors',
        'https://www.enr.com/northwest/Toplists/2019-Top-Contractors',
        'https://www.enr.com/Southeast/Toplists/2018-Top-Contractors',
        'https://www.enr.com/texas-louisiana/toplists/2019-top-contractors'
        ]

print('Welcome to ENR Scrape \n')

result_list = []

def list_regions():
    for i in enr_list:
        print(i)

def enr_region_choice():
    list_regions()
    url = input("\nPlease choose your region \n by copy and pasting from the selection above \n OR the url of the desired region and year: ")
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    # my_list = soup
    companies = set()
    for name in soup.select("tr > td > strong"):
        companies.add(name.text)


    for x_3 in companies:
      result_list.append(x_3)
  #   print(x_3)

enr_region_choice()

csv_results = []

result_list

def result_loop():
    for i in result_list:
        csv_results.append(i)

with open('enrscrape.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(result_list)
    for x_2 in csv_results[1:]:
        x_2 = x_2.lower()
        # print('"',(x.capitalize()),'" AND')
        writer.writerow(x_2)
