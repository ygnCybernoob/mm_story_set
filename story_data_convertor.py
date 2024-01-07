
import os
import shutil
import json
from datetime import datetime

##### user input data ######
index = 36
category_id= 1
story_url_format = 'https://raw.githubusercontent.com/ygncybernoob/mm_story_set/main/stories/{0}'
cover_url_format = 'https://raw.githubusercontent.com/ygncybernoob/mm_story_set/main/story_covers/{0}'
upload_date = datetime.now().date()
writer = "မင်းသုဝဏ်"

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
    new_name = 'story_{0}'.format(index) + '.md'
    
    ##end process

    current_file_path = os.path.join(unprocess_path, unprocess_file)
    new_file_path =   os.path.join(complete_file_path, new_name)
    shutil.copy(current_file_path, new_file_path)

    story_list.append(
        {
            "id": index,
            "category_id": category_id,
            "title": file_name,
            "cover_image_url": "",
            "story_url": story_url_format.format(new_name),
            "writer": writer,
            "moral": "",
            "upload_date": str(upload_date),
        }
    )

    index += 1 #increase it

with open('json_file.json', 'w', encoding='utf8') as f:
    json_string = json.dumps(story_list, ensure_ascii=False)
    f.write(json_string)

print("Data Covert Successfully!")
