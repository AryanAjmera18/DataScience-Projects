import streamlit as st
import pandas as pd
import numpy as np
## Title of the application
st.title("Hello StreamLit")

## Display a simple text
st.write("This is a simple text")

## Create a simple dataframe
url ='https://www.cricbuzz.com/cricket-team/india/2/stats'
df = pd.read_html(url)

st.write("here is the data frame")
#st.write(df[0])

# create a line chart

st.dataframe(df[0])
st.write("Top 10 Players by Runs:")
top_players = df[0].sort_values(by="RUNS", ascending=False).head(10)
st.line_chart(top_players[["PLAYER", "RUNS"]].set_index("PLAYER"))