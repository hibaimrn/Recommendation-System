# Alexa Reviews Recommendation System

## Overview

This Flask application utilizes a recommendation system to suggest similar items based on user input. The recommendation algorithm employs TF-IDF (Term Frequency-Inverse Document Frequency) vectorization and cosine similarity to identify items with similar review texts. The system is built using Python and Flask framework.

## How it Works

1. **Data Loading**: The application loads pre-scrapped Alexa reviews dataset (`recommendation_data.csv`).

2. **TF-IDF Vectorization**: Text features are converted into numerical vectors using TF-IDF vectorization.

3. **Cosine Similarity**: Cosine similarities between all items are computed based on the TF-IDF vectors.

4. **Recommendation Generation**: When a user inputs an item ID, the system retrieves the top N similar items based on cosine similarity.

5. **User Interface**: The application provides a user-friendly interface where users can input an item ID and specify the number of recommendations they want.

## Functionality

- **Item Recommendation**: Users can input an item ID and receive recommendations for similar items.
- **Customization**: Users can specify the number of recommendations they want to receive.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository and navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Flask application by executing `python app.py`.
5. Access the application through your web browser at `http://localhost:5000`.
6. Input an item ID and the desired number of recommendations.
7. View the recommended items.

## Dataset

The dataset used in this application contains pre-scrapped Alexa reviews data (`recommendation_data.csv`).

## Credits

- Developed by Hiba Imran.

## Disclaimer

This application is for educational purposes and does not provide real-time or accurate recommendations. The quality of recommendations may vary based on the dataset and algorithm used.

**Made with ❤️ by Hiba Imran**