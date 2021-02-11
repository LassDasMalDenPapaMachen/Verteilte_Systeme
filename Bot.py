import requests
import json
import telegram
from telegram.ext import Updater, CommandHandler
from flask import Flask, jsonify

def create_flask_app():
    app = Flask(__name__)

    @app.route("/") #URL des Services
    def index():
        return jsonify(Inzidenz = request_data())
    app.run()

def show_data(update, context):
    """show_data to the user."""
    update.message.reply_text(request_data())

def request_data():
    tmp = requests.get('https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Coronaf%C3%A4lle_in_den_Bundesl%C3%A4ndern/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json')
    data = json.loads(tmp.text)
    #print(json.dumps(data, indent=2))
    # for feature in data["features"]: 
    #    print(feature["attributes"]["cases7_bl_per_100k_txt"])

    return data["features"][0]["attributes"]["cases7_bl_per_100k_txt"]

def main():
    updater = Updater("BOT-TOKEN")
 # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("show_data", show_data))

    # on noncommand i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, show_data))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
    create_flask_app()