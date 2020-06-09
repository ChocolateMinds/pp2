weather_input = input("Hey, Dimpy! how's the weather tomorrow? (must enter sunny, rainy or snowy)\n")

if weather_input.lower() == "sunny":
    print("We all can go out!")
elif weather_input.lower() == "rainy" or weather_input == "snowy":
    print("Pch, it's a rainy day, let's stay put ")
else:
    print("Looks like you've not got what I'm asking you Dimpy!")