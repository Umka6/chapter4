student = ['Kirill', 'Taalai', 'Umut','Daniyar','Bogdan']
name = input('enter the name')
while name != 'exit':
    name = input('enter the name')
    if name == 'exit':
       break
    student += name
else:
     print(student)