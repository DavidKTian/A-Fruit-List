string1=input("Write any food that begins with the letter 'a'")
string1.lower()

if string1.startswith("a")==True:
  print("Good job")
elif string1.startswith("a")==False:
  print("Your input didn't start with 'a'. Please try again.")

string2=input("Now, write any food that ends with 'b'.")
string2.lower()

if string2.endswith("b")==True:
  print("That's right!")
elif string2.endswith("b")==False:
  print("No, that's not right.")

fruits=input("Now, enter five different fruits, separated by commas.\n")
fruits = fruits.split(",")
list1=[fruit.strip(' ') for fruit in fruits]

print("Now, let's see if %s is in this list"%string1)

if string1 in list1:
  print("Yes, it is")
elif string1 not in list1:
  print("No, it isn't.")

print("Now, let's see if %s is in this list"%string2)

if string2 in list1:
  print("Good work")
elif string2 not in list1:
  print("Not true")
