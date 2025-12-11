import streamlit as st
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

# Inisialisasi
lemmatizer = WordNetLemmatizer()

# --- LOAD DATA DAN MODEL ---
try:
    intents = json.loads(open('intents.json').read())
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    model = pickle.load(open('chatbot_model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: File model belum ditemukan. Jalankan 'python train_bot.py' dulu!")
    st.stop()

# --- FUNGSI OTAK BOT ---
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return(np.array(bag))

def predict_class(sentence):
    # Ubah kalimat user jadi angka
    p = bow(sentence, words)
    # Prediksi pakai model
    res = model.predict([p])[0]
    return res

def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result

# --- TAMPILAN WEB (STREAMLIT) ---
st.set_page_config(page_title="E-Commerce Bot", page_icon="🛍️")

st.title("🛍️ Chatbot Toko Online")
st.write("Silakan tanya stok, pengiriman, atau pembayaran.")

# Simpan riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan chat lama
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input User
if prompt := st.chat_input("Ketik pesan Anda di sini..."):
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot berpikir
    try:
        tag_prediksi = predict_class(prompt)
        response = get_response(tag_prediksi, intents)
    except Exception as e:
        response = "Maaf, saya belum paham. Coba gunakan kata lain ya."

    # Tampilkan balasan bot
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})