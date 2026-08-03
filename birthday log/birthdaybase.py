birthday={'Rudro':'04sep','aparna':'14may'}
while True:
    print('Enter the name(leave it empty to quite)')
    name=input()
    if name=='':
        break
    if name in birthday:
        print(birthday[name]+' is the birthday of '+ name)
    else:
        print('I dont have info of '+name+' whats the birthday?')
        date=input()
        birthday[name]=date
        print('Database updated')
