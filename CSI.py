def main():
        intro = input("Yo whats good lemme holla at yo name?")

        name = intro
        print ("Whats good ",name[0].upper() + name[1:].lower() + " ya fool")

        q1 = input("Where was ur exact location on the night of 11/03/2019?")
        if q1 == 'school':
            print ("You may go")

        else:
            print ("You are now a suspect of the murder of Curtis Knox")

main()

while True:
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print ('Hold up we getting u back')
    if answer == 'y':
        break
    else:
        print ('Goodbye')
        break
    break
main()

           
