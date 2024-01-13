
import os
import json
from datetime import datetime

##### user input data ######
id_index = 37
category_id= 2
upload_date = datetime.now().date()
writer = "အရှင်စက္ကိန္ဒ"

############################
story_list = []


unprocess_path = './unprocess/'
complete_file_path = './stories/'

file_set = os.listdir(unprocess_path)

for unprocess_file in file_set:
    
    ##file name prcoess
    file_name_lst = unprocess_file.split('.')
    if len(file_name_lst)>1: file_name_lst.pop()

    file_name = "".join(file_name_lst)
    
    ##end process

    current_file_path = os.path.join(unprocess_path, unprocess_file)
    with open(current_file_path, 'r', encoding='utf8') as f:

        story_list.append(
            {
                "id": id_index,
                "category_id": category_id,
                "title": file_name,
                "cover_image_url": "https://raw.githubusercontent.com/ygncybernoob/mm_story_set/main/story_covers/cover.jpg",
                "story": f.read(),
                "writer": writer,
                "moral": "",
                "upload_date": str(upload_date),
            }
        )

    id_index += 1 #increase it

with open('json_file.json', 'w', encoding='utf8') as f:
    json_string = json.dumps(story_list, ensure_ascii=False)
    f.write(json_string)

print("Data Covert Successfully!")
