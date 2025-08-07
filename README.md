# Anime Recommendation System using Content-Based Filtering

This project implements a content-based recommendation engine for anime, built using Python and NLP techniques. It suggests similar anime titles based on the selected anime’s genres and descriptions by using TF-IDF vectorization and cosine similarity.

---

## 📂 Datasets

- `anime.csv`: Anime metadata (title, genre, type, rating, etc.)
- `rating.csv`: User ratings for anime

> 📥 Datasets loaded from Google Drive

---

## 🔧 Technologies Used

| Category       | Tools & Libraries                  |
|----------------|------------------------------------|
| Programming    | Python                             |
| Data Handling  | Pandas                             |
| NLP/ML         | Scikit-learn (TF-IDF, Cosine Sim)  |
| Visualization  | Matplotlib, Seaborn                |
| Notebook       | Google Colab                       |

---

## 🧠 How It Works

1. **Preprocessing**  
   - Cleans missing values from both datasets  
   - Parses genres as lists for similarity computation

2. **Feature Extraction**  
   - Uses TF-IDF to vectorize genres or descriptions  
   - Computes cosine similarity between anime vectors

3. **Recommendation Engine**  
   - Takes an anime name as input  
   - Finds top N similar anime based on cosine similarity scores

## 📊 Output Example
Input: Naruto
Recommendations: Bleach, One Piece, Fairy Tail, etc.

## 🚀 Run It Yourself
Open in Google Colab: [Colab Link Here](https://colab.research.google.com/drive/159bnTYQmhVi7hwF1moTNfX6f2r11XP1V?usp=sharing)

## 📎 How to Use
1. Upload your anime dataset
2. Run the notebook step by step
3. Use the recommendation cell to get similar anime

## 👨‍💻 Author - Shrikant Bawankule



