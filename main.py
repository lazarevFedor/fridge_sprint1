import datetime
from decimal import Decimal


DATE_FORMAT = '%Y-%m-%d'


goods = {}


def add(items, title, amount, expiration_date=None):
    grocery_items = dict.get(items, title, [])
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT)
    grocery_items.append({'amount': amount, 'expiration_date': expiration_date})
    items[title] = grocery_items


def add_by_note(items, note):
    note = str.split(note, ' ')


    title_by_note = "".join(note[:-2])

    amount_by_note = Decimal(note[-2])

    expiration_date_by_note = note[-1]
    if expiration_date_by_note != '':
        expiration_date_by_note = datetime.datetime.strptime(note[-1], DATE_FORMAT)
    else:
        expiration_date_by_note = None

    grocery_items = dict.get(items, title_by_note, [])
    grocery_items.append({'amount': amount_by_note, 'expiration_date': expiration_date_by_note})
    items[title_by_note] = grocery_items


def find(items, needle):
    needle = str.lower(needle)
    list_of_grocery_items = list(items.keys())
    list_with_needle = []
    for item in list_of_grocery_items:
        if needle in item.lower():
            list_with_needle.append(item)
    return list_with_needle


def amount(items, needle):
    needle = str.lower(needle)
    list_with_needle = list(items[needle])
    amount_of_needle = Decimal('0')
    for item in list_with_needle:
        amount_of_needle += item['amount']
    return amount_of_needle

add(goods, 'Яйца', Decimal('3'), '2023-10-15')

print()
