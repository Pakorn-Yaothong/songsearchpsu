import spacy

# โหลดโมเดลภาษา (ใช้ภาษาอังกฤษ)
nlp = spacy.load("en_core_web_sm")

# อารมณ์ที่สามารถตรวจจับได้
emotion_keywords = {
    "happy": ["happy", "joy", "excited", "pleased", "cheerful"],
    "sad": ["sad", "depressed", "unhappy", "gloomy"],
    "angry": ["angry", "mad", "furious", "annoyed"],
    "love": ["love", "affection", "romance", "fondness"],
    "fear": ["fear", "scared", "afraid", "anxious"],
    "surprise": ["surprised", "amazed", "astonished"]
}

def predict_emotion(text):
    doc = nlp(text.lower())
    for token in doc:
        for emotion, keywords in emotion_keywords.items():
            if token.text in keywords:
                return emotion
    return "neutral"
