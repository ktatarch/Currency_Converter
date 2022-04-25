import json
import requests

cache = {}

def get_rate(currency, change, amount):
    if change in cache.keys():
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        get_data(currency, change)
    total = "{:.2f}".format(amount * cache[change])
    print(f"You received {total} {change.upper()}.")

def get_data(currency, change):
    global cache

    r = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
    data = json.loads(r.text)
    cache[change] = data[change]["rate"]

def validate(currency):
    if currency != "usd":
        get_data(currency, "usd")
    if currency != "eur":
        get_data(currency, "eur")

def main():
    currency = (input()).lower()
    validate(currency)

    while True:
        change = (input()).lower()
        if not change:
            break
        else:
            amount = int(input())
            if not amount:
                break
            else:
                print("Checking the cache...")
                get_rate(currency, change, amount)

main()
