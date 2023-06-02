# import os
# import openai
# from flask import Flask, session, request, jsonify
# from flask_cors import CORS
# from flask_session import Session
# from redis import Redis

# app = Flask(__name__)
# app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_REDIS'] = Redis(host='172.105.148.175', port=6379, password='')  # Update Redis connection details
# app.secret_key = os.urandom(24)  # Generate a secure secret key
# Session(app)

# CORS(app)
# openai.api_key = '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'  # Update with your OpenAI API key

# # def create_session(session_id):
# #     session['session_id'] = session_id
# #     session.permanent = True  # Set the session as permanent
# #     session.modified = True  # Mark the session as modified
# #     session['session_messages'] = [
# #         {"role": "system",
# #          "content": "Hi, my name is Ambittmedia assistant, a digital marketing agency and web development company that helps businesses succeed online. We specialize in SEO, PPC advertising, social media marketing, and web development. Please provide your name, email, and phone number so that we can contact you later."}
# #     ]


# def append_message(role, content):
#     messages = session['session_messages']
#     messages.append({"role": role, "content": content})
#     session['session_messages'] = messages


# @app.route('/api/chatbot', methods=['POST'])
# def chatbot_response():
#     message = request.json.get('message')
#     session_id=request.json.get('session_id')
#     print(session)

#     if 'session_id' not in session or session['session_id'] != session_id:
#         create_session(session_id)
#         print("NEW")
#         print(session_id)
#     else:
#         print("EXISTING")
#         print(session['session_messages'])

#     append_message("user", message)
#     messages = session['session_messages']

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )

#     chatbot_reply = response["choices"][0]["message"]["content"]
#     append_message("assistant", chatbot_reply)

#     return jsonify({'answer': chatbot_reply})

# if __name__ == '__main__':
#     app.run()


import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
openai.api_key = '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'  # Update with your OpenAI API key


@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    message_history = data.get('message_history', [])

    user_message = data.get('message')
    if user_message:
        message_history.append({"role": "user", "content": user_message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )

    chatbot_reply = response["choices"][0]["message"]["content"]
    message_history.append({"role": "assistant", "content": chatbot_reply})


    return jsonify({'answer': chatbot_reply, 'message_history': message_history})


if __name__ == '__main__':
    app.run()
