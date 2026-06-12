temperature = float(input("Enter today's temperature in Celsius: "))

if temperature < 20:
    print("Cold Day")
    if temperature < 10:
        print("Wear a jacket!")

elif temperature <= 30:
    print("Warm Day")
    if temperature > 25:
        print("It's a good day for outdoor activities!")
elif temperature > 30:
    print("Hot Day")
    if temperature > 35:
        print("Stay hydrated and avoid direct sunlight!")

        