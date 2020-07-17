from requests import get
from bs4 import BeautifulSoup
from colorama import Fore, init
from prettytable import PrettyTable
import urllib, json, os
init(convert=True)
# Request headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36",
    "Connection": "keep-alive",
    "Host": "iknowwhatyoudownload.com",
    "Referer": "https://iknowwhatyoudownload.com"
} 
