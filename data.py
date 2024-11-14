import json
input_file = "data"
output_file = ""

with open(f'{input_file}.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

#remove unuse key
fields_to_remove = ["id", "title", "author", "picture_count", "processed", "source", "crawled_at", "url"]
for item in data:
    for field in fields_to_remove:
        item.pop(field, None)

#remove empty content and topic
data = [item for item in data if item.get('topic') and item.get('content')]


with open('train_cleandata.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("---------------------- Done ---------------------")
