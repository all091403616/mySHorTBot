# -*- coding: utf-8 -*-
from microurl import bitlyapi
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

bitly=bitlyapi('a4b39f77f63aed484b2cd0763e247bd1b3b2c261')

updater=Updater('1012001760:AAFsk8wi5VOBNrYp7psLxyXFyaF8X9kYBUY')

LINK,CLICK,MODE,ROBOTS=range(4)

def start_command(bot, update):
    try:
        b = bot.get_chat_member('-1001206881648', update.message.from_user.id)
        if b.status == 'left':
            bot.send_message(update.message.chat.id,"برای استفاده از ربات لطفا در کانال زیز عضو شوید و مجددا روی /start کلیک کنید\n @jok_khone")
        else:
            keyboards = [
                ['🔗کوتاه کردن لینک🔗', '🖱تعداد کلیک لینک🖱'],
                ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
            ]
            reply_markup=ReplyKeyboardMarkup(keyboards,  one_time_keyboard=True)
            update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید",reply_markup=reply_markup)
            del keyboards
            del reply_markup
            del b
            return MODE
    except Exception as ex:
        print(str(ex))


def buttons(bot, update):
    if update.message.text=='🔗کوتاه کردن لینک🔗':
        keyboard = [
            [InlineKeyboardButton('توقف', callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('لطفا لینک خود را وارد کنید.', reply_markup=reply_markup)
        del keyboard
        del reply_markup
        return LINK
    elif update.message.text=='🖱تعداد کلیک لینک🖱':
        keyboard = [
            [InlineKeyboardButton('توقف', callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('لطفا لینک کوتاهی که از ربات دریافت کرده اید وارد کنید.', reply_markup=reply_markup)
        del keyboard
        del reply_markup
        return CLICK
    elif update.message.text == '🤖دیگر ربات های ما🤖':
        keyboard = [
            [InlineKeyboardButton('ربات متن جادویی', url='https://t.me/magic_txt_bot')],
            [InlineKeyboardButton('ربات دانلود از اینستاگرام', url='https://t.me/insta_down_load_bot')],
            [InlineKeyboardButton('ربات دانلود از یوتیوب', url='https://t.me/youtube_down_load_bot')],
            [InlineKeyboardButton('ربات مترجم فارسی', url='https://t.me/fatranslator_bot')],
            [InlineKeyboardButton('ربات آب و هوا فارسی', url='https://t.me/weather_persian_bot')],
            [InlineKeyboardButton('توقف', callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('ربات های ما', reply_markup=reply_markup)
        del keyboard
        del reply_markup
        return ROBOTS
    elif update.message.text == '🥁تبلیغات🥁':
        keyboard = [
            [InlineKeyboardButton('ارتباط با مدیر', url='https://t.me/ashoj79')],
            [InlineKeyboardButton('توقف', callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('برای تبلیغات با مدیر ارتباط برقرار کنید', reply_markup=reply_markup)
        del keyboard
        del reply_markup
        return ROBOTS


def short_link(bot,update):
    if 'http' in update.message.text:
        minified = bitly.shorturl(update.message.text)['url']
        update.message.reply_text(minified)
        keyboards = [
            ['🔗کوتاه کردن لینک🔗', '🖱تعداد کلیک لینک🖱'],
            ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
        update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
        del keyboards
        del reply_markup
        return MODE
    else:
        keyboard = [
            [InlineKeyboardButton('توقف', callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('لطفا لینک خود را با فرمت زیر وارد کنید.\nhttp://www.domain.com/xxx', reply_markup=reply_markup)
        del keyboard
        del reply_markup


def clicks(bot,update):
    if 'https://' in update.message.text:
        c=bitly.link_clicks(update.message.text)
        try:
            cl=c['link_clicks']
            update.message.reply_text('تعداد کلیک لینک شما: '+str(cl))
            keyboards = [
                ['🔗کوتاه کردن لینک🔗', '🖱تعداد کلیک لینک🖱'],
                ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
            ]
            reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
            update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
            del keyboards
            del reply_markup
            return MODE
        except:
            update.message.reply_text('لینک وارد شده صحیح نمی باشد یا لینک از این ربات دریافت نشده است')
            keyboards = [
                ['🔗کوتاه کردن لینک🔗', '🖱تعداد کلیک لینک🖱'],
                ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
            ]
            reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
            update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
            del keyboards
            del reply_markup
            return MODE
    else:
        update.message.reply_text('لینک وارد شده صحیح نمی باشد. لطفا لینک را با فرمت زیر وارد کنید\nhttps://bit.ly/xxx')


def cancel_button(bot, update):
    if update.callback_query.data=='cancel':
        keyboards = [
            ['🔗کوتاه کردن لینک🔗', '🖱تعداد کلیک لینک🖱'],
            ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
        update.callback_query.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
        del keyboards
        del reply_markup
        return MODE


def error(update,context):
    print('error: '+context.error)
    keyboards = [
        ['🔗کوتاه کردن لینک🔗', '🖱تعداد کلیک لینک🖱'],
        ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    del keyboards
    del reply_markup
    return MODE


def cancel(bot, update):
    update.message.reply_text("عملیات متوقف شد", reply_text=ReplyKeyboardRemove())
    keyboards = [
        ['🔗کوتاه کردن لینک🔗', '🖱تعداد کلیک لینک🖱'],
        ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    del keyboards
    del reply_markup
    return MODE

conv_handler=ConversationHandler(
    entry_points=[CommandHandler('start',start_command)],
    states={
        MODE:[MessageHandler(Filters.regex('^(🔗کوتاه کردن لینک🔗)$'),buttons),
              MessageHandler(Filters.regex('^(🖱تعداد کلیک لینک🖱)$'),buttons),
              MessageHandler(Filters.regex('^(🥁تبلیغات🥁)$'),buttons),
              MessageHandler(Filters.regex('^(🤖دیگر ربات های ما🤖)$'),buttons)],
        LINK:[MessageHandler(Filters.text,short_link),
              CallbackQueryHandler(cancel_button)],
        CLICK:[MessageHandler(Filters.text,clicks),
               CallbackQueryHandler(cancel_button)],
        ROBOTS:[CallbackQueryHandler(cancel_button)]
    },
    fallbacks=[CommandHandler('cancel',cancel)]
)

dp=updater.dispatcher

dp.add_handler(conv_handler)

updater.start_polling()

updater.idle()