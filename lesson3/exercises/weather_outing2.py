import random

weather_types = ["sunny","windy","snowing","pleasant","thunderstorms","rain","cloudy"]
tomorrow_weather = input("Hello I am Dimpy, do you want the latest weather report for tomorrow, please answer only Y for yes or N for no ")
Dimpy_weather = random.choice(weather_types)
if tomorrow_weather == "Y":
    print("tomorrows weather is",Dimpy_weather,", have a nice day!")

    if Dimpy_weather == "sunny" or Dimpy_weather == "windy" or Dimpy_weather == "pleasant" or Dimpy_weather == "cloudy":
        print("Hello family tomorrow weather is",Dimpy_weather,", lets go for an outing")

    else:
        print("Hello family tomorrow weather is", Dimpy_weather, ", Tomorrow is not a great day to go out")


else:
    print("You didn't want the latest weather report per your selection, Ok bye have a good day")
