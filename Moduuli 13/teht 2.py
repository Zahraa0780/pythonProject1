from flask import Flask, jsonify

app = Flask(__name__)


lentokentat = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Municipality": "London"},
    "LFPG": {"Name": "Charles de Gaulle Airport", "Municipality": "Paris"}
}

@app.route('/kenttä/<string:koodi>', methods=['GET'])
def hae_kentta(koodi):
    lentokentta = lentokentat.get(koodi)
    if lentokentta:
        lentokentta["ICAO"] = koodi
        return jsonify(lentokentta)
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

if __name__ == '__main__':
    app.run(debug=True)

