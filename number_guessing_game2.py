print("Think about a number between 0 and 1000, I will guess it in 10 attempts")
min = 0
max = 1000
while True:
    guess = int(((max - min) / 2) + min)
    print("I'm guessing:", guess)
    ans = 0
    while True:
        try:
            ans = int(input("Press 1 if my guess was too big, press 2 if my guess was too low, press 3 if I won: "))
            if ans <= 3 and ans >= 1:
                break
            else:
                continue
        except:
            continue
    if ans == 3:
        print("I won!!!")
        break
    elif ans == 2:
        min = guess
        continue
    elif ans == 1:
        max = guess
        continue
