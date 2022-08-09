

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