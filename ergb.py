import argparse
from urllib.request import urlopen, Request
import json
import colorama
from colorama import Back, Style
argparse = argparse.ArgumentParser()
argparse.add_argument("-r", "--rial", action="store_true", help="shows the values in IRR")
argparse.add_argument("-d", "--difference", action="store_true", help="shows the difference point")
args = argparse.parse_args()
colorama.init(wrap=False)
try:
    req = Request(
        url = "https://www.iranintl.com/api/finance?locale=en",
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    response = urlopen(req)
except:
    print(Back.RED + "Network Error!")
    exit(1)
data_json = json.loads(response.read())
lookFor = ["USD", "EUR", "GBP", "Emami Coin"]
names = {"USD": "💵 USD", "EUR": "💶 EUR", "GBP": "💷 GBP", "Emami Coin": "🪙 EGC"}
def convert_to_irr(inp):
    inp = inp.replace('٬', '')
    number = int(inp)
    number = number * 10
    rial_val = "{:,}".format(number)
    return rial_val
def print_value(val):
    if args.rial is True:
        return convert_to_irr(val) + " IRR "
    else: 
        return val + " TMN "
def show_diff(val):
    if args.difference is True:
        if args.rial is True:
            return str(val * 10) + " IRR "
        else: 
            return str(val) + " TMN "
    return ""
def print_data(info):
    if info["move"] == "up":
        print(Back.GREEN + names[info["title"]] + " = " + print_value(info["value"]) + "⬆️ " + show_diff(info["differenceP"]) + Style.RESET_ALL)
    elif info["move"] == "static":
        print(Back.YELLOW + names[info["title"]] + " = " + print_value(info["value"]) + "⏸️ " + show_diff(info["differenceP"]) + Style.RESET_ALL)
    elif info["move"] == "down":
        print(Back.RED + names[info["title"]] + " = " + print_value(info["value"]) + "⬇️ " + show_diff(info["differenceP"]) + Style.RESET_ALL)
for item in data_json["items"]:
    if item["title"] in lookFor:
        print_data(item)
