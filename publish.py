
import time
import json 
from google.cloud import pubsub_v1
import os
project_id=os.environ["PROJECT_ID"]

topic_name=os.environ["topic"]

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

def callback(message_future):
    # When timeout is unspecified, the exception method waits indefinitely.
    if message_future.exception(timeout=30):
        print('Publishing message on {} threw an Exception {}.'.format(
            topic_name, message_future.exception()))
    else:
        print(message_future.result())

import pandas as pd
from sodapy import Socrata

    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
client = Socrata("data.cityofchicago.org", None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(data.cityofchicago.org,
    #                  MyAppToken,
    #                  userame="user@example.com",
    #                  password="AFakePassword")

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
#while True:
results = client.get("n4j6-wkkf", limit=2000)
for line in results:
    json_string = json.dumps(line)
    print(json_string)
    data = json_string.encode('utf-8')
    message_future = publisher.publish(topic_path, data=data)
    message_future.add_done_callback(callback)
    print('Published message IDs:')
#  time.sleep(600)
