from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    con = mysql.connector.connect(user='root', password='cbRu8_=w', host='194.47.143.131',
                                  database='blog')

    cursor = con.cursor()
    cursor.execute("SELECT id, heading, body, date FROM posts")

    result = cursor.fetchall()
    cursor.close()
    con.close()

    return render_template("index.html", title="Index page", blog_posts=result)



@app.route('/post/<postId>')
def edit_post(postId):
    con = mysql.connector.connect(user='root', password='cbRu8_=w', host='194.47.143.131',
                                  database='blog')

    cursor = con.cursor()

    cursor.execute("SELECT id, heading, body, date FROM posts WHERE id="+postId)
    res = cursor.fetchone()
    cursor.close()
    con.close()
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)
