import sqlite3
with sqlite3.connect('top_hotels.db') as db:
    cursor=db.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS hotels(
id integer PRIMARY KEY,
hotels text NOT NULL,
location text NOT NULL,
country text NOT NULL,
region text NOT NULL,
company text NOT NULL,
score float NOT NULL,
rank integer NOT NULL,
rooms integer NOT NULL,
theme text NOT NULL,
year integer NOT NULL,
twentytwentyone integer NOT NULL,
past_rank integer);''')


hotel_list = []
hotelfile = open('top_hotels.csv', 'r')
for line in hotelfile:
    hotel_list.append(line)


#for a in range(1, len(hotel_list)):
#    hotel_list2 = []
#    hotel_list2 = hotel_list[a].strip()
#    hotel_list2 = hotel_list2.split(',')
#    hotels = hotel_list2[0]
#    location = hotel_list2[1]
#    country = hotel_list2[2]
#    region = hotel_list2[3]
#    company = hotel_list2[4]
#    score = hotel_list2[5]
#    rank = hotel_list2[6]
#    rooms = hotel_list2[7]
#    theme = hotel_list2[8]
#    year = hotel_list2[9]
#    twenty21 = hotel_list2[10]
#    past_rank = hotel_list2[11]
#    cursor.execute('''INSERT INTO hotels(hotels, location, country, region, company, score, rank, rooms, theme, year, twentytwentyone, past_rank)
#    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (hotels, location, country, region, company, score, rank, rooms, theme, year, twenty21, past_rank))
#    db.commit()
#hotelfile.close()

#cursor.execute('SELECT * FROM hotels')
#for x in cursor.fetchall():
#    print(x)
#print()

def choicepick():
    choice = int(input('1: Country\n2: Region\n3: Min. number of rooms\n4: Name/Part of name\n5: Rank in given range\n\nChoose a method to find hotels: '))
    while choice < 1 or choice > 5:
        choice = int(input('Enter a correct number: '))
    return choice
choice = choicepick()
print()

searchlist = []
cursor.execute('SELECT * FROM hotels')
for x in cursor.fetchall():
    searchlist.append(x)

def choice_1():
    countryfind = (input('Enter the country: ')).strip()
    for find in searchlist:
        country = find[3]
        if country.lower() == countryfind.lower():
            results.append(find)
    return results

def choice_2():
    regionfind = (input('Enter the region: ')).strip()
    for find in searchlist:
        region = find[4]
        if region.lower() == regionfind.lower():
            results.append(find)
    return results

def choice_3():
    min_rooms = int(input('Enter the min. number of rooms: '))
    for find in searchlist:
        rooms = find[8]
        if rooms >= min_rooms:
            results.append(find)
    return results

def choice_4():
     namefind = (input('Enter the name or part of the name: ')).strip()
     for find in searchlist:
        name = find[1]
        if namefind.lower() in name.lower():
            results.append(find)
     return results

def choice_5():
    range1 = int(input('Enter the first range of the rank: '))
    range2 = int(input('Enter the second range of the rank: '))
    if range2 < range1:
        tempnum = 0
        tempnum = range1
        range1 = range2
        range2 = tempnum
    for find in searchlist:
        rank = find[7]
        if range1 <= rank <= range2:
            results.append(find)
    return results
    
    
results = []
if choice == 1:
    results = choice_1()
elif choice == 2:
    results = choice_2()
elif choice == 3:
    results = choice_3()
elif choice == 4:
    results = choice_4()
elif choice == 5:
    results = choice_5()

for a in results:
    print(a)

hotelcount = 0
for row in results:
    hotelcount += 1
print()
if hotelcount == 1:
    print(hotelcount, 'hotel matches this description')
else:
    print(hotelcount, 'hotels match this description') 




