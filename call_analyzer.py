import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("HF_TOKEN"))  # должно напечатать твой токен, начиная с hf_


API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
}

def query_model(prompt):
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct:fireworks-ai",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()
    except ValueError:
        return {"error": "Не удалось распарсить JSON", "raw": response.text}

# ------------------- Streamlit -------------------
st.set_page_config(page_title="Call Evaluation Agent", layout="centered")
st.title("Агент оценки звонков (Llama 3.1)")

user_input = st.text_area("Введите расшифровку звонка", height=200)

if st.button("Анализировать"):
    if user_input.strip():
        prompt = f"""
        Ты — эксперт по оценке телефонных звонков.
        Проанализируй следующий разговор:

        {user_input}

        Верни строго JSON с полями:
        {{
          "sentiment": "positive | neutral | negative",
          "recommendations": ["совет 1", "совет 2"]
        }}
        """
        output = query_model(prompt)

        if "choices" in output:
            message = output["choices"][0]["message"]["content"]
            st.subheader("Результат")
            st.text(message)
        else:
            st.error(f"Ошибка API: {output}")
    else:
        st.warning("Введите текст для анализа.")


#positive
#Сотрудник: Добрый день! Рад помочь вам сегодня.  
#Клиент: Спасибо, вы очень быстро решили мою проблему!  
#Сотрудник: Рад был помочь, обращайтесь в любое время.  
#Клиент: Обязательно, спасибо ещё раз!

#neutral
#Сотрудник: Здравствуйте, чем могу помочь?  
#Клиент: Мне нужна информация о тарифах.  
#Сотрудник: Вот информация по тарифам.  
#Клиент: Хорошо, спасибо.  
#Сотрудник: Всего доброго.

#negative
#Сотрудник: Здравствуйте, чем могу помочь?  
#Клиент: Я уже час жду вашей поддержки, это ужасно!  
#Сотрудник: Извините за ожидание, но я могу помочь только сейчас.  
#Клиент: Это неприемлемо!  
#Сотрудник: Прошу прощения за неудобства.

