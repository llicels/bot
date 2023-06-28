import requests
#import telegram

class Alert:

    def telegram_alert(title, link):

        bot_token = '6149270833:AAEzUosTzfF6ljnVbEZvKT1vYOtG5jhi1F0'
        bot_chatID = '5776053316'
        send_api = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + title
        send_apiDetails = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + link
        response = requests.get(send_api)
        response = requests.get(send_apiDetails)