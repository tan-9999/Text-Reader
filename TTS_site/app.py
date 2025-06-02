from flask import Flask, request, render_template, jsonify
import pyttsx3  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form.get('text')
    volume = float(request.form.get('volume', 1.0))  # 0.0 to 1.0
    rate = int(request.form.get('rate', 200))        # Typical range: 100–300
    if text:
        engine = pyttsx3.init() 
        engine.setProperty('volume', volume)
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return jsonify({'status': 'success', 'message': 'Done'})
    return jsonify({'status': 'error', 'message': 'No text provided'})

if __name__ == '__main__':
    app.run(debug=True)
