#сделала соседний 4й вариант, тк у меня был третий
import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Функция для получения погоды
def get_weather(city_name):
    weather_api_key = '1f9b43d9f31e98f0322b59684be067c0'  
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}&units=metric'
    
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'Город': data['name'],
            'Температура (°C)': data['main']['temp'],
            'Влажность (%)': data['main']['humidity'],
            'Давление (гПа)': data['main']['pressure'],
            'Описание': data['weather'][0]['description']
        }
        return weather
    else:
        return {'Ошибка': 'Не удалось получить данные о погоде'}


if __name__ == '__main__':
    city_name = input('Введите название города для получения погоды: ')
    weather_info = get_weather(city_name)
    
    print("\nИнформация о погоде:")
    for key, value in weather_info.items():
        print(f'{key}: {value}')


# задание 2


# Функция для получения новостей
def get_news():
    news_api_key = '4beae52df4284a2eacaeb1509cb25671'  
    news_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}'  #с России не получалось взять новости:(
    
    response = requests.get(news_url)
    
    # Проверяем статус ответа
    if response.status_code == 200:
        data = response.json()
        # Проверяем наличие статей
        if data['totalResults'] > 0:
            articles = data['articles'][:5]  
            news_list = []
            for article in articles:
                news_item = {
                    'Заголовок': article['title'],
                    'Описание': article['description'],
                    'Источник': article['source']['name'],
                    'URL': article['url'],
                    'Дата': article['publishedAt']
                }
                news_list.append(news_item)
            return news_list
        else:
            return [{'Ошибка': 'Нет доступных новостей'}]
    else:
        return [{'Ошибка': f'Не удалось получить данные о новостях. Код ошибки: {response.status_code}'}]


if __name__ == '__main__':
    print("Получение новостей...")
    news_info = get_news()
    
    print("\nНовости:")
    for news in news_info:
        if 'Ошибка' in news:
            print(news['Ошибка'])
        else:
            print(f"Заголовок: {news['Заголовок']}")
            print(f"Описание: {news['Описание']}")
            print(f"Источник: {news['Источник']}")
            print(f"URL: {news['URL']}")
            print(f"Дата: {news['Дата']}\n")


# допзадание

def get_random_fox():
    response = requests.get('https://randomfox.ca/floof/')
    if response.status_code == 200:
        data = response.json()
        return data['image']
    else:
        return None

def update_image():
    url = get_random_fox()
    if url:
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img_data)
        label.config(image=img)
        label.image = img

root = tk.Tk()
root.title("Милые лисички!")

label = tk.Label(root)
label.pack()

button = tk.Button(root, text="переключить", command=update_image)
button.pack()

update_image()

root.mainloop()
