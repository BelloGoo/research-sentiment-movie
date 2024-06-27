import json

# Specify the file path
file_path = r'study\syn_emo_review_20240205.json'

# Read data from the JSON file
try:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")



# Assuming 'data' contains the JSON data you provided
# data = [
#     {"w1_SN": 2687, "w1_chi": "\u9084", "w1_eng": "Still", "w1_tag": "d", "w2_SN": 3827, "w2_chi": "\u7167\u7247", "w2_eng": "Photo", "w2_tag": "n", "sim": 0.9411764705882353},
#     {"w1_SN": 515, "w1_chi": "\u6700", "w1_eng": "Most", "w1_tag": "d", "w2_SN": 2211, "w2_chi": "\u6700\u591a", "w2_eng": "Most", "w2_tag": "d", "sim": 1.0},
#     {"w1_SN": 754, "w1_chi": "\u7247\u5b50", "w1_eng": "Film", "w1_tag": "n", "w2_SN": 1820, "w2_chi": "\u5f71\u7247", "w2_eng": "Movie", "w2_tag": "n", "sim": 1.0},
#     {"w1_SN": 754, "w1_chi": "\u7247\u5b50", "w1_eng": "Film", "w1_tag": "n", "w2_SN": 1751, "w2_chi": "\u6b4c\u821e", "w2_eng": "Musical", "w2_tag": "n", "sim": 0.9411764705882353},
#     {"w1_SN": 754, "w1_chi": "\u7247\u5b50", "w1_eng": "Film", "w1_tag": "n", "w2_SN": 958, "w2_chi": "\u897f\u90e8\u7247", "w2_eng": "Western", "w2_tag": "n", "sim": 0.8888888888888888}
# ]

# Extract 'w1_eng' from each dictionary
w1_eng_values = [entry["w1_eng"] for entry in data]

# Print the extracted values
# print(w1_eng_values)
unique_w1_eng_values = list(set(w1_eng_values))
print(unique_w1_eng_values)  # Print the unique values
print(len(unique_w1_eng_values))  # Print the number of unique values