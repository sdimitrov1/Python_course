Data = {}



while(True):
    newEntry = input ("Enter new Person data [y/n]?")
    print('Data')
    print('-----------------------')
    print('-----------------------')
    print('1 - Add/Update Person')
    print('2 - Display all Persons')
    print('3 - Give avg age of persons')
    print('4 - Search')
    print('5 - Delete Person')
    print('6 - Quit')
    choice = input('')
 
    if choice == '1':
        if newEntry == 'y':
            name = input('Enter the persons name:')
            Age = int(input('Enter the Age:'))
            City = input('Enter person City')
            Data[name] = Age
            print('Name added')
    elif choice == ('2'):
        for key, value in Data.items():
            print('Name:' + key)
            print(value)
            print('City' + City)
            print('--------')
    
    elif choice == ('3'):
        for age,values in Data.items():
            print(float(sum([int(i) for i in values])) / len(values))

    elif choice == ('4'):
        search_City = input('''Which City do you want to search?:''')
        position = 0
        for key, value in Data.items():
            position = position + 1
            if key == search_City:
                print('Name %s found in %s position' % (search_City, position))
                break
            else:
                print('Name %s not found in %s position' %
                      (search_City, position))
    elif choice == ('5'):
        which_one = input('''Who's Age do you want to delete?:''')
        for key, value in Data.items():
            if key == which_one:
                del Data[key]
                print('%s deleted' % which_one)
                break
            else:
                print('Name not found')
    elif choice == ('6'):
        Agefile = open('\\Desktop\Data\Data.txt', 'a')
        Agefile.write((Data))
        Agefile.close()
        break
Agefile = open('\\Desktop\Data\Data.txt')
Agename = (Agefile.read())


