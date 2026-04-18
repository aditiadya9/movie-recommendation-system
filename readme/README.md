# 🎬 Movie Recommendation System

## 📌 Project Overview
This project implements a content-based movie recommendation system that suggests similar movies based on multiple features such as genre, rating, release year, and duration. The system uses cosine similarity to identify movies with similar characteristics and provide personalized recommendations.

---

## 🎯 Objective
To build a scalable and intelligent recommendation system that goes beyond basic filtering by leveraging feature engineering and similarity techniques.

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- Scikit-learn  

---

## ⚙️ Features
- Accepts user input for a movie name  
- Handles partial and flexible search queries  
- Recommends top 5 similar movies  
- Uses multiple features for better accuracy  
- Displays results with ratings  

---

## 📊 Data Processing
- Encoded categorical feature (genre) using Label Encoding  
- Normalized numerical features (rating, year, duration) using MinMaxScaler  
- Created a feature matrix for similarity computation  

---

## 🧠 Algorithm Used
**Cosine Similarity (Content-Based Filtering)**  
- Measures similarity between movies based on feature vectors  
- Higher similarity score → more relevant recommendation  

---

## ▶️ How to Run
1. Install dependencies: pip install pandas scikit-learn

2. Run the program: python src/recommend.py

3. Enter a movie name when prompted  

---

## 📈 Results
- Generates top 5 personalized recommendations  
- Improved recommendation quality using multi-feature similarity  
- Provides faster and more relevant suggestions compared to basic filtering  

---

## 🚀 Future Improvements
- Add user-based collaborative filtering  
- Integrate a web interface (Streamlit)  
- Use larger real-world datasets (e.g., IMDb, TMDB)  
- Implement hybrid recommendation systems  

---

## 📂 Project Structure
Movie-Recommendation/
│── data/ # Dataset
│── src/ # Source code
│── insights/ # Project insights
│── README.md # Documentation

---

## ✨ Author Note
This project was developed as part of my learning journey in Data Science and Machine Learning, focusing on building practical and scalable systems.

## 📌 Sample Output

=== Movie Recommendation System ===

You selected: Inception

🔥 Top 5 Recommendations:
• Interstellar ⭐ 8.6
• The Matrix ⭐ 8.7
• Tenet ⭐ 7.5
• Avatar ⭐ 7.9
• Gravity ⭐ 7.7

## 📷 Demo
![Demo](output/demo.png)