

```markdown
# Movie Recommender System

## Overview

This project is a Movie Recommender System built using Python and Streamlit. The application allows users to input a movie title and receive recommendations for similar movies. It utilizes a similarity model trained on a dataset of movies and fetches movie posters from Wikipedia to enhance the user experience.

## Features

- **Interactive User Interface:** Users can easily select a movie from a dropdown menu.
- **Movie Recommendations:** The system suggests similar movies based on user input.
- **Movie Posters:** Displays movie posters fetched from Wikipedia for a visually appealing experience.
- **Customizable Background:** Change the application's background to enhance aesthetics.

## Requirements

To run this project, you need to have the following installed:

- Python 3.x
- Streamlit
- FuzzyWuzzy
- Pandas
- NumPy
- Requests
- BeautifulSoup4

You can install the necessary libraries using pip:

```bash
pip install streamlit fuzzywuzzy pandas numpy requests beautifulsoup4
```

## Dataset

This project uses the following datasets:

- **TrainData.pkl:** Pickle file containing the training data for the recommendation model.
- **similarity.pkl:** Pickle file containing the similarity matrix for the movies.
- **movies.csv:** CSV file containing movie titles and IDs.

Make sure to place these files in the `model` and `dataset` folders, respectively.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/movie-recommender-system.git
```

2. Navigate to the project directory:

```bash
cd movie-recommender-system
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open your web browser and go to `http://localhost:8501` to view the application.

## Customization

To change the background image of the application, replace the `bg.png` file in the `static` folder with your desired image.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you encounter any problems.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)
- [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)

```
