def evaluation(txt):
    a = input(txt)
    try:
        a= float(a)
    except:
        a= ""
    return a 


while True:
    
    txt = "Enter a number : "
    a = evaluation(txt)
    if type(a) != float:
        evaluation(txt)
    else:
        print("Thanks")
        break
    