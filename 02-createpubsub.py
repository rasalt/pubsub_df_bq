from google.cloud import pubsub_v1
import os
project_id =  os.environ["PROJECT_ID"]
topic_name = os.environ["topic"]
# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

topic = publisher.create_topic(topic_path)

print('Topic created: {}'.format(topic))
