import requests as requests

url = "https://api.telegram.org/bot(BOT_TOKEN)/"

# get chat id
def get_chat_id(update):
    chat_id=update['message']["chat"]["id"]
    return chat_id

# get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text

# get last update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]

# bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response

# main function
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            print(update_id)
            print(update)
            if get_message_text(update).lower() == "hi":
                send_message(get_chat_id(update), 'Hello I can help you with following:1.Mess Timings 2.Hostel Timings 3.Various clubs In college 4.Hospital Timings 5.Car Pool')
            elif get_message_text(update).lower() == "mess":
                send_message(get_chat_id(update), 'Sahaydri Mess: Breakfast 7:15 to 8:15 Lunch 12:15 to 13:15')
            elif get_message_text(update).lower() == "car pool":
                send_message(get_chat_id(update), 'Car Pool office is just after the Kripa hospital Contact No:94XXXXXXXX')
            else:
                send_message(get_chat_id(update), "I did not get you:(")
            update_id += 1

main()
