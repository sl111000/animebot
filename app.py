import os
import sys
import json

from flask import Flask,send_from_directory, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageTemplateAction,CarouselColumn,MessageEvent, TextMessage, TextSendMessage,URIAction,MessageAction
from utils import send_button_message, send_carousel_message, send_image_message, send_text_message,send_text_multiple_message,send_video_message
from fsm import TocMachine
from utils import send_text_message
os.environ['PATH'] =  os.pathsep + './Graphviz/bin/'
app = Flask(__name__, static_url_path="")
load_dotenv()
hash_map = dict()

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    import json

    data = json.loads(body)

    userId = data['events'][0]['source']['userId']
    machine = hash_map.setdefault(userId,TocMachine(
    states=["user", "power_input_num", "power_input_num1","power_ans","cal_input_num","cal_input_num1","cal_input_symbol","cal_ans"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "power_input_num",
            "conditions": "is_going_to_power_input_num",
        },
        {
            "trigger": "advance",
            "source": "power_input_num",
            "dest": "power_input_num1",
            "conditions": "is_going_to_power_input_num1",
        },
        {
            "trigger": "advance",
            "source": "power_input_num1",
            "dest": "power_ans",
            "conditions": "is_going_to_power_ans",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "cal_input_num",
            "conditions": "is_going_to_cal_input_num",
        },
        {
            "trigger": "advance",
            "source": "cal_input_num",
            "dest": "cal_input_num1",
            "conditions": "is_going_to_cal_input_num1",
        },
        {
            "trigger": "advance",
            "source": "cal_input_num1",
            "dest": "cal_input_symbol",
            "conditions": "is_going_to_cal_input_symbol",
        },
        {
            "trigger": "advance",
            "source": "cal_input_symbol",
            "dest": "cal_ans",
            "conditions": "is_going_to_cal_ans",
        },         
        {
            "trigger": "advance",
            "source":["user", "power_input_num", "power_input_num1","power_ans","cal_input_num","cal_input_num1","cal_input_symbol","cal_ans"],
            "dest": "user",
            "conditions": "back",
        },

    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
))
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            # send_text_message(event.reply_token, "Not Entering any State")
            if event.message.text == 'fsm圖':
                send_image_message(event.reply_token, f'{main_url}/show-fsm')
            else:
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
                send_button_message(event.reply_token, title, text, btn, url)

    return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)

    server = pywsgi.WSGIServer(('0.0.0.0',int(port)),port)

    server.serve_forever()
    #app.run(host="0.0.0.0", port=port, debug=True)

