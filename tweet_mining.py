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
tweets1 = pd.DataFrame()
tweets1['hashtags'] = list(map(lambda tweet: tweet['entities']['hashtags'] if tweet['entities'] != None else None, tweets_data))
print(str(tweets1))
target = open('data1.txt', 'w')
target.write(str(tweets1))
target.close()

# #plotting tweets_data
# print('Plotting data')
# poke_tweets = tweets['#pokemonGo'].value_counts()
# gthrone_tweets = tweets['#gameofthornes'].value_counts()

# fig, ax = plt.subplos()
# ax.tick_params(axis='x', labelsize=10)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Category' ,fontsize=15)
# ax.set_ylable('Number of tweets', fontsize=15)
# ax.set_title('popularity', fotnsize=15, fontweight='bold')
# poke_tweets.plot(ax=ax , kind='bar' ,color='blue')
# gthrone_tweets.plot(ax=ax , kind='bar' ,color='blue')
# plt.savefig('twit_pop.png')

