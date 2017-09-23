from algoliasearch import algoliasearch
import json as json

client = algoliasearch.Client("2RM7K3RK64","cfe617d580262b07179aa986c957b645")

index = client.init_index("contacts")
batch = json.load(open('contacts.json'))
index.add_objects(batch)

index.set_settings({"customRanking":["desc(followers)"]})

index.set_settings({"searchableAttributes": ["lastname", "firstname"]})

#"company","email", "city", "address"]})
