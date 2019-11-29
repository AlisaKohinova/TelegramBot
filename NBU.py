import requests

class Nbu:
    def __init__(self):
        self.url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json'


    def today_currencies(self):
        today = requests.get(self.url).json()
        date = today[0]['exchangedate']
        info = f'Сегодняшняя дата: {date} \n'
        with open('today_currencies.txt', 'a', encoding='utf-8') as file:
            file.write(date + '\n')
            num = 1
            print(date + '\n')
            for i in today:
                text_row = str(num) + ' - ' + i['txt'] + ' -- ' + str(i['rate']) + '\n'
                print(text_row)
                info += text_row
                text_row = file.write(text_row)
                num += 1
        return info
    def get_currency(self):
        user_date = input('Enter date in format YYYYMMDD:')
        user_currency = input('Currency name in Ukrainian:').strip()

        try:
            date_info = requests.get(self.url + '&date=' + user_date).json()
            for i in date_info:
                if i['txt'].lower() == user_currency.lower():
                    return f"{[i['txt']]} = {i['rate']} on date: {i['exchangedate']}"
        except:
            print('Invalid date or currency input.')

