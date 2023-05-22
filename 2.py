current_temp = int(input("Please input temprature in Fahrenheit: "))
#print(current_temp)
condition = str(input("Is it raining input Yes or No: "))
raining = ("yes" == condition.lower())

if current_temp < 50 :
    print("Wear a coat, hat, scarf and gloves.")
elif current_temp >= 50 and current_temp <= 70 and raining == (1==2):
    print("Wear a sweater or light jacket ")
elif current_temp >= 50 and current_temp <= 70 and raining == (1==1):
    print("Wear a jacket and pair of boots ")
elif current_temp > 70 and  raining == (1==2):
    print("Wear a t-shirt and shorts ")
elif current_temp > 70 and  raining == (1==1):
    print("Wear a light jacket  and boots")  
else:
    print("invalid input")