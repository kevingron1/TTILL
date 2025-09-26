import csv
import os
import locale



products = []           #lista

def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products


def view_products(products):
    for index, products in enumerate(products):
        print()
        
def list_all_products(products):
    for idx, product in enumerate(products):
        print(f"{idx+1} {product['name']} {product['price']} {product['quantity']}")

#TODO: Gör så man kan lägga till / ta bort produkt

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

load_data('db_products.csv')

os.system('cls')

print("X = Ta Bort Produkt \nA = Lägg till Produkt")

list_all_products(products)
choice = input().strip().upper()
if choice == "X":
    print("Vilken produkt vill du ta bort? (ange nummer)")
    list_all_products(products)
    idx = int(input("Välj produkt: "))
    product = products[idx-1]
    products.remove(product)
    print(f"Produkten {product['name']} togs bort")
    with open('db_products.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for p in products:
            writer.writerow(p)
elif choice == "A":
    print("Lägg till produkt")
    name = input("Namn: ")
    desc = input("Beskrivning: ")
    price = float(input("Pris: "))
    quantity = int(input("Kvantitet: "))
    id = max(p['id'] for p in products) + 1 if products else 1
    new_product = {
        "id": id,
        "name": name,
        "desc": desc,
        "price": price,
        "quantity": quantity
    }
    products.append(new_product)
    print(f"Produkten {name} lades till")
    with open('db_products.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for p in products:
            writer.writerow(p)

while True:
    idx = int(input("Välj produkt: "))
    product = products[idx-1]

    print(f"ID #: {product['id']} \nNamn: {product['name']} \nBeskrivning: {product['desc']} \nPris: {product['price']} {'SEK'} \nKvantitet: {product['quantity']}")