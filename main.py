from flask import request, render_template, Flask
import sqlite3

app = Flask(__name__)
def update_db(username,chat):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
  
    c.execute("CREATE TABLE IF NOT EXISTS chat (name text , chat text);")
    result = c.execute("INSERT INTO chat(name,chat) VALUES ('%s','%s')" %(username,chat) )
    conn.commit()
def get_data():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    result = c.execute("SELECT * FROM chat")
    conn.commit()
    return result.fetchall()
def delete_all():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    result = c.execute("DELETE FROM chat")
    conn.commit()

    

@app.route('/',methods=["GET", "POST"])
def home():
    messages=get_data() 
    if request.method == "POST":
        username = request.form['username']
        chat = request.form['chat']
        update_db(username,chat)
       
        messages=get_data() 
        return render_template('index.html',messages=messages)
    elif request.method == "GET" :   
        delete_all()
        print("ji") 
        return render_template('index.html',messages=messages)
    return render_template('index.html',messages=messages)    


if __name__ == "__main__":
    app.run(debug=True)