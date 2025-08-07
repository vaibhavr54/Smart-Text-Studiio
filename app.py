from flask import Flask, request, render_template, jsonify, session, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

app = Flask(__name__)
app.secret_key = 'e43df9a8a9adcc6e0c44e34f05dd8f68b1f54d8471a9a7d4308e739267a917d1'

# Load model and mappings
model = load_model('model/next_word_lstm_model2.h5')
with open('model/word2idx.pkl', 'rb') as f:
    word2idx = pickle.load(f)
with open('model/idx2word.pkl', 'rb') as f:
    idx2word = pickle.load(f)

# Parameters
seq_len = 5
vocab_size = len(word2idx) + 1

def predict_top_k_words(seed_text, k=3):
    input_seq = seed_text.lower().split()[-seq_len:]
    token_seq = [word2idx.get(w, 0) for w in input_seq]
    token_seq = pad_sequences([token_seq], maxlen=seq_len)
    preds = model.predict(token_seq, verbose=0)[0]
    top_indices = np.argsort(preds)[-k:][::-1]
    return [idx2word.get(idx, '') for idx in top_indices]

def generate_text(seed_text, n_words):
    result = seed_text.lower().split()
    for _ in range(n_words):
        input_seq = result[-seq_len:]
        token_seq = [word2idx.get(w, 0) for w in input_seq]
        token_seq = pad_sequences([token_seq], maxlen=seq_len)
        predicted_idx = np.argmax(model.predict(token_seq, verbose=0), axis=-1)[0]
        result.append(idx2word.get(predicted_idx, ''))
    return ' '.join(result)

@app.route('/')
def home():
    generated = session.pop('generated', None)
    seed = session.pop('seed', '')
    return render_template('index.html', generated=generated, seed=seed, selected_module='generate')

@app.route('/generate', methods=['POST'])
def generate():
    seed_text = request.form['seed_text_gen']
    n_words = int(request.form['n_words_gen'])
    result = generate_text(seed_text, n_words)
    session['generated'] = result
    session['seed'] = seed_text
    return redirect(url_for('home'))

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    seed_text = data.get('seed', '')
    suggestions = predict_top_k_words(seed_text)
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)
