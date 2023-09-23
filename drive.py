import weather

city = input("Enter City Name: ")
coordinates = weather.get_coorinates(city)
temprature = weather.get_temp(*coordinates)

temp =str((temprature['main']['temp']))
temp_min =str((temprature['main']['temp_min']))
temp_max =str((temprature['main']['temp_max']))
feels_like =str((temprature['main']['feels_like']))
pressure = str((temprature['main']['pressure']))
humidity = str((temprature['main']['humidity']))


print(f'\nTemp = {temp}\nMin Temp = {temp_min}\nMax Temp = {temp_max}\nFeels Like = {feels_like}\nPressure = {pressure}\nHumidity = {humidity}')
