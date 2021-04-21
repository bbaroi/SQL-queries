import sqlite3

def all_restaurants():
    print("The List of all Italian restaurants in TORONTO")
    print("-"*50)
    conn = sqlite3.connect("restaurants.db")
    cursor = conn.cursor()
    sql = '''SELECT name, location from italian_restaurants'''
    result = cursor.execute(sql)
    restaurants = result.fetchall()
    for restaurant in restaurants:
        print(restaurant)

def west_end_restaurants():
    print("The List of Italian restaurants in west-end TORONTO")
    print("-"*60)
    conn = sqlite3.connect("restaurants.db")
    cursor = conn.cursor()
    sql = '''SELECT name, location from italian_restaurants WHERE location="west-end Toronto"'''
    result = cursor.execute(sql)
    restaurants = result.fetchall()
    for restaurant in restaurants:
        print(restaurant)

def east_end_restaurants():
    print("The List of Italian restaurants in east-end TORONTO")
    print("-"*60)
    conn = sqlite3.connect("restaurants.db")
    cursor = conn.cursor()
    sql = '''SELECT name, location from italian_restaurants WHERE location ="east-end Toronto"'''
    result = cursor.execute(sql)
    restaurants = result.fetchall()
    for restaurant in restaurants:
        print(restaurant)

def downtown_restaurants():
    print("The List of Italian restaurants in downtown TORONTO")
    print("-"*55)
    conn = sqlite3.connect("restaurants.db")
    cursor = conn.cursor()
    sql = '''SELECT name, location from italian_restaurants WHERE location = "downtown Toronto"'''
    result = cursor.execute(sql)
    restaurants = result.fetchall()
    for restaurant in restaurants:
        print(restaurant)

def address(get_address):
    print("The address of {}".format(get_address))
    print("-"*40)
    conn = sqlite3.connect("restaurants.db")
    cursor = conn.cursor()
    sql = '''SELECT address from italian_restaurants WHERE name LIKE ?'''
    result = cursor.execute(sql,(get_address,))
    restaurants = result.fetchall()
    for restaurant in restaurants:
        print(restaurant)

def phone_num(get_ph_num):
    print("The phone number of {}".format(get_ph_num))
    print("-"*45)
    conn = sqlite3.connect("restaurants.db")
    cursor = conn.cursor()
    sql = '''SELECT phone from italian_restaurants WHERE name LIKE ?'''
    result = cursor.execute(sql,(get_ph_num,))
    restaurants = result.fetchall()
    for restaurant in restaurants:
        print(restaurant)

def main():
    while True:
        print("\nA - Name and Address of all italian restaurants in Toronto\nB - All italian restaurants in west end Toronto\nC - All italian restaurants in east end Toronto\nD - All italian restaurants in downtown Toronto\nE - Restaurant address\nF - Restaurant PH#\n")
        options= input("\nPick options A - F from the list above: ")
        if options.lower() == 'a':
            all_restaurants()
        elif options.lower() == 'b':
            west_end_restaurants()
        elif options.lower() == 'c':
            east_end_restaurants()
        elif options.lower() == 'd':
            downtown_restaurants()
        elif options.lower() == 'e':
            get_address = input("Restaurant name: ")
            address(get_address)
        elif options.lower() == 'f':
            get_ph_num = input("Restaurant name: ")
            phone_num(get_ph_num)
        elif options.lower() =='q':
            break
        else:
            print("\n****Pick options A - F from the list or enter Q to quit****\n") 


if __name__ == "__main__":
    main()
