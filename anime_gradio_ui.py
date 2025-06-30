import pandas as pd
import gradio as gr
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


# Load anime dataset
anime_df = pd.read_csv("/content/drive/MyDrive/Anime Recommendation/anime.csv")
…  demo.launch()
