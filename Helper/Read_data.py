#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:25:51 2019

@author: ajay
"""
import pandas as pd
import os
import pickle

objects = []
with (open("feat_label_map", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

names = []
for filename in os.listdir("flatten_features"):
    names.append(filename)
    
names.sort()

data = []
for name in names:
    file = open("flatten_features/"+name, "rb")
    data.append(pd.DataFrame(pickle.load(file)))
    break;















