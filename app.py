import streamlit as st
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

# Inisialisasi
lemmatizer = WordNetLemmatizer()

# ==========================================
# 1. KONFIGURASI TAMPILAN & WARNA (MODIFIKASI)
# ==========================================
st.set_page_config(
    page_title="Shoffle - CS Otomatis", 
    page_icon="🛍️",
    layout="centered"
)

# Menambahkan CSS untuk mengubah warna tanpa file eksternal
st.markdown("""
    <style>
    /* Mengubah warna latar belakang utama */
    .stApp {
        background-color: #FFFFFF;
    }
    /* Mengubah warna teks judul */
    h1 {
        color: #1E90FF;
    }
    /* Mengubah warna sidebar */
    [data-testid="stSidebar"] {
        background-color: #F0F2F6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (MODIFIKASI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=100)
    st.header("Shoffle")
    st.write("Solusi fashion kekinian terbaik untuk Anda.")
    st.divider()
    st.info("📅 Jam Operasional:\n\nSenin - Jumat: 08.00 - 17.00")
    
    if st.button("Hapus Percakapan"):
        st.session_state.messages = []
        st.rerun()

# ==========================================
# 2. LOAD DATA DAN MODEL (KODE ASLI)
# ==========================================
try:
    intents = json.loads(open('intents.json').read())
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    model = pickle.load(open('chatbot_model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: File model belum ditemukan. Jalankan 'python train_bot.py' dulu!")
    st.stop()

# ==========================================
# 3. FUNGSI OTAK BOT (KODE ASLI)
# ==========================================
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
    p = bow(sentence, words)
    res = model.predict([p])[0]
    return res

def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result

# ==========================================
# 4. LOGIKA CHAT (KODE ASLI DENGAN IKON BARU)
# ==========================================
st.title("Shoffle")
st.write("Silakan tanya stok, pengiriman, pembayaran, atau informasi promo.")

# Simpan riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan chat lama dengan Avatar (MODIFIKASI)
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Input User
if prompt := st.chat_input("Ketik pesan Anda di sini"):
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Bot berpikir
    try:
        tag_prediksi = predict_class(prompt)
        response = get_response(tag_prediksi, intents)
    except Exception as e:
        response = "Maaf, saya belum paham. Coba gunakan kata lain ya."

    # Tampilkan balasan bot dengan Avatar (MODIFIKASI)
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
