from protorpc import messages
from google.appengine.ext import ndb
from ferris3 import Model, Service, hvild, auto_service, auto_method
import ferris3 as f3
from twitter import Twitter, OAuth


class TwitterMessage(messages.Message):
    topics = messages.StringField(1)


@auto_service
class TwittersService(Service):

    @auto_method(returns=TwitterMessage)
    def get(self, request):
        config = {}
        execfile("config.py", config)
        twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
        results = twitter.trends.place(_id=1)
        return TwitterMessage(topics=results)
