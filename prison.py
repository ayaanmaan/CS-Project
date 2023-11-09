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

person_type_keywords = {'employee':{'title':'job', 'date':'date of hire'},'prisoner':{'title':'sentence', 'date':'incarceration date'}}
                                    
def rec_entry(rec_type):
    
    unique_id = False
    
    while not unique_id:
        
        rec_id = intcin(f"Enter {rec_type} ID: ")
        
        with open(f'{rec_type}.csv', 'a+', newline='') as rec_f:                                     

                if rec_id not in [row[0] for row in csv.reader(rec_f)]:
                    
                    name = input(f"Enter {rec_type} name: ")
                    title = input(f"Enter {rec_type} {person_type_keywords[rec_type]['title']}: ")
                    date = input(f"Enter {rec_type} {person_type_keywords[rec_type]['date']}: ")

                    csv.writer.writerow([rec_id, name, title, date])

                    unique_id = True

                else:
                    pass

def rec_search(rec_type):

    rec_id = intcin(f"Enter {rec_type} ID to search: ")

    with open(f'{rec_type}.csv', newline='') as rec_f:

        try:
            found_rec = csv.reader(rec_f)[[row[0] for row in csv.reader(rec_f)].index(rec_id)]
            print('Record found\n'+'-'*20+'\n'+f"Name: {found_rec[1]}\n{person_type_keywords[rec_type]['title'].capitalize()}: {found_rec[2]}\n{person_type_keywords[rec_type]['date']}: {found_rec[3]}")

        except ValueError:
            print('Record not found')

def rec_display(rec_type):
    
    with open(f'{rec_type}.csv', newline='') as rec_f:

        print(tab(csv.reader(rec_f), headers=[f"{rec_type.capitalize()} ID", f"{rec_type.capitalize()} Name", f"{person_type_keywords[rec_type]['title'].capitalize()}", f"{person_type_keywords[rec_type]['date'].capitalize()}"]))

def rec_remove(rec_type):
    
    rec_id = intcin(f"Enter {rec_type} ID to remove: ")
    
    with open(f'{rec_type}.csv', newline='') as rec_f:

        recs = csv.reader(rec_f)
        recs.remove(recs[[row[0] for row in csv.reader(rec_f)].index(rec_id)])

    with open(f'{rec_type}.csv', 'w', newline='') as rec_f:

        for row in recs:
            csv.writer.writerow(row)
        











        
        
    
