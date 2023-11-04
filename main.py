Welcoming_message= print("You are in the system")
His_name = input("Enter your name please:")
Welcoming=print("Hi "+His_name)
His_age = input('How old are you?:')
if int(His_age) < 18 :
     print("you are too young")
     print('Thank you for using the system')
     breakpoint()
else:
    print('Welcome to the system')
His_choice = input('What do want to do?:')
if str(His_choice):
    the_code=input("You have now to enter the code in one digit:")
if 4 < int(the_code) < 10:
    print("You have been accessed to your system "+His_name)
    print("choose your order")
    print('5 = Browsing. 6=Returning. 7=Purchasing. 8=Selecting. 9=Get out')
    The_number=input('Enter your order:')
    if int(The_number) == 5:
        input("Please write what you are searching for")
    if int(The_number) ==  6 :
     print("you can contact the call center by typing the number(0505560555),"
     "we wish you a happy day")
    if int(The_number) == 7 :
     His_order=input("Please type your order:")
     The_answer= print('Searching,please wait.')
    if int(The_number) == 8:
     the_number_of_the_order = input('Please type the serial number of your order:')
    if int(The_number) == 9:
     final_quation= input("Are you sure you wanna go out?:")
    if str(final_quation) == str(True):
        print("You are out of the system")
    else:
        print("Unfurtionatly you have to go out and get back again")
        breakpoint()
elif 0 < int(the_code) < 5:
    print("you are at the wrong system "+(His_name)+' you are going to another system')
    print("Transferring to another system")





