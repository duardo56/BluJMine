import json
import pandas as pd
import matplotlib.pyplot as plt

#Reading Tweets
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

#Structuring Tweets
print('Structuring Tweets\n')
tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet.get('text', None),tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))

tweets_by_languages = tweets['lang']
print(*tweets_by_languages)
sorted(tweets_by_languages)
saveFile = open('data.txt', 'w')
for i in tweets_by_languages:
    saveFile.write(i)
    saveFile.write('\n')
saveFile.close()

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
plt.show('tweet_by_lang')
plt.savefig('tweet_by_lang.png')

#Analyzing Tweets by Country
print('Analyzing tweets by country\n')
tweets_by_country = tweets['country'].value_counts()
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 Countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
plt.show('tweet_by_country')
plt.savefig('tweet_by_country.png')

