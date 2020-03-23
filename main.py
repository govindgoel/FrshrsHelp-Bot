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
            if get_message_text(update).lower() == "/start":
                send_message(get_chat_id(update),'Hello I can help you with following:\n 1. Type mess - To get mess timings \n 2. Type hostel - To get hostel timings \n 3. Type clubs - To get details of various clubs in college \n 4. Type hospital - To get hospital timings \n 5.Type car - To get car pool office details \n 6.Type stay - To get accomodation details in ashram \n 7.Type atm - To get ATM facility details  \n 🛠 Developed And Maintined By:Govind Goel')
            elif get_message_text(update).lower() == "mess":
<<<<<<< HEAD
                send_message(get_chat_id(update), 'Sahaydri Mess: Breakfast 7:15 to 8:15 \n Lunch 12:15 to 13:15 \n Dinner: 20:15 to 21:15')
            elif get_message_text(update).lower() == "car":
                send_message(get_chat_id(update), 'Car Pool office is just after the Kripa hospital \n Contact No: To be Updated')
            elif get_message_text(update).lower() == "hospital":
                send_message(get_chat_id(update), 'Amrita Kripa Hospital')
            elif get_message_text(update).lower() == "hostel":
                send_message(get_chat_id(update), 'Boys Hostel: \n Gate Opening Time: 5:00 A.M \n Gate Closing Time: 9:30 P.M \n Same for all first year boys hostels \n Girls Hostel: \n Gate Opening Time:   \n Gate Closing Time: ')
            elif get_message_text(update).lower() == "clubs":
                send_message(get_chat_id(update), '1. amFOSS: Free and Open Source Club of our college, more info@https://amfoss.in \n 2. bi0s: Cybersecurity club of our college, more info@https://bi0s.in \n 3. HuT Labs: HuT Labs is an engineering research lab using robotics for social cause, more info@https://www.amrita.edu/center/hut-labs ')
            elif get_message_text(update).lower() == "stay":
                send_message(get_chat_id(update), 'Accompanying person with the student can easily get accomodation in ashram, office is just in the entrance of the ashram')
            elif get_message_text(update).lower() == "atm":
                send_message(get_chat_id(update), 'Dhanlaxmi bank ATM is present on the way of you take left just before the Indian accomodation office ')

=======
                send_message(get_chat_id(update), 'Sahaydri Mess: Breakfast 7:15 to 8:15 Lunch 12:15 to 13:15')
            elif get_message_text(update).lower() == "car pool":
                send_message(get_chat_id(update), 'Car Pool office is just after the Kripa hospital Contact No:94XXXXXXXX')
>>>>>>> 8b09c72fa72aa19be5e0797d2582efc42cf52aed
            else:
                send_message(get_chat_id(update), "I did not get you:(")
            update_id += 1

main()
