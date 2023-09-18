import json
import networkx as nx
import pandas as pd

def get_screen_name(user_id, tweets):
    for tweet in tweets:
        if tweet['user']['id_str'] == user_id:
            return tweet['user']['screen_name']
    return None


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


closeness = nx.closeness_centrality(G)

print(f'Calculated the closeness centrality of {len(closeness)} nodes')

#Dataframe again
closeness_df = pd.DataFrame([(user_id, get_screen_name(user_id, tweets), cc) for user_id, cc in closeness.items()], columns=["user_id", "screen_name", "closeness"])

print(f'Created a DataFrame with {len(closeness_df)} rows')

#Descending order for closeness dataframe
closeness_df = closeness_df.sort_values("closeness", ascending=False)

print(f'Sorted the DataFrame by closeness centralities')


closeness_df.to_csv("closeness.csv", index=False)

print(f'Saved the DataFrame to "closeness.csv"')


top_users = closeness_df.head(10)
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
Top user: None (13) - tags: []
Top user: guardian (87818409) - tags: ['nomakeupselfie']
Top user: WSJ (3108351) - tags: ['ukraine', 'worldcup']
Top user: BBCWorld (742143) - tags: ['newsfromelsewhere', 'timetoact', 'dailycommute', 'berchtesgaden', 'bleachedbeauty', 'bbcworldcup']
Top user: guardiannews (788524) - tags: ['indyref']
Top user: BBCBreaking (5402612) - tags: []
Top user: BBCSport (265902729) - tags: ['bbctennis', 'qsteaser', 'worldcup', 'brazil2014', 'bbcworldcup']
Top user: GlastoFest (18863867) - tags: []
Top user: BBCNews (612473) - tags: ['stonehaven']
'''
Top user: BBCOS (2190056023) - tags: ['worldcup2014']
