from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#enter your keys here
ckey = ''
csecret = ''
atoken = ''
asecret = ''

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):

        try:
            print (data)
            saveFile = open('twitDB.txt', 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException:
            time.sleep(5)

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    #This handles Twitter authetication and the connection to Twitter Streaming API
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, StdOutListener())

    #This line filter Twitter Streams to capture data by the keywords: 'pokemonGO', 'gameofThornes'
    twitterStream.filter(track=["#football", "#basketball", "#soccer"])
