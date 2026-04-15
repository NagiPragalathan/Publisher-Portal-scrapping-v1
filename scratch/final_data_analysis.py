import json
import os

file_path = r'C:\Users\Admin\Documents\Work\XtraCut_Works\Publisher-Portal-scrapping-v1\Data\ExtractedData\extracted_data.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Count Colleges
colleges = []
# Check instituteData
inst_data = data.get('instituteData', {})
if inst_data:
    colleges.extend(list(inst_data.keys()))

# Check childPageData
child_data = data.get('childPageData', {})
inst_name = child_data.get('instituteTopCardData', {}).get('instituteName')
if inst_name:
    colleges.append(inst_name)

# 2. Count Data Points
def count_all_values(obj):
    count = 0
    if isinstance(obj, dict):
        for k, v in obj.items():
            if v and v != {} and v != []:
                count += 1
                count += count_all_values(v)
    elif isinstance(obj, list):
        for item in obj:
            count += 1
            count += count_all_values(item)
    return count

total_data_points = count_all_values(data)

# 3. Analyze sections
sections = []
for k, v in data.items():
    if v and v != {} and v != []:
        sections.append(k)

print(f"Colleges found: {list(set(colleges))}")
print(f"Total Colleges count: {len(set(colleges))}")
print(f"Estimated total data points (nested): {total_data_points}")
print(f"Non-empty main sections: {sections}")

# Detailed breakdown of childPageData
if child_data:
    print("\nBreakdown of Information available at IIT Madras:")
    inst_sections = child_data.get('instituteSectionData', {})
    print(f" - Total Detail Sections: {len(inst_sections)}")
    for s_name in inst_sections.keys():
        print(f"   * {s_name}")
