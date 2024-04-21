from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_key(length=6):
    """Generate a random key of given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/generate-key', methods=['GET'])
def generate_random_key():
    """Generate and return a random key."""
    key = generate_key()
    return jsonify({'key': key})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
