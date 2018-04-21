# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, session
import os
from statistics import mean as average


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


# добавляємо секретний ключ для сайту щоб шифрувати дані сессії
# при кожнаму сапуску фласку буде генечитись новий рандомний ключ з 24 символів
app.secret_key = os.urandom(24)
app.secret_key = '125'

@app.route('/')
def home():
    context = {}
    c_min_list =[1,2,3,445,5,6,7,8,9,10]
    context['c_min'] = round(average(c_min_list))
    c_max_list =[1,2,3,4,5,654,7,8,9,10]
    context['c_max'] = round(average(c_max_list))
    c_current_list =[1,2,3,4,5,654,7,8,9,10]
    context['c_current'] = round(average(c_current_list))
    # видумати логіку вираховування статусу емодзі на основі середньої темпаратури ,опадів,приготувати емодзі
    wind_list =[1,223,334,4,5,65,7,8,9,10]
    context['wind'] = round(average(wind_list))
    context['c_feel'] ='загуглити як на основі погодних даних виводити :як відчувається'
    precipitation_list =[21,23,53,64,75,63,72,81,91,10]
    context['precipitation'] = round(average(precipitation_list))
    humidity= [40,50,45,34,34,23,54,54,33]
    context['humidity']=round(average(humidity))
    print(round(average(humidity)))
    division = 1 / 8
    dew_point=((round(average(humidity))/100)**division * (112+0.9*round(average(c_current_list)))+0.1*round(average(c_current_list))-112)
    print(dew_point)
    return render_template('home.html',context=context)
if __name__ == '__main__':
    app.run(debug=True, port=7778)
