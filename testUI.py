import pandas as pd
import random
from datetime import datetime, timedelta
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
  base_url="https://integrate.api.nvidia.com/v1",
  api_key=""
)

# User ID range
user_ids = [1, 2, 3, 4, 5]

# Food and nutrition data
foods = [
    {"name": "Apple", "calories": 52, "protein": 0.3, "carbs": 14, "fats": 0.2, "fiber": 2.4},
    {"name": "Banana", "calories": 96, "protein": 1.3, "carbs": 27, "fats": 0.3, "fiber": 2.6},
    {"name": "Chicken Breast", "calories": 165, "protein": 31, "carbs": 0, "fats": 3.6, "fiber": 0},
    {"name": "Broccoli", "calories": 55, "protein": 3.7, "carbs": 11.2, "fats": 0.6, "fiber": 3.8},
    {"name": "Rice", "calories": 130, "protein": 2.7, "carbs": 28, "fats": 0.3, "fiber": 0.4},
]

# User information
user_info = {
    1: {"age": 25, "gender": "Male", "personality": "Active", "preferences": "Low fat", "routine": "Morning exercise"},
    2: {"age": 30, "gender": "Female", "personality": "Sedentary", "preferences": "High protein", "routine": "Evening walks"},
    3: {"age": 35, "gender": "Male", "personality": "Moderately active", "preferences": "Balanced diet", "routine": "Afternoon gym"},
    4: {"age": 40, "gender": "Female", "personality": "Active", "preferences": "Low carb", "routine": "Morning yoga"},
    5: {"age": 28, "gender": "Male", "personality": "Sedentary", "preferences": "High fiber", "routine": "No specific routine"},
}

# Generate 30 days of data
dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30)]

# Nutrition and health data generation
nutrition_records = []
health_records = []

for user_id in user_ids:
    for date in dates:
        daily_calories = 0
        daily_protein = 0
        daily_carbs = 0
        daily_fats = 0
        daily_fiber = 0
        daily_foods = []
        
        # Randomly select 3-5 types of food
        daily_food_count = random.randint(3, 5)
        for _ in range(daily_food_count):
            food = random.choice(foods)
            daily_foods.append(food["name"])
            daily_calories += food["calories"]
            daily_protein += food["protein"]
            daily_carbs += food["carbs"]
            daily_fats += food["fats"]
            daily_fiber += food["fiber"]
        
        nutrition_records.append({
            "user_id": user_id,
            "date": date,
            "foods": ", ".join(daily_foods),
            "calories": daily_calories,
            "protein": daily_protein,
            "carbs": daily_carbs,
            "fats": daily_fats,
            "fiber": daily_fiber
        })

        # Generate health data
        health_records.append({
            "user_id": user_id,
            "date": date,
            "weight": random.uniform(60, 90),
            "cholesterol_level": random.randint(150, 250),
            "blood_pressure": f"{random.randint(110, 140)}/{random.randint(70, 90)}",
            "age": user_info[user_id]["age"],
            "gender": user_info[user_id]["gender"],
            "personality": user_info[user_id]["personality"],
            "preferences": user_info[user_id]["preferences"],
            "routine": user_info[user_id]["routine"]
        })

nutrition_df = pd.DataFrame(nutrition_records)
health_df = pd.DataFrame(health_records)

nutrition_df.to_csv('nutrition_data.csv', index=False)
health_df.to_csv('health_data.csv', index=False)

# Data preprocessing
nutrition_df = pd.read_csv('nutrition_data.csv')
health_df = pd.read_csv('health_data.csv')

nutrition_df.fillna(0, inplace=True)
health_df.fillna(0, inplace=True)

# Merge datasets
data = pd.merge(nutrition_df, health_df, on=['user_id', 'date'])
data.to_csv('preprocessed_data.csv', index=False)

# Define interaction function
def interact(user_id, user_goal):
    user_data = data[data['user_id'] == user_id].tail(7)  # Get the most recent 7 days of data
    user_info_data = user_data.iloc[0].to_dict()

    health_summary = f"Age: {user_info_data['age']}, Gender: {user_info_data['gender']}, Personality: {user_info_data['personality']}, Preferences: {user_info_data['preferences']}, Routine: {user_info_data['routine']}\n"
    health_details = ""
    for index, row in user_data.iterrows():
        health_details += f"Date: {row['date']}, Foods: {row['foods']}, Calories: {row['calories']}, Protein: {row['protein']}, Carbs: {row['carbs']}, Fats: {row['fats']}, Fiber: {row['fiber']}, Weight: {row['weight']:.2f}, Cholesterol Level: {row['cholesterol_level']}, Blood Pressure: {row['blood_pressure']}\n"

    prompt = f"User's recent health status: {health_summary}Based on the following health data for the past week: {health_details}, provide a personalized recommendation to achieve the goal: {user_goal}"

    completion = client.chat.completions.create(
      model="meta/llama3-70b-instruct",
      messages=[{"role":"user","content":prompt}],
      temperature=0.5,
      top_p=1,
      max_tokens=1024,
      stream=True
    )

    response_text = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response_text += chunk.choices[0].delta.content

    return response_text

# Streamlit UI
st.title("Personalized Nutrition and Health Advisor")

st.sidebar.header("User Input")
user_id = st.sidebar.selectbox("Select User ID", user_ids)
user_goal = st.sidebar.text_input("Enter Your Health Goal", "")

if st.sidebar.button("Get Recommendation"):
    with st.spinner("Generating recommendation..."):
        recommendation = interact(user_id, user_goal)
        st.success("Recommendation Generated!")
        st.write(recommendation)
