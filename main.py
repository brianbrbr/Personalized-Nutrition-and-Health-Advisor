import pandas as pd
import torch
from transformers import BertTokenizer
import openai
from openai import OpenAI


# 初始化OpenAI客户端
client = OpenAI(
  base_url="https://integrate.api.nvidia.com/v1",
  api_key=""
)

# 讀取預處理後的數據
data = pd.read_csv('preprocessed_data.csv')

# 讀取分詞器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


# 定义交互函数
def interact():
    user_id = int(input("Enter your user ID (1-5): "))
    user_goal = input("Enter your health goal: ")

    # 提取用户的健康数据
    user_data = data[data['user_id'] == user_id].tail(7)  # 获取最近7天的数据
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

    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


if __name__ == "__main__":
    interact()