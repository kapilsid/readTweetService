from sqs_listener import SqsListener
from fetchTweets import TwitterQuery

class MyListener(SqsListener):
    def handle_message(self, body, attributes, messages_attributes):
        term1 = body['term1']
        term2 = body['term2']
        api = TwitterQuery()
        tweets1 = api.getTweets(query = term1,mnth=1)
        tweets2 = api.getTweets(query = term2,mnth=1)

        #run_my_function(body['param1'], body['param2'])

listener = MyListener(queue_url='https://sqs.us-east-1.amazonaws.com/521308251176/TweetQueue', error_queue='ErrorQueue', region_name='us-east-1')
listener.listen()