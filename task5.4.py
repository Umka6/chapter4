user = input("enter the password")
password = 'umka'
count = 1
if user == password:
    print('True')
while user != password:
    print("False")
    user = input('enter the password')
    count+=1
    print(count)
    if count > 3:
        print('you spent all attempts')
        break