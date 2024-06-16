# Personalized Nutrition and Health Advisor

## Project Overview

The Personalized Nutrition and Health Advisor is a generative AI-powered application designed to provide personalized nutrition and health recommendations based on user health data and dietary habits. This project leverages NVIDIA's LLM stack and LangChain technologies to create an efficient and practical health advisory agent.

## Features

- **User-specific Recommendations**: Tailors nutrition and health advice based on individual user profiles, including age, gender, personality, dietary preferences, and daily routines.
- **Data Generation**: Generates synthetic data for food intake and health metrics over 30 days for different user profiles.
- **Integration with NVIDIA's LLM and LangChain**: Utilizes NVIDIA's Llama3 and LangChain frameworks to process and analyze data, generating insightful recommendations.
- **Interactive GUI**: Provides a user-friendly interface for users to interact with the health advisor and receive real-time recommendations.

## Requirements

- Python 3.9 or higher
- pandas
- torch
- transformers
- openai


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/personalized-nutrition-health-advisor.git
    cd personalized-nutrition-health-advisor
    ```

2. Install the required packages:
    ```bash
    pip install pandas torch transformers openai tkinter pyttsx3
    ```

3. Set up OpenAI API:
    - Create an account and get your API key from [nvidia_llama3_70b](https://build.nvidia.com/explore/discover?snippet_tab=Python#llama3-70b).
    - Replace `nvapi-KyIbcCy` in the code with your actual API key.

## Usage

1. Generate synthetic data:
    ```bash
    python generate_data.py
    ```

2. Preprocess the data:
    ```bash
    python preprocess_data.py
    ```

3. Run the interactive GUI:
    ```bash
    python main.py
    ```

## Code Explanation

- `generate_data.py`: Generates synthetic food intake and health metric data for 30 days for different user profiles.
- `preprocess_data.py`: Merges the nutrition and health data, filling any missing values and saving the preprocessed data.
- `main.py`: The main interactive script that takes user input, processes the data using NVIDIA's LLM, and provides personalized health recommendations.

## Submission

1. [Link to the GitHub repository](https://github.com/brianbrbr/personalized-nutrition-health-advisor)
2. [Link to the demo video](https://youtu.be/your-demo-video)
3. [Social media post](https://twitter.com/your-twitter-post)

## Contact

- Name: Brian
- Email: liubrian888@gmail.com.tw
- Country: Taiwan
