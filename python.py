from time import sleep
print("Welcome To Age Test")
type = input('''Do You Want To Find Your Age(1) Or Birth Year(2)?
 ''')
if type="1":
 birthdate = input('What Is Your Birthdate? ')
 int(birthdate)
 age = 2022 - int(birthdate)
 print("You Are"+age+"years old.")
 sleep(1)
 print('Thankyou for using age.test')
if type="2":
 age1 = input('What Is Your Age')
 int(age)
 birthyear = 2022 - int(age1)
 print("You Were Born In"+birthyear)
 sleep(1)
 print('Thankyou for using age.test')
