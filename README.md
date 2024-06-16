# Personalized Nutrition and Health Advisor

**Project Name:** Personalized Nutrition and Health Advisor

**Project Category:** Agents with models larger than 8 billion parameters

**Description:**
Our project, the Personalized Nutrition and Health Advisor, leverages the power of NVIDIA's LLM and LangChain technologies to deliver tailored nutrition and health recommendations. By analyzing user-specific health data collected from various sources such as edge devices, wearables, and smartphones, the advisor provides personalized guidance aimed at helping users achieve their health goals.

## Motivation

With the growing awareness of the importance of personalized health and nutrition, there is a pressing need for advanced solutions that can cater to individual needs. Our project addresses this need by utilizing state-of-the-art AI technologies to create a comprehensive and effective personalized health advisor.

## Features

1. **Data Collection and Simulation:**
   - Generates simulated health and nutrition data for users based on age, gender, personality, dietary preferences, and routine activities.
   - Data sources include edge devices, wearables, and smartphones.

2. **Data Preprocessing:**
   - Cleans and preprocesses the data to ensure accuracy and reliability.
   - Merges nutrition and health data for comprehensive analysis.

3. **Personalized Interaction:**
   - Utilizes a BERT-based tokenizer for processing user inputs.
   - Engages with users to understand their health goals and provide personalized recommendations.

4. **AI-Driven Recommendations:**
   - Employs NVIDIA's LLMs to generate tailored health and nutrition advice based on recent health data.
   - Integrates LangChain framework for seamless data processing and interaction.

5. **User Interface:**
   - Interactive Streamlit-based UI for easy access and user engagement.
   - Provides detailed and actionable health recommendations.

## Technology Stack

- **NVIDIA LLM:** Utilizes models such as Llama3-70b-instruct for generating personalized recommendations.
- **LangChain:** Framework for data processing and AI interaction.
- **Streamlit:** Front-end framework for user interaction.
- **BERT Tokenizer:** For processing user inputs.
- **OpenAI:** API integration for advanced AI capabilities.
- **Pandas:** Data manipulation and preprocessing.

## Requirements

- Python 3.9 or higher
- pandas
- torch
- transformers
- openai
- streamlit


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
    - Replace `your_api_key` in the code with your actual API key.

## Usage
1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Generate synthetic data:
    ```bash
    python generate_data.py
    ```

3. Preprocess the data:
    ```bash
    python preprocess_data.py
    ```

4. Set up OpenAI API key:
    ```bash
   # In your Python script, add your OpenAI API key
   client = OpenAI(
   base_url="https://integrate.api.nvidia.com/v1",
   api_key="your_api_key"
)

    ```

5. Run the interactive GUI:
    ```bash
    python main.py
    streamlit run test.py 
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

## Submission:
-This project is licensed under the MIT License.

## Acknowledgements:
-We would like to thank NVIDIA and LangChain for providing the tools and technologies that made this project possible.
