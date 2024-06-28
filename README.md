# Movie Recommendation System

This project is a movie recommendation system that uses user ratings to recommend movies. It provides two types of recommendations: user-based and item-based, using either Euclidean distance or Pearson correlation for similarity calculations.

## Core Functionalities

  -  User-based Recommendations: Recommends movies based on the similarity between users.
  -  Item-based Recommendations: Recommends movies based on the similarity between items (movies).
 -   Data Handling: Reads user, movie, and rating data from CSV files.
  -  HTTP Server: Serves user, movie data, and recommendations through a simple HTTP server.
  -  Frontend: Provides a simple web interface to view and create movie recommendations.

### Technologies Used

  -  JavaScript (Node.js): For the server-side logic and controllers.
  -  Python: For handling data and generating recommendations.
  -  Express.js: Web framework for building the server and handling routes.
 -   EJS: Embedded JavaScript templating for rendering dynamic HTML pages.
  -  fetch: For making HTTP requests.
  -  pandas: For data manipulation in Python.
  -  http.server: For creating a simple HTTP server in Python.

## Project Structure

  1.  /src/controllers/
      -  controller.js: Handles the logic for showing and creating movie recommendations.
  2.  /src/python/
      -  server.py: Python server for handling requests and generating recommendations.
      -  functions/: Contains Python scripts for calculating recommendations.
          -  euclidean_distance.py: Calculates Euclidean distance for recommendations.
         -   item_based.py: Generates item-based recommendations.
          -  movie_data.py: Handles movie data reading and processing.
          -  recommendation.py: Generates user-based recommendations.
  3.  /src/routes/
      -  router.js: Defines the routes for the application.
  4.  /src/views/
     -   home.ejs: EJS template for the home page, showing recommendations.
 5.   /src/server.js: Main server file for the Node.js application.

## Setup

  1. Clone the repository:

2. Install Node.js dependencies:

    - npm install

3. Install Python dependencies:

    - pip install pandas

4. Set up environment variables in a .env file.

5. Start the Python server:

    - python src/python/server.py

6. Start the Node.js server:

    -  npm start

## Usage

1.  Run the Python server to handle data and generate recommendations.
2.  Run the Node.js server to serve the frontend and handle user interactions.
3.  Open your browser and navigate to http://localhost:3000.
4.  Select your user and method, then get movie recommendations.

## Dependencies

-  Node.js: Ensure you have Node.js installed on your system.
-  Express.js: Web framework for Node.js.
-  EJS: Templating engine for generating HTML views.
-  pandas: Python library for data manipulation.
-  fetch: For making HTTP requests in Node.js.

## License

This project is licensed under the MIT License.
