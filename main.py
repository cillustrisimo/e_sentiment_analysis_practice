import streamlit as st
import plotly.express as px
import glob
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer

# Creating a dicitionary that contains the values I need to plot
files = glob.glob("sample_diary/*.txt")
analyzer = SentimentIntensityAnalyzer()

print(files)

d = {}
d_cleaned = {}
for file in files:
    with open(file, "r") as new_files:
        text = new_files.read()
        d[file] = text.lower().strip("\n")
        filename = Path(file).stem
        d_cleaned[filename] = d[file]

print(d_cleaned)

neg = {}
pos = {}

for key, value in d_cleaned.items():
    print(key)
    scores = analyzer.polarity_scores(value)
    print(scores)
    neg[key] = scores['neg']
    pos[key] = scores['pos']

neg_keys = neg.keys()
neg_values = neg.values()
pos_keys = pos.keys()
pos_values = pos.values()

# Creating the website
st.title("Diary Tone and Sentiment Analysis")

st.subheader("Positivity in each entry")

figure = px.line(x=pos_keys, y=pos_values, labels={"x": "Dates", "y": "Positivity Quotient"})
st.plotly_chart(figure)

st.subheader("Negativity in each entry")
figure_two = px.line(x=neg_keys, y=neg_values, labels={"x": "Dates", "y": "Negativity Quotient"})
st.plotly_chart(figure_two)