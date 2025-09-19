service = 0
def tipcalc():
    tip = input ("How was the service? Bad, Okay, Good, Great")
    tip_perc = 0    
    if tip == "Great":
      tip_perc = 0.25
    elif tip == "Good":
      tip_perc = 0.20
    elif tip == "Okay":
      tip_perc = 0.15
    elif tip == "bad":
      tip_perc = 0
    else:
        print ("Invalid")
    bill = float(input("what is your billamount"))
    print(tip_perc)
    subtotal = tip_perc * bill
    print(subtotal)
    Total = subtotal + bill 
    print (f"This is your total: {Total}")
tipcalc()
