import urllib.request
import json
import os
import ssl
import streamlit as st
import pandas as pd
import json
import pickle

import pickle
model = pickle.load(open("/content/drive/MyDrive/Herramientas3/model.pkl","rb"))

data = {
        "age": 22,
        "job": "technician",
        "marital": "married",
        "education": "high.school",
        "default": "no",
        "housing": "no",
        "loan": "yes",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "duration": 0,
        "campaign": 1,
        "pdays": 0,
        "previous": 0,
        "poutcome": "failure",
        "emp.var.rate": -3.40,
        "cons.price.idx": 92.20,
        "cons.conf.idx": -50.80,
        "nr.employed": 4936.60
      }

df = pd.json_normalize(data)

model.predict(df)

st.write(model.predict(df))
