# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on your selection.

## 📋 Overview

This project implements a movie recommendation system using content-based filtering techniques. It analyzes movie features such as genres, keywords, overview, and languages to find similar movies based on cosine similarity. The user can select a movie from a dropdown menu, and the system will recommend five similar movies with their posters.

## 🚀 Technologies Used

- **Python 3.12**: Core programming language with modern features
- **Streamlit**: For creating the interactive web interface
  - Easy to create data apps with minimal code
  - Built-in components for data visualization
- **Scikit-learn**: For machine learning functionality
  - `CountVectorizer`: To convert text data into numerical features
  - `Cosine Similarity`: To measure similarity between movies
- **Pandas**: For data manipulation and analysis
- **Pickle**: For serializing and deserializing Python objects
  - Used to save and load the pre-computed similarity matrix and movie dataset
- **TMDB API**: To fetch movie posters
- **UV Package Manager**: For dependency management
  - Modern, fast Python package manager and resolver
  - Compatible with pip and virtualenv

## 🛠️ Project Structure

- `Movie_Recommendation_System.ipynb`: Jupyter notebook containing the data preprocessing and model building
- `main.py`: Streamlit application code
- `movie_list.pkl`: Serialized dataframe containing movie information
- `similarity.pkl`: Pre-computed similarity matrix
- `pyproject.toml`: Project dependencies and metadata
- `.python-version`: Python version specification

## 📊 Data Processing Flow

1. **Data Collection**: Downloaded TMDB movie dataset from Kaggle
2. **Data Cleaning**:
   - Filtered to only include released movies
   - Selected top 10,000 popular movies
   - Removed unnecessary columns
3. **Feature Engineering**:
   - Combined text data from multiple columns (overview, genres, keywords, languages)
   - Converted all text to lowercase for consistency
4. **Text Processing**:
   - Used CountVectorizer to convert text to numerical vectors
   - Applied English stop words removal
5. **Similarity Calculation**:
   - Computed cosine similarity matrix between all movies
   - Serialized results for future use
6. **Web Application**:
   - Created a Streamlit interface for user interaction
   - Implemented movie recommendation function

## 🔧 Setup and Installation

### Prerequisites

- Python 3.12
- UV package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd movie-recommendation-system
   ```

2. Install dependencies using UV:
   ```bash
   uv venv
   uv pip install -e .
   ```

3. Run the application:
   ```bash
   streamlit run main.py
   ```

## 📝 Why UV Package Manager?

UV was chosen for this project because:
- **Speed**: Up to 10-100x faster than pip
- **Reliability**: Deterministic dependency resolution
- **Compatibility**: Works with standard Python tools like pip and virtualenv
- **Lockfiles**: Automatic generation of lockfiles for reproducible environments
- **Modern**: Support for modern Python packaging standards

## 🖥️ Usage

1. Launch the application
2. Select a movie from the dropdown menu
3. Click "Show Recommendations"
4. View the five recommended movies with their posters

## 👨‍💻 Author

Hardik Songara

## 📄 License

This project is open source and available under the [MIT License](LICENSE).