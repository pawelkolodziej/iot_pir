# https://www.rototron.info/dht22-tutorial-for-raspberry-pi/
import time
import datetime
import os
import urllib
from pyfcm import FCMNotification

# gloabl variables
ts = None
st = None
THINGS_PEAK_API_KEY = "K4IFY5XAYK4NHDZK"
#FCM
push_service = FCMNotification(api_key="AAAAjVs6fnk:APA91bEbakG5CYynZsP2DtYNPPYKAvNMVnjMFf2eyvWrTwn0lGd7dptzs0TwP7Fm0mtct_v2rdkmx_vyX57HMy57CwwDqUF2n_yHPOr0Sw8KOTiKNCcwAIvxfumBUgHa6LAdgEBaiK5D")
registration_id = "eHZgHLdQJ24:APA91bEk8-JwSocNqiMSFJP04r5QHEfQA5MmGCDVZRVSukckzz2ZCVGOaS4kFZK18oSUZq28Fl6diRsDpxVz0tyOezH_A7_YLP5ZFMgF8NvPaY7KLIfeeos0L3NHcoR_GzAwTStriEWd"

# get current Date and Time
def getCurrentDateAndTime():
    global ts, st
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


# send it to thingspeak.com
def sendToThingsPeak():
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % THINGS_PEAK_API_KEY
    f = urllib.urlopen(baseURL + "&field3=1")


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
        fo.write('Motion detected!')

def sendNotoficationMotion():
    message_title = "Alert"
    message_body = "Wykryto ruch"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
