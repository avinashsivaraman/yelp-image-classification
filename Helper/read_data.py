# helper file to read data
import pandas as pd
import os
import pickle

objects = []
with (open("C:/Projects/SML project/flatten_features/feat_label_map", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

names = []
for filename in os.listdir("C:/Projects/SML project/flatten_features/flatten_features"):
    names.append(filename)
    
names.sort()

data = []
for name in names:
    file = open("C:/Projects/SML project/flatten_features/flatten_features/"+name, "rb")
    data.append(pickle.load(file))
    break;
















