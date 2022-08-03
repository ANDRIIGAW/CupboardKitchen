from flask import Flask, render_template, request
import sqlite3 as sql
from datetime import datetime
import os

# https://github.com/ANDRIIGAW/CupboardKitchen
# https://youtu.be/TN_9Q3Q5ang


now = datetime.now()

PEOPLE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route("/")
def index():
    '''Сreating the first page'''
    full_filename1 = os.path.join(app.config['UPLOAD_FOLDER'], 'kitch1.jpg')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'kitch2.jpg')
    full_filename3 = os.path.join(app.config['UPLOAD_FOLDER'], 'kitch3.jpg')
    full_filename4 = os.path.join(app.config['UPLOAD_FOLDER'], 'kitch4.jpg')
    full_filename5 = os.path.join(app.config['UPLOAD_FOLDER'], 'cupb1.jpg')
    full_filename6 = os.path.join(app.config['UPLOAD_FOLDER'], 'cupb2.jpg')
    full_filename7 = os.path.join(app.config['UPLOAD_FOLDER'], 'cupb3.jpg')
    full_filename8 = os.path.join(app.config['UPLOAD_FOLDER'], 'cupb4.jpg')
    full_filename9 = os.path.join(app.config['UPLOAD_FOLDER'], 'cupb5.jpg')
    con = sql.connect("cupbkitch.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from orders")
    data = cur.fetchall()
    return render_template("index.html",
                           user_image1=full_filename1,
                           user_image2=full_filename2,
                           user_image3=full_filename3,
                           user_image4=full_filename4,
                           user_image5=full_filename5,
                           user_image6=full_filename6,
                           user_image7=full_filename7,
                           user_image8=full_filename8,
                           user_image9=full_filename9,
                           datas=data
                           )


@app.route("/answer", methods=['GET', 'POST'])
def answer(*args):
    if request.method == 'POST':
        name = request.form.get("name")
        phone = request.form.get("phone")
        furniture = request.form.get("furniture")
        height = request.form.get("height")
        long = request.form.get("long")
        dising_number = request.form.get("dising_number")
        bools = request.form.get("bools")
        check_list_input = [name, phone, furniture,
                            height, long, dising_number, bools]
        check_list_output = check(check_list_input)
        if check_list_output != True or len(phone) < 10 or any(map(str.isdigit, phone)) != True:
            return render_template("check.html")
        con = sql.connect("cupbkitch.db")
        cur = con.cursor()
        if bools != "yes":
            price_furnitur = round(float(height)/10 * float(long) * 100000)
            cur.execute("INSERT INTO orders (name, phone, furniture, height, long, dising_number, bools, price_furnitur,  date) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);",
                        (name, phone, furniture, height, long, dising_number, bools, price_furnitur, now))
            return render_template("answer.html",
                                   name=name,
                                   phone=phone,
                                   furniture=furniture,
                                   height=height,
                                   long=long,
                                   dising_number=dising_number,
                                   bools="НІ",
                                   price_furnitur=price_furnitur)

        else:
            price_furnitur = round(
                float(height)/10 * float(long) * 100000 * 1.3)
            cur.execute("INSERT INTO orders (name, phone, furniture, height, long, dising_number, bools, price_furnitur,  date) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);",
                        (name, phone, furniture, height, long, dising_number, bools, price_furnitur, now))
            return render_template("answer.html",
                                   name=name,
                                   phone=phone,
                                   furniture=furniture,
                                   height=height,
                                   long=long,
                                   dising_number=dising_number,
                                   bools="ТАК",
                                   price_furnitur=price_furnitur)
    return render_template("index.html")


@app.route("/check")
def check_page():
    return render_template("check.html")


def check(s):
    item = s
    for j in item:
        if j in ["-", "--", " ", "", "-", "_", "__", "?", "~q", "%", "~p", "#", "~h", "/", "~s", "\"", "''", None]:
            return False
        else:
            return True


if __name__ == "__main__":
    app.run(debug=True)
