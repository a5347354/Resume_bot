from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import QAresume as qa
import json

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('')
# Channel Secret
handler = WebhookHandler('')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text.strip().lower()

    with open('mode_changed', 'r' , encoding='utf8') as f:
        mode = bool(json.load(f))

    if "模式切換" == message or "切換模式" == message:
        with open('mode_changed', 'w', encoding='utf8') as f:
            mode = not mode
            json.dump(mode, f, ensure_ascii=False)
            if mode:#通知模式改變
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='text message'))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='text message'))


    # 以SVM判斷
    if mode:
        message = qa.predict_cat(message)
        print(message)

    if "問題請教" in message or "主目錄" == message or "main" == message:
        line_bot_api.reply_message(event.reply_token, questions())
    elif "hello" == message:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='text message'))
    elif "關於你" in message or "個性" in message:
        line_bot_api.reply_message(
            event.reply_token, [
                    TextSendMessage(text='text message'),
                    StickerSendMessage(package_id=11538, sticker_id=51626527)
                ]
        )
    elif "怎麼樣的人" in message or "luke" in message or "about me" in message or "關於我" in message or "個性" in message:
        line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='text message'),
                    aboutme()
                ]
            )

    elif "經歷" in message or "experience" == message:
        line_bot_api.reply_message(event.reply_token, experience())

    elif "專案" in message or "project" == message:
        line_bot_api.reply_message(event.reply_token, project())

    elif "得獎" in message or "獎項" in message or "獎" in message or "award" == message:
        line_bot_api.reply_message(event.reply_token, award())

    elif "論文" in message or "thesis" == message:
        line_bot_api.reply_message(event.reply_token, thesis())

    elif "證照" in message or "certificate" == message:
        line_bot_api.reply_message(event.reply_token, certificate())

    elif "興趣" in message or "hobby" == message:
        line_bot_api.reply_message(event.reply_token, hobby())

    else: #教導使用者使用
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='text message'))



def questions():
    template_message = TemplateSendMessage(
        alt_text='text message',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='',
                    action=PostbackTemplateAction(
                        label='About me',
                        text='text message',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='',
                    action=PostbackTemplateAction(
                        label='Experience',
                        text='text message',
                        data='action=buy&itemid=2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='',
                    action=PostbackTemplateAction(
                        label='Project',
                        text='text message',
                        data='action=buy&itemid=3'
                    )
                ),
                ImageCarouselColumn(
                    image_url='',
                    action=PostbackTemplateAction(
                        label='Award',
                        text='text message',
                        data='action=buy&itemid=4'
                    )
                ),
                ImageCarouselColumn(
                    image_url='',
                    action=PostbackTemplateAction(
                        label='Thesis',
                        text='text message',
                        data='action=buy&itemid=5'
                    )
                ),
                ImageCarouselColumn(
                    image_url='',
                    action=PostbackTemplateAction(
                        label='Certificate',
                        text='text message',
                        data='action=buy&itemid=6'
                    )
                ),
                # ImageCarouselColumn(
                #     image_url='',
                #     action=PostbackTemplateAction(
                #         label='Club',
                #         text='text message',
                #         data='action=buy&itemid=7'
                #     )
                # ),
                ImageCarouselColumn(
                    image_url='',
                    action=PostbackTemplateAction(
                        label='Hobby',
                        text='text message',
                        data='action=buy&itemid=8'
                    )
                )

            ]
        )
    )
    return template_message


def aboutme():
    aboutme_ImagemapMessage = ImagemapSendMessage(
        base_url='',
        alt_text='text message',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri='',
                area=ImagemapArea(
                    x=0, y=0, width=520, height=1040
                )
            )
            # MessageImagemapAction(
            #     text='text message',
            #     area=ImagemapArea(
            #         x=520, y=0, width=520, height=1040
            #     )
            # )
        ]
    )
    return aboutme_ImagemapMessage


def experience():
    experience_Carousel_template = TemplateSendMessage(
        alt_text='text message',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Note',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        MessageTemplateAction(
                            label='無',
                            text='text message'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        MessageTemplateAction(
                            label='無',
                            text='text message'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        MessageTemplateAction(
                            label='無',
                            text='text message'
                        )
                    ]
                )
            ]
        )
    )
    return experience_Carousel_template

def project():
    project_Carousel_template = TemplateSendMessage(
        alt_text='text message',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='github',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='github',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='github',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='github',
                            uri=''
                        )
                    ]
                )
            ]
        )
    )
    return project_Carousel_template

def award():
    award_Carousel_template = TemplateSendMessage(
        alt_text='text message',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                )
            ]
        )
    )
    return award_Carousel_template

def thesis():
    thesis_Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://example.com/preview.jpg',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                )
            ]
        )
    )
    return thesis_Carousel_template

def certificate():
    certificate_Carousel_template = TemplateSendMessage(
        alt_text='text message',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Link',
                            uri=''
                        )
                    ]
                )
            ]
        )
    )
    return certificate_Carousel_template

def hobby():
    hobby_Carousel_template = TemplateSendMessage(
        alt_text='text message',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Picture',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='title message',
                    text='text message',
                    actions=[
                        URITemplateAction(
                            label='Picture',
                            uri=''
                        )
                    ]
                )
            ]
        )
    )
    return hobby_Carousel_template



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
