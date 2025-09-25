""" friend_comes=True
money=True

def and_movies(friend,money):
         if friend == True and money == True:
          print("Going to the movies")
         else:
            print("I have no friends or i have no money")
        
""" """

and_movies(friend_comes,money) """
""" 
homework=True
def not_movies(homework):
    if not homework:
        print("movie time")
    else:
        print("hommework time,I hate russian")
not_movies(homework)  """
""" 
def factor(x,y):
    if x % y == 0:
        print(f"{y}is a factor of {x}")
factor(25,5) """

""" def oddoreven(x,y):
    if x % y == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is not even")
oddoreven(79489384,2) """


""" service = 0
def tipcalc():
    tip = input ("How was the service? Bad, Okay, Good, Great")
    tip_perc = 0    
    if tip == "Great":
      tip_perc = 0.25
    elif tip == "Good":
      tip_perc = 0.20
    elif tip == "Okay":
      tip_perc = 0.15
    elif tip == "Bad":
      tip_perc = 0
    else:
        print ("Invalid")
    bill = float(input("what is your billamount"))
    subtotal = tip_perc * bill
    Total = subtotal + bill 
    print (f"This is your total: {Total}")
tipcalc()
 """
def factors():
  list=[]
  num = input("What is your number?")
  num = int(num)
  for i in range(num):
    if num%(i+1) == 0:
      list.append(i+1)
  print (list)
factors()
 