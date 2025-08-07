import pandas as pd
import gradio as gr
import pickle
from sklearn.metrics.pairwise import cosine_similarity # type: ignore
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore

# Load anime dataset (update the path as needed)
anime_df = pd.read_csv("anime.csv")  # Assumes anime.csv is in the same folder

# Placeholder recommendation function
def your_recommendation_function(user_input):
    # Example: return top 1 anime title containing the user input
    matches = anime_df[anime_df['name'].str.contains(user_input, case=False, na=False)]
    if not matches.empty:
        return f"Recommended: {matches.iloc[0]['name']}"
    else:
        return "No recommendations found."

# Create Gradio interface
demo = gr.Interface(fn=your_recommendation_function, inputs="text", outputs="text")
demo.launch()
