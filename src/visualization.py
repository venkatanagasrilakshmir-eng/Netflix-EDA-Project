import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Load Dataset
df = pd.read_csv("../data/netflix_titles.csv")

# -----------------------------
# Content Type Distribution
# -----------------------------
plt.figure(figsize=(6, 4))

sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows")
plt.savefig("../images/content_type_distribution.png")
plt.close()

# -----------------------------
# Top Countries
# -----------------------------
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10, 5))

top_countries.plot(kind='bar')

plt.title("Top 10 Countries with Most Content")
plt.xlabel("Country")
plt.ylabel("Count")

plt.savefig("../images/country_analysis.png")
plt.close()

# -----------------------------
# Release Year Trend
# -----------------------------
plt.figure(figsize=(12, 5))

sns.histplot(df['release_year'], bins=30)

plt.title("Content Release Trend")

plt.savefig("../images/release_year_trend.png")
plt.close()

# -----------------------------
# Genre Distribution
# -----------------------------
genres = df['listed_in'].str.split(', ').explode()

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10, 5))

top_genres.plot(kind='bar')

plt.title("Top Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.savefig("../images/genre_distribution.png")
plt.close()

print("Visualizations Saved Successfully")
