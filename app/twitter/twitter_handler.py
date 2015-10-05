import webapp2
from ferris3 import settings, oauth2, google_apis
from twitter import Twitter, OAuth
import logging

config = settings.get("twitter")


class TwitterHandler(webapp2.RequestHandler):
    def get(self):
        twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
        results = twitter.trends.place(_id=1)

        # credentials = oauth2.build_service_account_credentials(["https://www.googleapis.com/customsearch"])
        # customSearch = google_apis.build("customsearch", "v1", credentials)
        # self.response.write("TRENDS - %s <br/>" % customSearch.cse.list(q='#SomosPuebloValiente') )

        self.response.write("Worldwide Trends <br/>")
        for location in results:
            for trend in location["trends"]:
                self.response.write(" - %s <br/>" % trend["name"])


# Ferris will automatically discover these routes
# and add them to the WSGI application.
webapp2_routes = [
    webapp2.Route('/twitter', TwitterHandler)
]
