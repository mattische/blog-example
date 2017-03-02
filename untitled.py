from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    con = mysql.connector.connect(user='<user>', password='<password>', host='194.47.143.131',
                                  database='<database name>')

    cursor = con.cursor()
    cursor.execute("SELECT id, heading, body, date FROM posts")

    result = cursor.fetchall()
    cursor.close()
    con.close()

    return render_template("index.html", title="Index page", <database name>_posts=result)



@app.route('/post/<postId>')
def edit_post(postId):
    con = mysql.connector.connect(user='<user>', password='<password>', host='194.47.143.131',
                                  database='<database name>')

    cursor = con.cursor()

    cursor.execute("SELECT id, heading, body, date FROM posts WHERE id="+postId)
    res = cursor.fetchone()
    cursor.close()
    con.close()
    return render_template("edit_post.html", post=res)


@app.route('/update_post', methods=['POST'])
def update():
    print("update post...")
    con = mysql.connector.connect(user='<user>', password='<password>', host='194.47.143.131',
                                  database='<database name>')

    cursor = con.cursor()

    cursor.execute("UPDATE posts SET heading='"+request.form['heading']+"', body='"+\
                   request.form['body']+"', date=now() WHERE id=" + request.form['postId'])

    cursor.close()
    con.commit()
    con.close()
    return render_template("edited_post.html")

if __name__ == '__main__':
    app.run(debug=True)
