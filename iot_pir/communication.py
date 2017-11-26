# https://www.rototron.info/dht22-tutorial-for-raspberry-pi/
import time
import datetime
import os
import urllib
import sensor as sensor

# gloabl variables
ts = None
st = None
THINGS_PEAK_API_KEY = "DALZ4ZCKJ03P9GHY"


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