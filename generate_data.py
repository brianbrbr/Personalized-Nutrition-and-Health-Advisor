import pandas as pd
import random
from datetime import datetime, timedelta

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

# Nutrition data
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

print("Generated 'nutrition_data.csv' and 'health_data.csv'")
