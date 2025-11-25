Stock Price Prediction System (AI Project)

This project is a Machine Learning based system that predicts stock closing prices using **Linear Regression**.  
It uses historical stock market data such as **Open, High, Low, and Volume** to predict the **Close price**.

# Features
- Load stock market data from CSV file
- Train Linear Regression model
- Predict stock prices
- Visualize actual vs predicted prices with graph
- Predict future stock price using custom inputs

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## 📂 Project Structure
stock-price-prediction/
│
├── stock_data.csv
├── stock_prediction.py
└── README.md

# How to Run the Project

1. Install required libraries:
```bash
pip install pandas numpy matplotlib scikit-learn
Run the code:

bash
Copy code
python stock_prediction.py

Sample Output (Terminal)

Dataset Loaded Successfully
   Open  High  Low   Close  Volume
0  200   210   195   205    3500000
1  205   212   202   210    3400000


Model Accuracy: 0.89
Predicted Future Stock Price: 207.52

Sample Graph Output
The project displays a graph with:

Blue line → Actual Price

Orange line → Predicted Price


# Movie Recommendation System (AI Project)

This project is a **content-based movie recommender system** built using **Natural Language Processing (NLP)**.  
It recommends movies based on **genre similarity** using **Cosine Similarity**.

---

# Features
- Load movie dataset from CSV
- Convert movie genres into vectors
- Calculate similarity between movies
- Recommend top 5 similar movies

# Technologies Used
- Python
- Pandas
- Scikit-learn (CountVectorizer, Cosine Similarity)


# Project Structure
movie-recommendation-system/
│
├── moviesdata.csv
├── movie_recommender.py
└── README.md



#How to Run the Project

1. Install required libraries:
```bash
pip install pandas scikit-learn
Run the code:

bash
Copy code
python movie_recommender.py

Sample Output (Terminal)
yaml
Copy code
File Loaded From: moviesdata.csv

Dataset Preview:
   title                genre
0  Avatar     Action Adventure
1  Titanic    Romance Drama
2  Avengers   Action Sci-Fi

Enter a movie name: Avatar

Recommended Movies for Avatar:
Avengers
Guardians of the Galaxy
Iron Man
Thor
Justice League

