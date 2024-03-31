# Spam Detector with Chat

This project is a simple web application that combines a spam detection model with a chat interface. It utilizes Flask for the backend, SocketIO for real-time communication, and a Naive Bayes classifier for spam detection. The frontend is built with HTML, CSS, and JavaScript.

## Files:

### `app.py`
This file contains the Flask application and handles the web server, routing, and interaction with the spam detection model. It uses the SocketIO library to enable real-time communication between the server and the client.

### `scripts.js`
The JavaScript file contains functions for making predictions using AJAX to communicate with the server. It also updates the chat interface based on the model's predictions.

### `home_with_chat.html`
This HTML file is the main page of the web application. It includes a chat interface, a message input form, and displays the spam detection results in real-time.

### `model training.ipynb`
This Jupyter Notebook file demonstrates the process of training the spam detection model using a Naive Bayes classifier. It involves data preprocessing, model training, evaluation, and model persistence using joblib.

### `styles.css`
The CSS file contains styling rules for the web application, defining the appearance of various elements such as the header, buttons, chat box, and result container.

## Instructions:

1. Ensure you have the required dependencies installed by following the instructions in `model training.ipynb`.

2. Run the Flask application using the command:
    ```bash
    python app.py
    ```

3. Access the application in your web browser at `http://localhost:5000`.

4. Enter a message in the provided text area and click the "Predict" button to see the spam detection results in real-time.

## Note:

- The spam detection model is trained using the `spam.csv` dataset (not provided here). Make sure to replace it with your own dataset or adjust the code accordingly.

- The project uses Flask-SocketIO for real-time updates. Ensure that you have the required dependencies installed:
    ```bash
    pip install Flask Flask-SocketIO pandas scikit-learn
    ```