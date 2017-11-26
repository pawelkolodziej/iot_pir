# https://www.rototron.info/dht22-tutorial-for-raspberry-pi/
import time
import datetime
import os
import urllib
from pyfcm import FCMNotification

# gloabl variables
ts = None
st = None
THINGS_PEAK_API_KEY = "DALZ4ZCKJ03P9GHY"
#FCM
push_service = FCMNotification(api_key="AIzaSyArSraurFhSQqzh3G_5Av_m6-ZFA6ptxEo")
registration_id = "<device registration_id>"


# get current Date and Time
def getCurrentDateAndTime():
    global ts, st
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


# send it to thingspeak.com
def sendToThingsPeak():
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % THINGS_PEAK_API_KEY
    f = urllib.urlopen(baseURL + "&field3=MOTION_DETECTED")


def printMotion():
    print 'Motion detected!'


def saveToHtml():
    filename = "./pi_motion.html"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, "ab") as fo:
        fo.write(st + 'Motion detected!')

def sendNotoficationMotion():
    message_title = "Alert"
    message_body = "Wykryto ruch"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
