from transitions.extensions import GraphMachine
from linebot.models import MessageAction,URIAction,MessageTemplateAction,CarouselColumn,MessageEvent, TextMessage, TextSendMessage,URIAction,MessageAction
from utils import send_button_message, send_carousel_message, send_image_message, send_text_message,send_text_multiple_message,send_video_message
from utils import power


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.weight = -1
        self.height = -1
        self.choice = ''
        self.machine = GraphMachine(model=self, **machine_configs)


    def is_going_to_power_input_num(self, event):
        return event.message.text == '計算次方'

    def is_going_to_power_input_num1(self, event):
        text = event.message.text
        try:
            w = int(text)
        except ValueError:
            return False
        self.weight = w
        return True 

    def is_going_to_power_ans(self, event):
        text = event.message.text
        try:
            w = int(text)
        except ValueError:
            return False
        self.height = w
        return True   

    def is_going_to_cal_input_num(self, event):
        return event.message.text == '簡易計算機'


    def is_going_to_cal_input_num1(self, event):
        text = event.message.text
        try:
            w = int(text)
        except ValueError:
            return False
        self.weight = w
        return True 

    def on_enter_power_input_num(self, event):
        reply = event.reply_token
        text = event.message.text
        send_text_message(reply, '請輸入數字')

    def on_enter_power_input_num1(self, event):
        reply = event.reply_token
        text = event.message.text
        send_text_message(reply, '請輸入要的次方數')

    def on_enter_power_ans(self, event):
        ans = BMI(self.num, self.num1)
        title = '結果'
        text = f'power:{ans[0]}, {ans[1]}'
        btn = [
            MessageTemplateAction(
                label = '返回主選單',
                text ='返回主選單'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back(self, event):
        text = event.message.text
        return text == '返回主選單'

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
            MessageTemplateAction(
                label = '簡易計算機',
                text = '簡易計算機'
           )
        ]
        send_button_message(event.reply_token, title, text, btn) 