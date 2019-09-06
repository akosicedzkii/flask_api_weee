import time
import sys
import json
import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

def queue_message(message,subject):
    conn = stomp.Connection()
    conn.set_listener('', MyListener())
    conn.start()
    conn.connect('user', 'user', wait=True)

    #conn.subscribe(destination='/queue/test', id=1, ack='auto')
    queue = { "message" : message , "subject" : subject }
    conn.send(body=json.dumps(queue), destination='/queue/emailer')

    time.sleep(0.01)
    conn.disconnect()