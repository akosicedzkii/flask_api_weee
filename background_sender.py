import stomp
import time
import send_email
import logging
import json

class SampleListener(object):
  def on_message(self, headers, msg):
    print(msg)
    message = json.loads(msg)
    send_email.send_message(message["message"],message["subject"])
    
    
while True: 
    conn = stomp.Connection10()
    
    conn.set_listener('SampleListener', SampleListener())
    
    conn.start()
    
    conn.connect()
    
    conn.subscribe('emailer')
    
    time.sleep(1) # secs
    
    conn.disconnect()
# conn = stomp.Connection10()
    
# conn.set_listener('SampleListener', SampleListener())

# conn.start()

# conn.connect()

# conn.subscribe('emailer')

# time.sleep(1) # secs

# conn.disconnect()