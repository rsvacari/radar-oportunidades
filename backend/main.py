from flask import Flask, jsonify
from scraping import get_acoes, get_fiis
from scoring import rank_acoes, rank_fiis
from flask_cors import CORS   # <-- ADICIONE ISTO

app = Flask(__name__)
CORS(app)  # <-- LIBERA ACESSO DE QUALQUER DOMÍNIO

@app.route("/api/acoes")
def api_acoes():
    df = get_acoes()
    df_rank = rank_acoes(df)
    return jsonify(df_rank.to_dict(orient="records"))

@app.route("/api/fiis")
def api_fiis():
    df = get_fiis()
    df_rank = rank_fiis(df)
    return jsonify(df_rank.to_dict(orient="records"))

@app.route("/api/health")
def api_health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
