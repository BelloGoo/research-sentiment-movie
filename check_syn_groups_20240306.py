import json


# check synonym groups
review_file_path = r'study\syn_emo_review_20240306.json'
with open(review_file_path, 'r') as review_json_file:
    review_data = json.load(review_json_file)
new_review_data = []
for i in range(len(review_data)):
    if review_data[i][2] > 200:
        new_review_data.append(review_data[i][1])
print("synonym groups (review): ",len(new_review_data))

st_file_path = r'study\syn_emo_st_20240306.json'
with open(st_file_path, 'r') as st_json_file:
    st_data = json.load(st_json_file)
new_st_data = []
for i in range(len(st_data)):
    if st_data[i][2] > 100:
        new_st_data.append(st_data[i][1])
print("synonym groups (st): ",len(new_st_data))
review_set = set(new_review_data)
st_set = set(new_st_data)
intersection_set = review_set & st_set
print("intersection: ",len(intersection_set))
unique_to_review = review_set - st_set
print("unique to review: ",len(unique_to_review))
unique_to_st = st_set - review_set
print("unique to st: ",len(unique_to_st))


# viewing desscritive words for movies
# for i in range(len(new_review_data)):
#     # for j in new_review_data[i][3]:
#     #     print(j)
#     print(new_review_data[i][1])
    
# print(new_review_data)
# print("========================================")
# print(new_st_data)