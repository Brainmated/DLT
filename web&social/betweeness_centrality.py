import json
import networkx as nx
import pandas as pd

def get_screen_name(user_id, tweets):
    for tweet in tweets:
        if tweet['user']['id_str'] == user_id:
            return tweet['user']['screen_name']
    return None

# Load the tweets from the JSON files
tweets = []
for i in range(3):
    with open(f'tweets.json.{i}', 'r', encoding='utf-8') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                tweets.append(tweet)
            except json.JSONDecodeError as e:
                print(f'Error: {e}. Skipping line...')

print(f'Loaded {len(tweets)} tweets from the JSON files')

# Construct the user-to-user network
G = nx.DiGraph()
for tweet in tweets:
    user_id = tweet['user']['id_str']
    if user_id not in G:
        G.add_node(user_id)
    if 'retweeted_status' in tweet:
        retweet_user_id = tweet['retweeted_status']['user']['id_str']
        if retweet_user_id not in G:
            G.add_node(retweet_user_id)
        G.add_edge(user_id, retweet_user_id)

print(f'Constructed a user-to-user network with {len(G.nodes)} nodes and {len(G.edges)} edges')

#Betweeness centrality from networkx
betweenness = nx.betweenness_centrality(G)

print(f'Calculated the betweenness centrality of {len(betweenness)} nodes')

#Dataframe to print to pd
betweenness_df = pd.DataFrame([(user_id, get_screen_name(user_id, tweets), bc) for user_id, bc in betweenness.items()], columns=["user_id", "screen_name", "betweenness"])

print(f'Created a DataFrame with {len(betweenness_df)} rows')

#sorting in descending order the dataframe
betweenness_df = betweenness_df.sort_values("betweenness", ascending=False)

print(f'Sorted the DataFrame by betweenness centralities')

betweenness_df.to_csv("betweenness.csv", index=False)

print(f'Saved the DataFrame to "betweenness.csv"')

# Get the top-10 central users
top_users = betweenness_df.head(10)
for _, row in top_users.iterrows():
    user_id = row['user_id']
    screen_name = row['screen_name']
    # Characterize the user based on the content of their posts (e.g. using tags)
    tags = []
    for tweet in tweets:
        if tweet['user']['id_str'] == user_id and 'entities' in tweet:
            for entity in tweet['entities']['hashtags']:
                tag = entity['text'].lower()
                if tag not in tags:
                    tags.append(tag)
    print(f'Top user: {screen_name} ({user_id}) - tags: {tags}')

'''
Top user: BBCWorld (742143) - tags: ['newsfromelsewhere', 'timetoact', 'dailycommute', 'berchtesgaden', 'bleachedbeauty', 'bbcworldcup']
Top user: WSJ (3108351) - tags: ['ukraine', 'worldcup']
Top user: Quantanamo (32696158) - tags: []
Top user: BBCSport (265902729) - tags: ['bbctennis', 'qsteaser', 'worldcup', 'brazil2014', 'bbcworldcup']
Top user: guardiannews (788524) - tags: ['indyref']
Top user: guardian (87818409) - tags: ['nomakeupselfie']
Top user: BBCNewsMagazine (14697685) - tags: []
Top user: BBCNews (612473) - tags: ['stonehaven']
Top user: end_svc (2414093978) - tags: ['eutopjobs', 'timetoact']
Top user: Independent (16973333) - tags: ['worldcup2014']
'''
