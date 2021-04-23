from datetime import datetime
import pywhatkit as kit

def notification():
    now = datetime.now()
    hour = int(now.strftime('%H'))
    minutes = int(now.strftime('%M')) + 2

    message = "Your appointment " + "(on this day) " + "has been booked at time " + "(appointment time)" + "."

# Number must be connected from database

    kit.sendwhatmsg("+91", message, hour, minutes)


notification()