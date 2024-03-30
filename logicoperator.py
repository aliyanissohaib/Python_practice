temp = int(input("what is the temperature outside: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good")
elif temp < 0 and temp > 30:
    print("the temperature is not good")