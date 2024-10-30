lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
l2 = [dict for dict in lst1 if isinstance(dict,str)]
print(l2)

if type(str) in l2: #Перевірив через цик чи тип стрінг:)
    print('String')
else:
    print("Not String")