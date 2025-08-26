# 📞 Call Evaluation Agent (HF API)

Минимальный ИИ-агент для оценки телефонных звонков:
- Определяет тон разговора: **positive / neutral / negative**
- Генерирует 1–2 рекомендации для улучшения общения

## 🧠 Модель

Используется модель Hugging Face: [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) через бесплатный Inference API.

## Установка

1. Клонируем репозиторий:
```bash
git clone https://github.com/username/call-eval-agent.git
cd call-eval-agent
```

2. Устанавливаем зависимости:
```bash
pip install -r requirements.txt
```

3. Создаём .env файл:
```bash
HF_API_TOKEN=ваш_токен
```

4. Запуск приложения:
```bash
streamlit run call_analyzer.py
```"# call-eval-agent" 
