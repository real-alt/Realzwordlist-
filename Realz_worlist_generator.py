#!/usr/bin/env python3

import itertools
import random
import string
from datetime import datetime

# Easy password list
EASY_PASSWORDS = [
    'password', '123456', '12345678', 'qwerty', 'abc123', 'football',
    'monkey', 'letmein', 'shadow', 'master', 'welcome', 'login',
    'admin', '123123', 'iloveyou', 'starwars', 'dragon', 'passw0rd'
]

# Keyboard walk patterns
KEYBOARD_PATTERNS = ['qwerty', 'asdfgh', 'zxcvbn', '123456', '1q2w3e', 'qazwsx']

# Clothing and shoe brands
BRANDS = ['nike', 'adidas', 'puma', 'reebok', 'vans', 'converse', 'underarmour', 'jordans', 'fila', 'gucci', 'lv']

# Colors
COLORS = ['red', 'blue', 'green', 'black', 'white', 'purple', 'yellow', 'orange', 'pink', 'gray']

def get_inputs():
    print("Enter comma-separated values or press Enter to skip.")
    victim_name = input("Victim's full name: ").lower().split(',')
    mom_name = input("Mom's name: ").lower().split(',')
    dad_name = input("Dad's name: ").lower().split(',')
    kids_names = input("Kids' names: ").lower().split(',')
    birthdays = input("Birthdays (ddmmyyyy or mmddyyyy): ").split(',')
    hobbies = input("Hobbies: ").lower().split(',')
    fav_sports = input("Favorite sports teams: ").lower().split(',')
    fav_colors = COLORS + input("Favorite colors: ").lower().split(',')
    fav_brands = BRANDS + input("Clothing/Shoe brands: ").lower().split(',')
    cars = input("Cars owned or liked: ").lower().split(',')
    phone_numbers = input("Phone numbers (comma-separated): ").split(',')
    area_codes = input("Area codes to generate random phone numbers from: ").split(',')

    return {
        'names': victim_name + mom_name + dad_name + kids_names,
        'birthdays': birthdays,
        'hobbies': hobbies,
        'sports': fav_sports,
        'colors': fav_colors,
        'brands': fav_brands,
        'cars': cars,
        'phones': phone_numbers,
        'area_codes': area_codes
    }

def leetspeak(word):
    table = str.maketrans('aeiost', '43105+')
    return word.translate(table)

def insert_symbols(word, symbols="!@#$%&*"):
    pos = random.randint(0, len(word))
    return word[:pos] + random.choice(symbols) + word[pos:]

def generate_combos(data, leet=False, symbols=False, reversed_names=False, initials=False):
    base = data['names'] + data['birthdays'] + data['hobbies'] + data['sports'] + data['colors'] + data['brands'] + data['cars']
    combos = set()

    for word in base:
        if not word: continue
        combos.add(word)
        combos.add(word + '123')
        combos.add(word + '1234')
        combos.add(word + '!')
        combos.add(word.title())
        if leet:
            combos.add(leetspeak(word))
        if symbols:
            combos.add(insert_symbols(word))
        if reversed_names:
            combos.add(word[::-1])
        if initials:
            combos.add(''.join([w[0] for w in word.split() if w]))

    for phone in data['phones']:
        combos.add(phone)
        for word in base:
            combos.add(phone + word)
            combos.add(word + phone)

    for area in data['area_codes']:
        for _ in range(5):
            rand_number = area + ''.join(random.choices(string.digits, k=7))
            combos.add(rand_number)
            for word in base:
                combos.add(rand_number + word)

    combos.update(EASY_PASSWORDS)
    combos.update(KEYBOARD_PATTERNS)

    return list(combos)

def generate_random_passwords(count, min_len=8, max_len=16):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return [''.join(random.choices(all_chars, k=random.randint(min_len, max_len))) for _ in range(count)]

def generate_numeric_range(max_value=100000000):
    return [str(i).zfill(10) for i in range(max_value)]

def main():
    data = get_inputs()
    leet = input("Enable leetspeak? (y/n): ").lower() == 'y'
    symbols = input("Insert symbols randomly? (y/n): ").lower() == 'y'
    reversed_names = input("Include reversed words? (y/n): ").lower() == 'y'
    initials = input("Include initials? (y/n): ").lower() == 'y'
    random_pass = input("Add random passwords with mixed chars? (y/n): ").lower() == 'y'
    rand_count = int(input("How many random passwords? (e.g. 50): ")) if random_pass else 0
    numeric_gen = input("Add numeric list (0 to 100,000,000)? (y/n): ").lower() == 'y'
    limit = int(input("Max wordlist size (0 = no limit): "))

    print("\nGenerating wordlist...")
    wordlist = generate_combos(data, leet, symbols, reversed_names, initials)

    if random_pass:
        wordlist += generate_random_passwords(rand_count, 1, 20)

    if numeric_gen:
        print("This might take a while... adding numeric range up to 100,000,000")
        wordlist += generate_numeric_range(100000)

    wordlist = list(set(wordlist))
    if limit > 0:
        wordlist = wordlist[:limit]

    print(f"Generated {len(wordlist)} passwords. Saving to realzwordlist.txt")
    with open("realzwordlist.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print("Done. You can now use realzwordlist.txt with your tools.")

if __name__ == "__main__":
    main()
