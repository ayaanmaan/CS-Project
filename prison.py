import csv
from tabulate import tabulate as tab

def intcin(msg):
    inp = False
    while not inp:
        try:
            return int(input(msg))
            inp = True   
        except ValueError:
            print('Invalid Input - Expected an integer')
            pass

rec_type = {1:'employee', 2:'prisoner'}
person_type_keywords = {'employee':{'title':'job', 'date':'date of hire'},'prisoner':{'title':'sentence', 'date':'incarceration date'}}

def rec_entry(rec_type_num):
    global rec_type
    unique_id = False
    while not unique_id:
        rec_id = intcin(f"Enter {rec_type[rec_type_num]} ID: ")
        with open(f'{rec_type[rec_type_num]}.csv', newline='') as rec_f_read:
            rec_type_data = list(csv.reader(rec_f_read))
        if rec_id not in list(map(int,[row[0] for row in rec_type_data])):
            name = input(f"Enter {rec_type[rec_type_num]} name: ")
            title = input(f"Enter {rec_type[rec_type_num]} {person_type_keywords[rec_type[rec_type_num]]['title']}: ")
            date = input(f"Enter {rec_type[rec_type_num]} {person_type_keywords[rec_type[rec_type_num]]['date']}: ")
            with open(f'{rec_type[rec_type_num]}.csv', 'a', newline='') as rec_f:
                csv.writer(rec_f).writerow([rec_id, name, title, date])
            unique_id = True
        else:
            print(f"{rec_type[rec_type_num].capitalize()} ID {rec_id} already exists.")
            pass

def rec_search(rec_type_num):
    global rec_type
    rec_id = intcin(f"Enter {rec_type[rec_type_num]} ID to search: ")
    with open(f'{rec_type[rec_type_num]}.csv', newline='') as rec_f:
        recs = list(csv.reader(rec_f))
        try:
            found_rec = [recs[list(map(int,[row[0] for row in recs])).index(rec_id)]]
            print('RECORD FOUND')
            print(tab(found_rec, headers=[f"{rec_type[rec_type_num].capitalize()} ID", f"{rec_type[rec_type_num].capitalize()} Name", f"{person_type_keywords[rec_type[rec_type_num]]['title'].capitalize()}", f"{person_type_keywords[rec_type[rec_type_num]]['date'].capitalize()}"],tablefmt='outline'))
        except ValueError:
            print('\nRECORD NOT FOUND')

def rec_display(rec_type_num):
    global rec_type
    with open(f'{rec_type[rec_type_num]}.csv', newline='') as rec_f:
        print(tab(list(csv.reader(rec_f)), headers=[f"{rec_type[rec_type_num].capitalize()} ID", f"{rec_type[rec_type_num].capitalize()} Name", f"{person_type_keywords[rec_type[rec_type_num]]['title'].capitalize()}", f"{person_type_keywords[rec_type[rec_type_num]]['date'].capitalize()}"],tablefmt='outline'))

def rec_remove(rec_type_num):
    global rec_type
    rec_id = intcin(f"Enter {rec_type[rec_type_num]} ID to remove: ")
    with open(f'{rec_type[rec_type_num]}.csv', newline='') as rec_f:
        recs = list(csv.reader(rec_f))
        recs.remove(recs[list(map(int,[row[0] for row in recs])).index(rec_id)])
    with open(f'{rec_type[rec_type_num]}.csv', 'w', newline='') as rec_f:
        for row in recs:
            csv.writer(rec_f).writerow(row)

def menu1():
    global rec_type
    while True:
        command_num = intcin(f'''
Available commands:
1. Quit
2. Access employee records
3. Access prisoner records

Enter a command number: ''')
        if command_num == 1:
            raise SystemExit
        elif command_num in (2,3):
            menu2(command_num-1)
        else:
            print('Invalid command number. Choose a number from 1 to 3 for corresponding commands.')

def menu2(rec_type_num):
    global rec_type
    while True:
        command_num = intcin(f'''
Available commands:
1. Quit
2. Enter {rec_type[rec_type_num]} record
3. Search {rec_type[rec_type_num]} record from ID
4. Display all {rec_type[rec_type_num]} records
5. Delete {rec_type[rec_type_num]} record from ID
6. Go back

Enter a command number: ''')
        if command_num == 1:
            raise SystemExit
        elif command_num == 2:
            rec_entry(rec_type_num)
        elif command_num == 3:
            rec_search(rec_type_num)
        elif command_num == 4:
            rec_display(rec_type_num)
        elif command_num == 5:
            rec_remove(rec_type_num)
        elif command_num == 6:
            menu1()
        else:
            print('Invalid command number. Choose a number from 1 to 6 for corresponding commands.')
    
        

print('''
   _____           _             _   _____      _                                                           
  / ____|         | |           | | |  __ \    (_)                                                          
 | |     ___ _ __ | |_ _ __ __ _| | | |__) | __ _ ___  ___  _ __                                            
 | |    / _ \ '_ \| __| '__/ _` | | |  ___/ '__| / __|/ _ \| '_ \                                           
 | |___|  __/ | | | |_| | | (_| | | | |   | |  | \__ \ (_) | | | |                                          
  \_____\___|_| |_|\__|_|  \__,_|_| |_|   |_|  |_|___/\___/|_| |_|               
  __  __                                                   _     _____       _             __
 |  \/  |                                                 | |   |_   _|     | |           / _|              
 | \  / | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_    | |  _ __ | |_ ___ _ __| |_ __ _  ___ ___ 
 | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|   | | | '_ \| __/ _ \ '__|  _/ _` |/ __/ _ \\
 | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_   _| |_| | | | ||  __/ |  | || (_| | (_|  __/
 |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__| |_____|_| |_|\__\___|_|  |_| \__,_|\___\___|
                            __/ |                                                                           
                           |___/
''')

menu1()
