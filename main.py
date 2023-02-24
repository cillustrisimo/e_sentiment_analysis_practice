import streamlit as st
import plotly.express as px
import glob
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer

# Creating a list that contains the values I need to plot
files = glob.glob("sample_diary/*.txt")
analyzer = SentimentIntensityAnalyzer()
print(files)
negativity = []
positivity = []

for file in files:
    with open(file) as open_file:
        content = open_file.read()
    scores = analyzer.polarity_scores(content)
    negativity.append(scores["neg"])
    positivity.append(scores["pos"])

dates = [date.strip(".txt").strip('sample_diary\\') for date in files]

# Creating the website
st.title("Diary Tone and Sentiment Analysis")

st.subheader("Positivity in each entry")

figure = px.line(x=dates, y=positivity, labels={"x": "Dates", "y": "Positivity Quotient"})
st.plotly_chart(figure)

st.subheader("Negativity in each entry")
figure_two = px.line(x=dates, y=negativity, labels={"x": "Dates", "y": "Negativity Quotient"})
st.plotly_chart(figure_two)