import json

file_path = r'C:\Users\Admin\Documents\Work\XtraCut_Works\Publisher-Portal-scrapping-v1\Data\ExtractedData\extracted_data.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

child_data = data.get('childPageData', {})
print(f"Keys in childPageData: {list(child_data.keys())}")

# Check if there are lists inside it
for k, v in child_data.items():
    if isinstance(v, list) and len(v) > 0:
        print(f" - {k}: {len(v)} items")
    elif isinstance(v, dict) and len(v) > 0:
        print(f" - {k}: {len(v)} keys")
