import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=canon+m50&_sacat=0"




def get_data(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def parse(soup):
    productslist = []
    results = soup.find_all("div", {"class" : "s-item__info clearfix"})
    for item in results:
        products = {
            'title': item.find('div', {'class': 's-item__title'}).text,
            'soldprice': item.find('span', {'class': 's-item__price'}),
            'bids': item.find("span", {'class': 's-item__bids'}),
            'link': item.find("a", {"class":"s-item__link"}),
        }
        productslist.append(products)
    return productslist

def output(productslist):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv("output.csv", index=False)
    print("saved to csv")
    return

soup = get_data(URL)
productslist = parse(soup)
output(productslist)