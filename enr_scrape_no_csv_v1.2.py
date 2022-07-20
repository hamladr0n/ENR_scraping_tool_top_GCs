'''
ENR_Scraping tool

use "auto-py-to-exe" to create the exe


'''
import sys
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import string
import csv

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
    my_list = soup
    companies = set()
    for name in soup.select("tr > td > strong"):
        companies.add(name.text)

    #         companies
    #         print(companies)
    #         print(my_list)
    #         clear()
    for x in companies:
        result_list.append(x)
#             print(x)

enr_region_choice()

# ATTEMPT TO PUT COMPANY IN QOTES
for x in result_list:
    x = x.lower()
    # print('"',(x.capitalize()),'" AND')
    print(x.capitalize())

# Prints list like: ['FERROVIAL AGROMAN US CORP.','

csv_results = []

result_list

def result_loop():
    
    for i in result_list:
        csv_results.append(i)

#run this as: python program.py output.txt

filename = csv_results[1:]
# orig_sys = sys.stdout
with open(filename,'w') as csv_results[:]:
    sys.stdout = out
    #your code here

# enr_txt = open('enrscrape2.txt','w')

# enr_txt.write(str(result_list))
# enr_txt.close()

# enr_txt_2 = open('enrscrape_txt_2.txt','w')
# with enr_txt_2 as f:
#     enr_txt_2.write(str(result_list))
#     print("test111")


# with open('enrscrape3.txt', 'w') as f:
#     # writer = f.write(f)
#     # write(result_list)
#     # sys.stdout = out
#     for x in csv_results[1:]:
#         x = x.lower()
#         # print('"',(x.capitalize()),'" AND')
#         writer.writerow(x)



# with open('enrscrape.txt','w') as f: 
#     writer = csv.writer(csv_file)
#     writer.writerow(result_list)
#     for x in csv_results[1:]:
#         x = x.lower()
#         # print('"',(x.capitalize()),'" AND')
#         writer.writerow(x)
#     for line in csv_results[:]: 
#         print(line) 




# with open('enrscrape.csv', 'w') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(result_list)
#         for x in csv_results[1:]:
#             x = x.lower()
#             # print('"',(x.capitalize()),'" AND')
#             writer.writerow(x)





# with open('output.csv', 'w') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(enr_region_choice)
#         for row in rows[1:]:
#             data = [th.text.rstrip() for th in row.find_all('td')]
#             writer.writerow(data)