from flask import Flask, jsonify
from controller import Controller

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/test-tienda-nube', methods=['GET'])
def test_tienda_nube():
    try:
        return jsonify(Controller.get_shipments())
    except Exception as e:
        print('Oops! An error has ocurred.')
        return jsonify([])


app.run(debug=True)