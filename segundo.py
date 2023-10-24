from flask import Flask, request, jsonify
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from flask_cors import CORS   # <-- Importa CORS
app = Flask(__name__)
CORS(app) 

# Carga de datos
df = pd.read_excel('Datos.xlsx')

# Inicializar el stemmer y las stopwords
stemmer = SnowballStemmer('spanish')
stop_words = set(stopwords.words('spanish'))

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    return ' '.join(stemmer.stem(token) for token in tokens if token.isalpha() and token not in stop_words)

df['Frase'] = df['Frase'].apply(preprocess)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Frase'])
y = df['Clasificacion']

model = LogisticRegression()
model.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    frase = preprocess(data['frase'])
    vectorized = vectorizer.transform([frase])
    prediction = model.predict(vectorized)
    return jsonify(prediction=int(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)
