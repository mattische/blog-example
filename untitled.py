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


if __name__ == '__main__':
    app.run(debug=True)
