import json
from collections import Counter

# Load the JSON file
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# Count occurrences of each unique 'topic'
topic_counts = Counter(item['topic'] for item in data)
# Write the unique topic counts to a text file





with open('topic.txt', 'w', encoding='utf-8') as file:
    file.write("Unique topics and their counts:\n")
    for topic, count in sorted(topic_counts.items(), key=lambda x: x[1], reverse=True):
        file.write(f"{topic}: {count}\n")

print("Done")
