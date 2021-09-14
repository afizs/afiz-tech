# School Management System

students = {'ID1': {'name': 'John', 'dob': '01-01-2010', 'class': '5'}, 
'ID2': {'name': 'Sarah', 'dob': '09-01-2010', 'class': '5'}, 
'ID3': {'name': 'Frank', 'dob': '09-01-2011', 'class': '6'}
}

print('-----'*8)
print('\tSchool Management System')
print('-----'*8)
choice = int(input('1. Total Number of Students \n2. Display Student details \n3. Add new student \n4. Exit\nChoose Your option = '))
if choice == 1:
    print(f'Total Students: {len(students)}')
elif choice == 2:
    pass
elif choice == 3:
    pass
else:
    pass