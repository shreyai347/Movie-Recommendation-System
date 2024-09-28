
---

# Movie Recommender System

![Screenshot 2024-09-28 072838](https://github.com/user-attachments/assets/00ba7468-2929-4e7a-a5e7-d5b343bad556)
![Screenshot (80)](https://github.com/user-attachments/assets/712143a4-f1d0-44db-a165-9141d19da56f)
![Screenshot 2024-09-28 073053](https://github.com/user-attachments/assets/9eccfa3d-fdfc-40d2-8529-606c4d43c032)


## Overview

The Movie Recommender System is a user-friendly web application built with Streamlit that suggests movies based on user input. Utilizing advanced recommendation algorithms, it offers personalized movie recommendations by analyzing similarities among films in a dataset. The application features a clean interface, dynamic recommendations, and informative movie posters fetched from Wikipedia.

## Features

- **User Input**: Users can type or select a movie from a dropdown menu.
- **Dynamic Recommendations**: Once a movie is selected, the system recommends similar movies based on a trained model.
- **Movie Posters**: Fetches and displays movie posters from Wikipedia, with a fallback option for missing posters.
- **Responsive Design**: The application is designed to provide a seamless experience across different devices.

## Technologies Used

- **Python**: The core programming language.
- **Streamlit**: Framework for building the web application.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **FuzzyWuzzy**: For fuzzy string matching to improve search accuracy.
- **BeautifulSoup**: For web scraping to retrieve movie posters from Wikipedia.
- **Pickle**: For loading pre-trained models and datasets.

## Installation

To set up the Movie Recommender System locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the application in your web browser (default is usually `http://localhost:8501`).
2. Type or select a movie from the dropdown.
3. Click on "Show Recommendation" to get similar movie suggestions.
4. Explore the recommendations and view their posters.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by collaborative filtering techniques for movie recommendations.
- Thanks to the developers of Streamlit and the various libraries used.

---

Feel free to modify any section to better fit your project’s specifics!
