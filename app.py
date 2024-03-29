import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
import re

# def validate_email(email):
#     pattern = r'^[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email) is not None

def validate_email(message):
    pattern = r'[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, message)
    if match:
        email = match.group()
        return email
    else:
        return None


def validate_name(name):
    if name== "Derrick Dadson":
        return True
    # pattern = r'^[A-Za-z\s]{1,50}$'
    # return re.match(pattern, name) is not None

def validate_phone_number(message):
    pattern = r'(?:\+|0)?[0-9]{10,15}'
    match = re.search(pattern, message)
    if match:
        phone_number = match.group()
        return phone_number
    else:
        return None
    
    
conn = psycopg2.connect(
    dbname="derrickdb",
    user="derrickson",
    password="ww2DadsonKwamena",
    host="172.105.148.175",
    port="5432"
)



app = Flask(__name__)
CORS(app)
openai.api_key = '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'  # Update with your OpenAI API key


@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    message_history = data.get('message_history', [])
    session_id=data.get('session_id')
    user_message = data.get('message')

    print(session_id)

    if validate_name(user_message):
        print("Name")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM ambittmedia_clients where session_id='{session_id}'")
        user_exist=cur.fetchall()

        if user_exist:
            
            update_query = """
                UPDATE ambittmedia_clients
                SET name = %s
                WHERE session_id = %s;
            """
            cur.execute(update_query, (user_message, session_id))
            conn.commit()
        else:
            insert_query=("INSERT INTO ambittmedia_clients (name,session_id) VALUES(%s,%s)")
            record_to_insert = (user_message, session_id)
            cur.execute(insert_query, record_to_insert)
            conn.commit()
    
    elif validate_email(user_message):
        print("Email")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM ambittmedia_clients where session_id='{session_id}'")
        user_exist=cur.fetchall()

        if user_exist:
            
            update_query = """
                UPDATE ambittmedia_clients
                SET email = %s
                WHERE session_id = %s;
            """
            cur.execute(update_query, (validate_email(user_message), session_id))
            conn.commit()

 

        # else:
        #     insert_query=("INSERT INTO ambittmedia_clients (name,session_id) VALUES(%s,%s)")
        #     record_to_insert = (user_message, session_id)
        #     cur.execute(insert_query, record_to_insert)
        #     conn.commit()        

    elif validate_phone_number(user_message):
        print("Phone Number")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM ambittmedia_clients where session_id='{session_id}'")
        user_exist=cur.fetchall()

        if user_exist:
            update_query = """
                UPDATE ambittmedia_clients
                SET phone_number = %s
                WHERE session_id = %s;
            """
            cur.execute(update_query, (validate_phone_number(user_message), session_id))
            conn.commit()


    

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
