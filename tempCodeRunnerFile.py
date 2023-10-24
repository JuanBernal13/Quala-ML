import pandas as pd

# Carga de datos
df = pd.read_excel('Datos.xlsx')

print(df)

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Descargar las stopwords en español
nltk.download('stopwords')

# Inicializar el stemmer y las stopwords
stemmer = SnowballStemmer('spanish')
stop_words = set(stopwords.words('spanish'))

def preprocess(text):
    # Tokenizar
    tokens = nltk.word_tokenize(text.lower())
    # Eliminar stopwords y aplicar stemming
    return ' '.join(stemmer.stem(token) for token in tokens if token.isalpha() and token not in stop_words)

df['Frase'] = df['Frase'].apply(preprocess)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Frase'])
y = df['Clasificacion']

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

pruebas_bebidas = [
    "Este café es malo, no me gusta en absoluto.",
    "La bebida es bastante regular, ni buena ni mala.",
    "Me encanta esta bebida, es realmente buena.",
    "No puedo recomendar esta bebida, es muy mala para mi gusto.",
    "La calidad de esta bebida es regular, no es excepcional.",
    "Tengo que admitir que esta bebida es realmente buena.",
    "Esta bebida es terrible, el sabor es horrible."
]

etiquetas_bebidas = [0, 1, 2, 0, 1, 2, 0]

# Preprocesar las frases de prueba
frases_preprocesadas_bebidas = [preprocess(frase) for frase in pruebas_bebidas]

# Vectorizar las frases de prueba utilizando el mismo vectorizador
X_prueba_bebidas = vectorizer.transform(frases_preprocesadas_bebidas)

# Realizar la predicción con el modelo entrenado
predicciones_bebidas = model.predict(X_prueba_bebidas)

# Imprimir las predicciones junto con las etiquetas reales
for frase, etiqueta_predicha, etiqueta_real in zip(pruebas_bebidas, predicciones_bebidas, etiquetas_bebidas):
    if etiqueta_predicha == 0:
        print(f"Frase: '{frase}' -> Clasificación: Mala (0) | Etiqueta Real: {etiqueta_real}")
    elif etiqueta_predicha == 1:
        print(f"Frase: '{frase}' -> Clasificación: Regular (1) | Etiqueta Real: {etiqueta_real}")
    else:
        print(f"Frase: '{frase}' -> Clasificación: Buena (2) | Etiqueta Real: {etiqueta_real}")
