import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# import tkinter as tk
# from tkinter import filedialog

# Open file dialog (Removed tkinter as it causes issues in Colab)
# root = tk.Tk()
# root.withdraw()

# file_path = filedialog.askopenfilename(
#     title="Select Movies Dataset",
#     filetypes=[("CSV files", "*.csv")]
# )

# Directly specify the file path
file_path = "moviesdata.csv"

print("File Loaded From:", file_path)

# Load dataset
data = pd.read_csv(file_path)
print("\nDataset Preview:")
print(data.head())

# Convert genres to numeric vectors
cv = CountVectorizer()
count_matrix = cv.fit_transform(data["genre"])

# Calculate similarity
cosine_sim = cosine_similarity(count_matrix)

# Recommendation function
def recommend_movie(movie_name):
    if movie_name not in data["title"].values:
        print("Movie not found ❌")
        return
    index = data[data["title"] == movie_name].index[0]
    scores = list(enumerate(cosine_sim[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\n🎬 Recommended Movies for {movie_name}:\n")
    for i in sorted_scores[1:6]:
        print(data.iloc[i[0]]["title"])

# Run the system
movie = input("\nEnter a movie name: ")
recommend_movie(movie)
