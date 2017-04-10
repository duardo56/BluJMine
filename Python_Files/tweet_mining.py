import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
        return False

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
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))

#Adding programming languages columns to the tweets DataFrame
print('Adding programming languages tags to the data\n')
tweets['#football'] = list(tweets['text'].apply(lambda tweet: word_in_text('#football', tweet)))
tweets['#basketball'] = list(tweets['text'].apply(lambda tweet: word_in_text('#basketball', tweet)))
tweets['#soccer'] = list(tweets['text'].apply(lambda tweet: word_in_text('#soccer', tweet)))

print (tweets['#football'].value_counts()[True])
print (tweets['#basketball'].value_counts()[True])
print (tweets['#soccer'].value_counts()[True])

#Analyzing Tweets by Popular Game: First attempt
print('Analyzing tweets by Most Popular Game: First attempt\n')
pop_game = ['#football', '#basketball', '#soccer']
tweets_by_pop_game = [tweets['#football'].value_counts()[True], tweets['#basketball'].value_counts()[True], tweets['#soccer'].value_counts()[True]]

x_pos = list(range(len(pop_game)))
width = 0.4
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_pop_game, width, alpha=1, color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: football vs. basketball vs. soccer  (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.09 * width for p in x_pos])
ax.set_xticklabels(pop_game)
plt.grid()
plt.show('tweet_by_popular_game')
plt.savefig('tweet_by_popular_game.png')