# Sentiment Analysis

## Overview

This folder contains the code and resources for sentiment analysis. The goal of this project is to analyze, classify the sentiment of text data and create API.

## Structure

- `Restaurant_Reviews.csv`: Dataset containing reviews of restaurants.
- `train.ipynb`: Jupyter notebooks for exploratory data analysis and model training.
- `sentiment_model`: Contains the trained models and scripts for training new models.
- `api/`: API server that expose endpoint for the sentiment model.


## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the `sentiment` folder:
    ```sh
    cd sentiment
    ```

### Usage

1. Train the model:
    ```sh
    juptyer notebook train.ipynb
    ```

2. Start the API server:

* Change directory to `api` folder:
```sh
cd api
```
* Install the required packages:
```sh
pip install -r requirements.txt
```
* Start the server:
```sh
uvicorn main:app --reload
```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

