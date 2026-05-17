# Netflix-EDA-Project

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Netflix dataset to uncover insights about movies and TV shows available on Netflix. The analysis helps understand content distribution, trends, and patterns using Python data visualization tools.

## Dataset Information

### The dataset contains information such as:
- **Title** - Name of the content
- **Type** - Movie or TV Show
- **Director** - Director name
- **Cast** - Actors involved
- **Country** - Production country
- **Release Year** - Year the content was released
- **Rating** - Age rating (G, PG, PG-13, R, TV-MA, etc.)
- **Duration** - Runtime for movies or number of seasons for TV shows
- **Genre** - Listed genres

### Dataset Columns:
| Column | Description |
|--------|-------------|
| show_id | Unique ID for each content |
| type | Movie or TV Show |
| title | Name of content |
| director | Director name |
| cast | Actors involved |
| country | Production country |
| date_added | Date added to Netflix |
| release_year | Year released |
| rating | Age rating |
| duration | Duration (minutes for movies, seasons for TV shows) |
| listed_in | Genre/Categories |

## Key Objectives
✓ Analyze Netflix content distribution (Movies vs TV Shows)  
✓ Identify top countries producing content  
✓ Study yearly content growth trends  
✓ Understand most popular genres and ratings  
✓ Compare Movies vs TV Shows characteristics  

## Exploratory Data Analysis (EDA)

### 1. Content Type Distribution
Shows the ratio of Movies vs TV Shows on Netflix with a bar chart visualization.

### 2. Country Analysis
Identifies which countries produce the most Netflix content using a horizontal bar chart of the top 10 countries.

### 3. Release Year Trend
Shows how Netflix content has grown over the years with a line chart displaying content releases by year.

### 4. Rating Distribution
Displays the distribution of content ratings (G, PG, PG-13, R, TV-MA, etc.) using a count plot.

### 5. Duration Analysis
Compares the duration distribution between Movies (in minutes) and TV Shows (in seasons).

## Key Insights
- 📊 Movies are significantly more prevalent than TV Shows on Netflix
- 🌍 United States produces the highest volume of Netflix content
- 📈 Netflix content significantly increased after 2015
- 🎭 Drama and International Movies are the most common genres
- 📺 Most TV Shows run for 1-2 seasons

## Technologies Used
- **Python 3.x** - Programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Static data visualization
- **Seaborn** - Statistical data visualization
- **Jupyter Notebook** - Interactive notebooks

## Visualization Code

### Using the Visualization Script

The `src/visualization.py` script generates comprehensive EDA visualizations automatically.

#### Setup Instructions:

**1. Install Dependencies**
```bash
pip install pandas numpy matplotlib seaborn
```

**2. Prepare Your Data**
- Place your Netflix dataset at `data/netflix_titles.csv`
- Ensure the CSV has the expected columns (title, type, country, release_year, rating, duration, etc.)

**3. Run the Visualization Script**
```bash
python src/visualization.py
```

**4. Output**
All visualizations will be saved to the `images/` folder:
- `content_type_distribution.png` - Bar chart of Movies vs TV Shows
- `release_year_distribution.png` - Line chart of content over years
- `top_countries.png` - Bar chart of top 10 producing countries
- `rating_distribution.png` - Bar chart of content ratings
- `duration_distribution.png` - Histogram of duration distribution

### Visualization Code Features
✨ **Automatic Image Generation** - Creates high-resolution PNG files (300 DPI)  
✨ **Netflix Styled Colors** - Uses Netflix red (#E50914) color scheme  
✨ **Professional Formatting** - Includes titles, labels, and legends  
✨ **Easy Customization** - Simple parameters to modify charts  

### Code Example:
```python
import pandas as pd
from visualization import create_visualizations

# Load your Netflix dataset
df = pd.read_csv('data/netflix_titles.csv')

# Generate all visualizations
create_visualizations(df, output_dir='images')
```

## How to Run This Project

### Option 1: Using the Visualization Script (Recommended)
```bash
# 1. Clone the repository
git clone https://github.com/venkatanagasrilakshmir-eng/Netflix-EDA-Project.git

# 2. Navigate to project directory
cd Netflix-EDA-Project

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# 4. Run visualization script
python src/visualization.py

# 5. Check the 'images' folder for generated visualizations
```

### Option 2: Using Jupyter Notebook
```bash
# 1. Clone the repository
git clone https://github.com/venkatanagasrilakshmir-eng/Netflix-EDA-Project.git

# 2. Navigate to project directory
cd Netflix-EDA-Project

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# 4. Launch Jupyter Notebook
jupyter notebook

# 5. Open and run the notebook files for interactive analysis
```

## Project Structure
```
Netflix-EDA-Project/
├── data/
│   └── netflix_titles.csv          # Netflix dataset
├── src/
│   └── visualization.py            # Main visualization script
├── images/                         # Output folder for generated visualizations
├── notebooks/
│   └── netflix_eda.ipynb          # Interactive Jupyter notebook
└── README.md                       # Project documentation
```

## Sample Visualizations Preview
![Netflix EDA Dashboard](https://github.com/user-attachments/assets/eb709ccb-7a67-4c6b-b8be-02596353763a)

## Key Findings
1. **Content Distribution**: Approximately 70% Movies, 30% TV Shows
2. **Geographic Focus**: USA, India, and UK lead in content production
3. **Growth Trend**: Exponential growth in Netflix content from 2015-2020
4. **Rating Preferences**: TV-MA, PG-13, and R-rated content are most common
5. **Genre Leaders**: Drama, International, and Comedy are top genres

## Contributing
Contributions are welcome! Feel free to:
- Fork the repository
- Create a feature branch
- Submit a pull request with improvements

## License
This project is open source and available for educational purposes.

## Contact & Support
For questions or suggestions, feel free to open an issue on GitHub or contact the repository maintainer.

---
**Last Updated**: May 2026  
**Dataset Source**: Kaggle Netflix Titles Dataset
