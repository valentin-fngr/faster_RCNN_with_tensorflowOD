import os

BASE_PATH = "data/OxfordPetDataset"
ANNOT_PATH = os.path.join(BASE_PATH, "annotations")
XMLS_PATH = os.path.join(ANNOT_PATH, "xmls")
IMAGE_PATH = os.path.join(BASE_PATH, "images")

TRAIN_RECORD = os.path.join("records", "training.record")
TEST_RECORD = os.path.join("records", "testing.record")
CLASSES_FILE = os.path.join("records", "classes.pbtxt")

TEST_SIZE = 0.2

CLASSES = {"DOG" : 0, "CAT" : 1}