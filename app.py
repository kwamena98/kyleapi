# import openai
# from flask import Flask, session, request, jsonify
# from flask_cors import CORS
# import random


# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# CORS(app)
# openai.api_key = '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'

# def generate_unique_id(length):
#     """Generate a random string of given length."""
#     chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

#     return ''.join(random.choice(chars) for _ in range(length))

#     # return "jhASHkj"

# def create_session():
#     session['session_id'] = generate_unique_id(10)
#     session['session_messages'] = [{"role": "system", "content": "Hi my  name is Ambittmedia assistant, a a digital marketing agency and web development company that helps businesses succeed online. They specialize in SEO, PPC advertising, social media marketing, and web development. Ask the user to provide the name , email and phone number step by step so that we can  call them or contact them later"}]



# def append_message(role, content):
#     session['session_messages'].append({"role": role, "content": content})





# # # def generate_random_string(length):

# # # # Generate 10 random strings of length 10
# # # random_strings = generate_random_string(10)

# # print(random_strings)

# @app.before_request
# def check_session():
#     if 'session_id' not in session:
#         create_session()
#     else:
#         print(session['session_messages'])

# @app.route('/api/chatbot', methods=['POST'])
# def chatbot_response():
#     # message=request.json['message']
#     message = request.form.get('message')
#     print(message)
    
#     append_message("user", message)
    
#     messages = session['session_messages']
#     print(messages)
    
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )
    
#     chatbot_reply = response["choices"][0]["message"]["content"]
#     append_message("assistant", chatbot_reply)

#     print(messages)
    
#     return jsonify({'answer': chatbot_reply})

# if __name__ == '__main__':
#     app.run()


import openai
from flask import Flask, session, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

CORS(app)
openai.api_key = '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'

def generate_unique_id(length):
    """Generate a random string of given length."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def create_session():
    session['session_id'] = generate_unique_id(10)
    session['session_messages'] = [{"role": "system", "content": "Hi, my name is Ambittmedia assistant, a digital marketing agency and web development company that helps businesses succeed online. We specialize in SEO, PPC advertising, social media marketing, and web development. Please provide your name, email, and phone number so that we can contact you later."}]

def append_message(role, content):
    messages = session['session_messages']
    messages.append({"role": role, "content": content})
    session['session_messages'] = messages

@app.before_request
def check_session():
    if 'session_id' not in session:
        create_session()
    else:
        print(session['session_messages'])

@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    message = request.form.get('message')
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
