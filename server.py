from flask import Flask, request, jsonify, render_template
from password_generator import generate_password

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['GET'])
def generate_password_endpoint():
    length = int(request.args.get('length', 8))
    use_uppercase = request.args.get('uppercase', 'false').lower() == 'true'
    use_lowercase = request.args.get('lowercase', 'true').lower() == 'true'
    use_digits = request.args.get('digits', 'false').lower() == 'true'
    use_special = request.args.get('special', 'false').lower() == 'true'
    
    password = generate_password(length=length, 
                                 use_uppercase=use_uppercase, 
                                 use_lowercase=use_lowercase, 
                                 use_digits=use_digits, 
                                 use_special=use_special)
    
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
