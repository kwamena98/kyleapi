
import openai
from flask import Flask, session, request, jsonify
from flask_cors import CORS
import random
from flask_session import Session
from redis import Redis

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='172.105.148.175', port=6379, password='')
app.secret_key="kajsdkajsdlkjaslkdjlkasjdlas"
Session(app)

CORS(app)
openai.api_key = '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'


# def generate_unique_id(length):
#     """Generate a random string of given length."""
#     chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     return ''.join(random.choice(chars) for _ in range(length))

def create_session(session_id):
    session['session_id'] = session_id
    session['session_messages'] = [{"role": "system", "content": "Hi, my name is Ambittmedia assistant, a digital marketing agency and web development company that helps businesses succeed online. We specialize in SEO, PPC advertising, social media marketing, and web development. Please provide your name, email, and phone number so that we can contact you later."}]

def append_message(role, content):
    messages = session['session_messages']
    messages.append({"role": role, "content": content})
    session['session_messages'] = messages

# @app.before_request
# def check_session():
#     if 'session_id' not in session:
#         create_session()
#         print(session['session_id'])
#     else:
#         print(session['session_messages'])

@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    message = request.form.get('message')
    session_id=request.form.get('session_id')

    if session_id not in session:
        create_session(session_id)
    else:
        print(session['session_messages'])
    # message=request.json['message']
    # print(message)
    append_message("user", message)
    messages = session['session_messages']
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    chatbot_reply = response["choices"][0]["message"]["content"]
    append_message("assistant", chatbot_reply)
    
    return jsonify({'answer': chatbot_reply})

if __name__ == '__main__':
    app.run()
