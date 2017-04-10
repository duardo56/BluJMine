from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'Hz4hQYkP34Qpv1XqBhs5xLzrQ'
csecret = 'Chd3tgD5VxsXDVbGjNFYLeR8YTNE6nnlHXehn6X0U89M2szFFN'
atoken = '838993675552239616-H0oj90kNPkcErxmLZ7E5Q4xQT0Up2kj'
asecret = '7tgeJCI2BUzs6UyxpuEg8y9cWkegKJEcoWLg40NEnl1UH'

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