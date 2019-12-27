import pyowm

owm = pyowm.OWM('54a2f131c5a1a86d827374c22af22e54', language = "ru")

palce = input('В каком городе? ')

observation = owm.weather_at_place(palce)
w = observation.get_weather()

temp = round(w.get_temperature('celsius')['temp'])

print('В городе ' + palce + ' сейчас ' + w.get_detailed_status())
print('Температура сейчас в районе ' + str(temp) + ' градусов')

if temp < 0:
    print('Сейчас ппц как холодно, одевайся теплее!')
elif temp < 15:
    print('Сейчас холодно, не зыбудь свиторок =) ')
else:
    print('Температура норм! Кайфуй! ')

input()
# print(w)