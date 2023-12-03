import pywhatkit as kit
import schedule
import time

# Define the recipient's phone number (with country code, e.g., +1 for the US)
to_phone_number = '+919822441629'

# Define the message you want to send
message = 'Hello, this is an automated WhatsApp message! Generated By Satyam. Please Dont Reply to this Message'

def SendWhatsappMessage():
    # Send the message
    kit.sendwhatmsg(to_phone_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)
    print("WhatsApp Message Sent")

# Schedule the message to be sent every 1 minute
schedule.every(1).minutes.do(SendWhatsappMessage)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
