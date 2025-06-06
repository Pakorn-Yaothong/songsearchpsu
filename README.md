# 🎵 Song Emotion Search Web App 🎵

A Flask-based **web application** that analyzes the **emotion** of user-input text and recommends matching songs using the **Genius API**.
The app uses **SpaCy NLP** to detect emotions and provides real-time song search results through a simple web interface.

---

## 🚀 Features

* 🔍 **Analyze emotion** from user text input
* 🎵 **Search songs** related to detected emotion via Genius API
* 🌐 **Simple Web Interface** using Flask
* 🧠 **Emotion detection** via SpaCy NLP model (`en_core_web_sm`)
* 🛁 **API integration** with Genius API
* ✅ Ready for deployment (Procfile + Gunicorn)

---

## ⚙️ Tech Stack

* **Backend**: Flask
* **NLP**: SpaCy (`en_core_web_sm`)
* **External API**: Genius API (for song search)
* **Deployment**: Gunicorn + Procfile (for Render/Heroku etc.)

---

## 📚 How It Works

1️⃣ User types a message in the web form
2️⃣ The app analyzes the text to detect **emotion**:
\- `happy`, `sad`, `angry`, `love`, `fear`, `surprise`, `neutral`
3️⃣ The app queries **Genius API** for songs related to that emotion
4️⃣ Results are displayed as a list of matching songs 🎵

---

## 🔌 Installation & How to Run the App

### 1️⃣ Clone the repo:

```bash
git clone https://github.com/your-username/workflow262.git
cd workflow262
```

### 2️⃣ Setup virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` file:

```env
GENIUS_API_KEY=your_genius_api_key_here
```

### 5️⃣ Run the app:

```bash
python app.py
```

Then open in browser:

```
http://127.0.0.1:5000/
```

---

## 💻 How to Use the App

1️⃣ Open the app in your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
2️⃣ On the home page, you will see a text input form
3️⃣ Type any sentence or message that expresses your current mood or feeling
\- Example: `"I feel so happy today!"`
4️⃣ Click **Search Song** button
5️⃣ The app will detect the **emotion** and show a list of matching songs (fetched from Genius API)
6️⃣ If no songs are found → an error message will be displayed

---

## 🧠 Emotion Keywords Mapping

| Emotion  | Example Keywords                       |
| -------- | -------------------------------------- |
| happy    | happy, joy, excited, pleased, cheerful |
| sad      | sad, depressed, unhappy, gloomy        |
| angry    | angry, mad, furious, annoyed           |
| love     | love, affection, romance, fondness     |
| fear     | fear, scared, afraid, anxious          |
| surprise | surprised, amazed, astonished          |
| neutral  | (default fallback)                     |

---

## 👨‍💼 Author

**Pakorn Yaothong**
GitHub: [https://github.com/Pakorn-Yaothong](https://github.com/Pakorn-Yaothong)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
