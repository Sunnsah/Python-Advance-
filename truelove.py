while(True):
    print("Press q for quite")
    a = input(" Enter a Number : ")

    if a == 'q':
        break
    try:
        a = int(a)
        if a > 50:
            print(f"You Entered a number greater than 50  that is {a}")
    except Exception as e:
        print(f"You enter a {e}")
        