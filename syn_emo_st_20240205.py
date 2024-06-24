from nltk.corpus import wordnet as wn
from emo_st_phr import st_eng, st_chi, tags, SNs
import json
from copy import deepcopy

def writeJson(new_entry):
    # New data entry

    # Specify the file path
    file_path = r"C:\Users\85270\OneDrive\桌面\Python\study\syn_emo_st_20240205.json"

    # Read existing content from the JSON file
    try:
        with open(file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty list
        existing_data = []

    # Append the new entry to the existing data
    existing_data.append(new_entry)

    # Write the updated data to the JSON file with indentation
    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=2)

    return " - DATA LOGGED - "


THRESHOLD = 0.857

saved_SNs = deepcopy(SNs)
saved_st_eng = deepcopy(st_eng)

for i in range(0,len(saved_SNs)-1):
    
    w1 = saved_st_eng[i]
    w1_SN = saved_SNs[i]
    w1_chi = st_chi[i]
    w1_tag = tags[i]

    print("SN-processing: ", w1_SN, f"[{w1}]")

    for j in range((i+1),(len(saved_st_eng))):

        try:
            w2 =  saved_st_eng[j]
            w2_SN = saved_SNs[j]
            w2_chi = st_chi[j]
            w2_tag = tags[j]
        except IndexError:
            break

        try:
            c1 = wn.synsets(w1)[0]
            c2 = wn.synsets(w2)[0]
            similarity = c1.wup_similarity(c2)
            # print(similarity)
            if similarity >= THRESHOLD:
                data = {
                    "w1_SN":w1_SN,
                    "w1_chi":w1_chi,
                    "w1_eng":w1,
                    "w1_tag":w1_tag,
                    "w2_SN":w2_SN,
                    "w2_chi":w2_chi,
                    "w2_eng":w2,
                    "w2_tag":w2_tag,
                    "sim":similarity,
                }

                print(writeJson(data))

        except:
            continue

    print(f"finished: {w1_SN}|[{w1}]")
    print(f"{i+1}/2849")