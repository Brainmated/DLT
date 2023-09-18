import json
import networkx as nx
import scipy.sparse as sparse

def get_tags(tweet):
    tags = []
    hashtags = tweet['entities']['hashtags']
    for tag in hashtags:
        tags.append(tag['text'])
    return tags

contacts = {}
for i in range(3):
    with open(f'tweets.json.{i}', 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            if "user" in tweet and "id_str" in tweet["user"]:
                user_id = tweet['user']['id_str']
                for mention in tweet['entities']['user_mentions']:
                    contact_id = mention['id_str']
                    if user_id != contact_id:
                        if user_id not in contacts:
                            contacts[user_id] = set()
                        contacts[user_id].add(contact_id)

graph = nx.Graph()
for user_id, contact_ids in contacts.items():
    for contact_id in contact_ids:
        if not graph.has_edge(user_id, contact_id):
            graph.add_edge(user_id, contact_id, weight=1)
        else:
            graph[user_id][contact_id]['weight'] += 1

#Using link prediction with Jaccard, still wont work, receiving error of float to integer reading
scores_jaccard = sparse.lil_matrix((len(graph), len(graph)))
for i, user in enumerate(graph.nodes()):
    for j, potential_contact in enumerate(graph.nodes()):
        if i != j and not graph.has_edge(user, potential_contact):
            neighbors1 = set(graph.neighbors(user))
            neighbors2 = set(graph.neighbors(potential_contact))
		#distinguish common neighbors
            common_neighbors = neighbors1.intersection(neighbors2)
            all_neighbors = neighbors1.union(neighbors2)
            if len(all_neighbors) > 0:
		#adjust the similarity score
                similarity = len(common_neighbors) / len(all_neighbors)
                scores_jaccard[i, j] = similarity

#Need this matrix DONT CHANGE
scores_jaccard_dict = {}
for i, user in enumerate(graph.nodes()):
    scores_jaccard_dict[user] = {}
    for j, potential_contact in enumerate(graph.nodes()):
        if i != j and not graph.has_edge(user, potential_contact):
		#adjusting the jaccard score as the similarity,doesnt work
		print(j)
            similarity = scores_jaccard[i, j]
            if similarity > 0:
                scores_jaccard_dict[user][potential_contact] = similarity
                
                
                
                
                
                
                
