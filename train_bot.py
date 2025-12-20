import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier

try:
    nltk.download('punkt')
    nltk.download('punkt_tab') 
    nltk.download('wordnet')
    nltk.download('omw-1.4')
except:
    pass

lemmatizer = WordNetLemmatizer()

# --- 1. MEMBACA DATA ---
print("Membaca file intents.json...")
try:
    data_file = open('intents.json').read()
    intents = json.loads(data_file)
except FileNotFoundError:
    print("ERROR: File intents.json tidak ditemukan! Pastikan ada di folder yang sama.")
    exit()

words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']

# --- 2. PREPROCESSING ---
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Memecah kalimat jadi kata
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print(f"Data siap: {len(documents)} kalimat training.")

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# --- 3. TRAINING SET ---
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    training.append([bag, doc[1]])

import random
random.shuffle(training)
training = np.array(training, dtype=object)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

# --- 4. MELATIH MODEL ---
print("Sedang melatih model...")
model = RandomForestClassifier(n_estimators=100)
model.fit(train_x, train_y)

pickle.dump(model, open('chatbot_model.pkl', 'wb'))
print("SUKSES! Model berhasil dibuat (chatbot_model.pkl)")
