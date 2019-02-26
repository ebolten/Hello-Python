def hello():
    times = input('How many times do you want to see "Hello World"?: ')
    print ('. . .')
    for i in range(int(times)):
        print ('Hello World!')

    again = input('Would you like to see "Hello World" again?: ')
    if again.lower() == 'yes':
        return hello()
    elif again.lower() == 'no':
        print ('Ok! Goodbye :)')
    else:
        print ('That was not a "yes" or "no"')
        return hello()

hello()
