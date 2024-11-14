import json

# Load the JSON file
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

[item for item in data if item.get('topic') and item.get('content')]

# Save the modified data back to a JSON file
with open('train_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Fields removed and data saved to 'modified_file.json'.")
