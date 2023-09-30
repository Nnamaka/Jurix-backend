from flask import Flask, jsonify, request
from flask_cors import CORS
from utils.chain import qa


app = Flask(__name__)
CORS(app)

@app.route("/api/test")
def hello_world():
        return jsonify({
                'message': 'Jurix is Live..!'
        })

@app.route("/api/jurix/chat", methods=['POST'])
def jurix():

        data = request.get_json()
        user_chat = data['prompt']

        result = qa({'question': user_chat})

        # TODO
        # save message to database from here or do it at the 
        # frontend

        return jsonify({
                'message': result['answer']
        })


if __name__ == "__main__":
        app.run()
