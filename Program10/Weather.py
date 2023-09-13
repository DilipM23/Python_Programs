import json

with open("D:\Dilip\VS Code\Python\weather.json.txt",'rb') as f :
    data = json.load(f)

current_temp = data['main']['temp']
humidity = data['main']['humidity']
des = data['weather']['des'] 

print(f'Current Temperature :{current_temp} deg celsius')
print(f'Humidity :{humidity}')
print(f'Weather Description :{des}')