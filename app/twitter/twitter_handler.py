import webapp2
from ferris3 import settings
from twitter import Twitter, OAuth

config = settings.get("twitter")


class TwitterHandler(webapp2.RequestHandler):
    def get(self):
        twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], settings["consumer_secret"]))
        results = twitter.trends.place(_id=1)

        self.response.write("Worldwide Trends")

        for location in results:
            for trend in location["trends"]:
                self.response.write(" - %s" % trend["name"])


# Ferris will automatically discover these routes
# and add them to the WSGI application.
webapp2_routes = [
    webapp2.Route('/twitter', TwitterHandler)
]
