import json
import pandas as pd
import xlwt
import xlsxwriter
import matplotlib.pyplot as plt
import re
#import cv2

#Q for qoutes
hashtag1Q = "pokemonGO"
hashtag2Q = "gameofThornes"
#for parenthesis 
hashtag1P = 'pokemonGO'
hashtag2P = 'gameofThornes'

# tweets_data = []
# tweet = []
# tweets = pd.DataFrame()

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


# def extractTweets():
#     ckey = 'Hz4hQYkP34Qpv1XqBhs5xLzrQ'
#     csecret = 'Chd3tgD5VxsXDVbGjNFYLeR8YTNE6nnlHXehn6X0U89M2szFFN'
#     atoken = '838993675552239616-H0oj90kNPkcErxmLZ7E5Q4xQT0Up2kj'
#     asecret = '7tgeJCI2BUzs6UyxpuEg8y9cWkegKJEcoWLg40NEnl1UH'
#
#     # This is a basic listener that just prints received tweets to stdout.
#     class StdOutListener(StreamListener):
#
#         def on_data(self, data):
#
#             try:
#                 print (data)
#                 saveFile = open('twitDB.txt', 'a')
#                 saveFile.write(data)
#                 saveFile.write('\n')
#                 saveFile.close()
#                 return True
#             except BaseException:
#                 time.sleep(5)
#
#         def on_error(self, status):
#             print (status)
#
#     if __name__ == '__main__':
#         # This handles Twitter authetication and the connection to Twitter Streaming API
#         auth = OAuthHandler(ckey, csecret)
#         auth.set_access_token(atoken, asecret)
#         twitterStream = Stream(auth, StdOutListener())
#
#         # This line filter Twitter Streams to capture data by the keywords: 'pokemonGO', 'gameofThornes'
#         twitterStream.filter(track=["pokemonGo", "gameofThrones"])


# Reading Tweets



print('Reading Tweets\n')
tweets_data_path = 'twitDB.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
str(tweet)

# Structuring Tweets

print('Structuring Tweets\n')

# tweets1 = pd.DataFrame()
# tweets1['hashtags'] = list(map(lambda tweet: tweet['entities']['hashtags'] if tweet['entities'] != None else None, tweets_data))
# target = open( 'data1.txt', 'w')
# target.write(str(tweets1))
# # # for i in tweets:
# # #     target.write(i)
# target.close()

tweets = pd.DataFrame()

tweets['text'] = list(map(lambda tweet: tweet.get('text', None),tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
# tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))
# tweets['full_name'] = list(map(lambda tweet: tweet['place']['full_name'] if tweet['place'] != None else None, tweets_data))
tweets['friends_count'] = list(
    map(lambda tweet: tweet['user']['friends_count'] if tweet['user'] != None else None, tweets_data))
# tweets['entities'] = list(map(lambda tweet: tweet.get('entities', None),tweets_data))
# tweets['id'] = list(map(lambda tweet: tweet.get('id', None),tweets_data))
# tweets['favorite_count'] = list(map(lambda tweet: tweet.get('favorite_count', None),tweets_data))
# tweets['retweet_count'] = list(map(lambda tweet: tweet.get('retweet_count', None),tweets_data))
# print(str(tweets))

# Write to Excel
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('twitData.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
tweets.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()  # tweets_by_languages = tweets['lang'].value_counts()

# print(tweets_by_languages)
# saveFile = open('data.txt', 'a')
# saveFile.write(tweets_by_languages)
# saveFile.write('\n')
# saveFile.close()
#

#plot by attribute , split by tag 
tweets[hashtag1P] = tweets['text'].apply(lambda tweet: word_in_text(hashtag1P, tweet))
tweets[hashtag2P] = tweets['text'].apply(lambda tweet: word_in_text(hashtag2P, tweet))

print tweets[hashtag1P].value_counts()[True]
print tweets[hashtag2P].value_counts()[True]

prg_langs = [hashtag1P, hashtag2P]
tweets_by_prg_lang = [tweets[hashtag1P].value_counts()[True], tweets[hashtag2P].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')


# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: csGo vs. WoW (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
# plt.grid()
plt.savefig('pVSg.png')

#plot by relevancy 
tweets['gaming'] = tweets['text'].apply(lambda tweet: word_in_text('gaming', tweet))
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('gaming', tweet))
# or word_in_text('tutorial', tweet))
# print tweets['relevant'] == True [hashtag1P].value_counts()[True]
# print pd.value_counts(tweets['relevant'].values, sort=False)
print tweets[tweets.relevant == 'csGo'].value_counts()
print tweets['relevant'][hashtag1P].value_counts()[True]
print tweets[tweets['relevant'] == True][hashtag2P].value_counts()[True]

tweets_by_prg_lang = [tweets[tweets['relevant'] == True][hashtag1P].value_counts()[True],
                      tweets[tweets['relevant'] == True][hashtag2P].value_counts()[True]]
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: csGo vs. WoW (Relevant data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.savefig('pVSg_Relevant.png')




#plot by attribute 
#Analyzing Tweets by Language
print('Analyzing tweets by language\n')
tweets_by_lang = tweets['lang'].value_counts()
fig, ax = plt.subplots()

ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')

tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
plt.savefig('tweet_by_lang.png')
#
# #Analyzing Tweets by Country
# print('Analyzing tweets by country\n')
# tweets_by_country = tweets['country'].value_counts()
# fig, ax = plt.subplots()
# ax.tick_params(axis='x', labelsize=10)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Countries', fontsize=15)
# ax.set_ylabel('Number of tweets' , fontsize=15)
# ax.set_title('Top 5 Countries', fontsize=15, fontweight='bold')
# tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
# plt.savefig('tweet_by_country.png')
