import json
import os

file_path = r'C:\Users\Admin\Documents\Work\XtraCut_Works\Publisher-Portal-scrapping-v1\Data\ExtractedData\extracted_data.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_summary(obj, prefix=''):
    summary = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, list):
                summary[prefix + k] = f"List with {len(v)} items"
            elif isinstance(v, dict):
                child_summary = get_summary(v, prefix + k + '.')
                summary.update(child_summary)
            else:
                summary[prefix + k] = "Value"
    return summary

print(f"Top level keys: {list(data.keys())}")
print(f"Total top-level keys: {len(data)}")

# Count non-empty sections
non_empty = [k for k, v in data.items() if v and v != {} and v != []]
print(f"Non-empty sections: {len(non_empty)}")
for k in non_empty:
    val = data[k]
    if isinstance(val, (list, dict)):
        print(f" - {k}: {len(val)} items/keys")
    else:
        print(f" - {k}: (single value)")
