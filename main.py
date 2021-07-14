from tkinter import *
import requests

win = Tk()

def get_weather():
	city = cityField.get()
	key  = '8b023b88c76fd1fb80e6f07061550c91'
	url  = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': key, 'q':city, 'units':'metric'}

	result = requests.get(url, params=params)
	weather = result.json()

	info['text'] = f"{str(weather['name'])}:{weather['main']['temp']}"

win.title('Weather')
win.geometry('300x250')
win.resizable(False, False)

frame_top = Frame(win, bg='#fff')
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(win, bg='#fff', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg = '#fff', font=30)
cityField.pack()

btn = Button(frame_top, text = 'Подивитися погоду', command = get_weather)
btn.pack()

info = Label(frame_bottom, text='Інформація про погоду', font=40)
info.pack()

win.mainloop()