import os
import json
from collections import OrderedDict
#os.listdir를 사용하시면 쉽게 디렉토리 내에 파일들을 접근 가능합니다.
dir_path = "./valid_road_information/label"
file_lst = os.listdir(dir_path)
f_path=[]
file_data = OrderedDict()
file_data["images"]=[]
file_data["categories"]=[]
file_data["annotations"]=[]
id = 0
ann_id=0

#categories = 0
image_info = OrderedDict()
image_info['id'] = 0
image_info['name'] = "traffic_light"
file_data["categories"].append(image_info)

#categories = 1
image_info = OrderedDict()
image_info['id'] = 1
image_info['name'] = "traffic_sign"
file_data["categories"].append(image_info)

# 현재 디렉토리내에 각각의 파일을 출력
for file in file_lst:
    if file.split(".")[1] == 'json':
        filepath = dir_path + '/' + file
        f_path.append(filepath)

for path in f_path:
    with open(path, 'r') as f:
        json_data = json.load(f)

    image_info = OrderedDict()
    image_info['file_name'] = json_data["image"]["filename"]
    image_info['width'] = json_data["image"]["imsize"][0]
    image_info['height'] = json_data["image"]["imsize"][1]
    image_info['id'] = id

    file_data['images'].append(image_info)

    for annotation in json_data["annotation"]:
        annotation_info = OrderedDict()
        if annotation['class'] == 'traffic_light':
             xmin = annotation['box'][0]
             ymin = annotation['box'][1]
             xmax = annotation['box'][2]
             ymax = annotation['box'][3]
             annotation_info['segmentation']=[[]]
             annotation_info["image_id"] = id
             annotation_info["bbox"]=[xmin,ymin,xmax-xmin,ymax-ymin]
             annotation_info["category_id"] = 0
             annotation_info["id"] = ann_id
             annotation_info["area"] = (xmax-xmin)*(ymax-ymin)
             annotation_info["iscrowd"] = 0
             ann_id+=1
             file_data['annotations'].append(annotation_info)

        elif annotation['class']=='traffic_sign':
             xmin = annotation['box'][0]
             ymin = annotation['box'][1]
             xmax = annotation['box'][2]
             ymax = annotation['box'][3]
             annotation_info['segmentation'] = [[]]
             annotation_info["image_id"] = id
             annotation_info["bbox"] = [xmin, ymin, xmax - xmin, ymax - ymin]
             annotation_info["category_id"] = 1
             annotation_info["id"] = ann_id
             annotation_info["area"] = (xmax - xmin) * (ymax - ymin)
             annotation_info["iscrowd"] = 0
             ann_id += 1
             file_data['annotations'].append(annotation_info)

    id=id + 1

file_path = "./valcoco.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(file_data,file,ensure_ascii=False,indent="\t")


#
