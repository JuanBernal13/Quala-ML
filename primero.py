from flask import Flask, request, jsonify
from flask_cors import CORS   # <-- Importa CORS
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)  # <-- Habilita CORS para toda la aplicación

# Cargando y entrenando un modelo de ejemplo
data = load_diabetes()
X, y = data.data, data.target
model = LinearRegression().fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    prediction = model.predict([input_data])
    return jsonify(prediction[0])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
