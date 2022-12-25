from transitions.extensions import GraphMachine
from linebot.models import MessageAction,URIAction,MessageTemplateAction,CarouselColumn,MessageEvent, TextMessage, TextSendMessage,URIAction,MessageAction
from utils import send_button_message, send_carousel_message, send_image_message, send_text_message,send_text_multiple_message,send_video_message
from utils import send_text_message
from utils import power


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.weight = -1
        self.height = -1
        self.choice = ''
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_power(self, event):
        return event.message.text == '次方'

    def on_enter_Input_num(self, event):
        reply = event.reply_token
        text = event.message.text
        send_text_message(reply, '請輸入數字')

    def on_enter_Input_num1(self, event):
        reply = event.reply_token
        text = event.message.text
        send_text_message(reply, '請輸入要的次方數')

def on_enter_user(self, event):
        self.weight = -1
        self.height = -1
        self.choice = ''
        print('還在user')
        title = '請選擇想要的功能'
        text = '功能如下'
        btn = [
            MessageTemplateAction(
                label = '計算次方',
                text ='計算次方'
            ),
            
        ]
        send_button_message(event.reply_token, title, text, btn, url) 