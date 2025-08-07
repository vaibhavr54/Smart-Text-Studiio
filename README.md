# 🧠 Next Word Predictor using LSTM

This is a Flask-based web application that uses a trained LSTM model to predict the next word in a sentence. It offers two powerful modules:
1. **Text Generation**: Enter a seed sentence and generate a user-defined number of next words.
2. **Smart Keyboard**: Get top-3 next word suggestions in real-time as you type.

---

## 📚 Dataset Used: Cornell Movie Dialogues Corpus

The LSTM model was trained on the **Cornell Movie Dialogues Corpus**, a well-established dataset that captures natural and informal human conversations from movie scripts. It is widely used for building conversational AI models and next-word predictors.

* **📌 Source**: [Cornell Movie Dialogs Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)
* **💬 Total Dialogues**: 220,000+ conversational exchanges
* **🎭 Characters**: Over 10,000 unique speakers
* **🎞️ Movies**: 617 films
* **🧪 Training Subset**: First **20,000 dialogues** used for training

### ✅ Why This Dataset?

* Realistic and natural human dialogue
* Wide sentence diversity
* Rich in contextual dependencies and informal structures

### 🔄 Preprocessing Steps

* Combined dialogues into coherent line-level context
* Removed punctuation and special characters, and converted text to lowercase
* Tokenized into sequences of 6 words (last word used as label)
* Generated vocabulary mappings (`word2idx`, `idx2word`)
* Used Keras `pad_sequences` to ensure fixed sequence length

### ⚙️ Ideal Use Cases

* ✍️ Predictive Typing
* ⌨️ Auto-Complete Applications
* 🤖 Conversational Agents
* 🔮 Next-Word Prediction in Informal Text

---

## 🚀 Features

- Predict the next word based on context using a deep learning model.
- Auto-complete feature with real-time suggestions.
- Tab key support to auto-insert top suggestion.
- Responsive and modern UI for smooth user experience.
- Modular and scalable architecture.

---

## 🏗️ Project Structure

```

├── app.py                     # Main Flask backend
├── model/
│   ├── next_word_lstm_model2.h5   # Trained LSTM model
│   ├── word2idx.pkl               # Word to index mapping
│   └── idx2word.pkl               # Index to word mapping
├── templates/
│   └── index.html             # Frontend HTML (Jinja2 templated)
├── static/
│   └── style.css              # CSS for styling the app
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation
```
---

## 🧠 Model Overview

- **Model Type**: LSTM (Long Short-Term Memory)
- **Input Sequence Length**: 5 words
- **Vocabulary Size**: Depends on dataset used
- **Output**: Top 3 next-word predictions with probabilities

---

## ⚙️ Installation

1. **Clone the repository**
   ```
   git clone https://github.com/vaibhavr54/Smart-Text-Studio.git
   cd Smart-Text-Studio
   ```

2. **Create virtual environment (optional but recommended)**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```
   python app.py
   ```

5. Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Screenshots

### 🌟 Text Generation Module

Input a starting sentence and generate the continuation based on LSTM prediction.
<img width="1919" height="927" alt="image" src="https://github.com/user-attachments/assets/b6bfa5c0-a7d5-49de-a7d2-2c1e409aa52c" />


### 🧠 Smart Keyboard

Real-time top-3 word suggestions. Tab key autocompletes the first suggestion.
<img width="1919" height="932" alt="image" src="https://github.com/user-attachments/assets/a87f32f7-6464-4fa6-a12b-10a8e280b6d4" />

---

## 📦 Dependencies

* Flask
* TensorFlow / Keras
* NumPy
* Pickle

You can install all via:

```
pip install -r requirements.txt
```

---

## 🛡️ Security

This app uses Flask sessions to store data temporarily across redirects. A secret key is required for session encryption. Make sure to replace `'your_super_secret_key'` with a strong random key in production.

---

## 📝 Future Improvements

* Add punctuation prediction.
* Allow user to upload and train custom datasets.
* Use attention-based models (e.g., Transformers) for better accuracy.
* Add multilingual support.

---

## 👨‍💻 Author

**Vaibhav Rakshe**
B.Tech CSE (Data Science), Vishwakarma Institute of Information Technology, Pune

Mail- [vaibhavrakshe9220@gmail.com](mailto:vaibhavrakshe9220@gmail.com)

---
