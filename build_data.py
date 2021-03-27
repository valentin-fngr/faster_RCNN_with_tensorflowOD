import os 
from config.config import (
    XMLS_PATH, CLASSES_FILE, CLASSES, TEST_SIZE, TRAIN_RECORD, TEST_RECORD
)
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split


def main(): 
    
    with open(CLASSES_FILE, "w") as f: 

        # loop over clases 
        for k, v in CLASSES.items(): 
            item = (" item {\n"
                "\tid : " + str(v) + "\n"
                "\tname : '" + str(k) + "'\n"
                "}\n")
            f.write(item)

    # data 
    D = {}
    
    # read xmls
    for filename in os.listdir(XMLS_PATH): 
        file_path = os.path.join(XMLS_PATH, filename)
        with open(file_path, "r") as f: 
            s = f.read()
            bs = BeautifulSoup(s)
            image_name = bs.annotation.filename.contents[0]
            print(image_name)
            label = bs.object.contents[0].findAll(text=True)[0]
            label = str.upper(label)
            bbox_infos = bs.bndbox.contents
            xmin = float(bbox_infos[0].findAll(text=True)[0])
            ymin = float(bbox_infos[1].findAll(text=True)[0])
            xmax = float(bbox_infos[2].findAll(text=True)[0])
            ymax = float(bbox_infos[3].findAll(text=True)[0])
            
            image_path = os.path.join(IMAGE_PATH, image_name)
            # get the value
            image_infos = D.get(image_path, []) 

            img_infos.append([label, [xmin, ymin, xmax, ymax]])
            D[image_path] = image_infos

    # train test split
    trainKeys, testKeys = train_test_split(list(D.keys()), shuffle=True, random_state=42, test_size=TEST_SIZE)

    # seperate dataset 
    datasets = [
        ("train", trainKeys, TRAIN_RECORD), 
        ("test", testKeys, TEST_RECORD)
    ]


main()