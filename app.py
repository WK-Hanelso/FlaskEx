import os           # 파일 핸들링
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import datetime

from models import db
from models import Fcuser
from models import LED_nomdle

from ledControl import *

app = Flask(__name__ )
# status는 현재 gpio led 상태를 저장하는 변수
status = {}

@app.route("/led/<color>/<mode>")
def turnMode( color, mode ):
    global status
    red = 0
    yellow = 0
    green = 0
    time = datetime.datetime.now().strftime( "%Y-%m-%d-%H:%M:%S")

    # LED 컨트롤러 생성
    objLed = LedController()

    if color == "all":
        color = "rgy"

    # LED 설정값 set
    objLed.setListColor( list( color ) )
    objLed.setMode( int( mode ) )
    
    objLed.actLed()

    # db값 확인
    if objLed.isSetColor( "RED" ):
        red = int( mode )
        status["RED"] = red
    if objLed.isSetColor( "YELLOW"):
        yellow = int( mode )
        status["YELLOW"] = yellow
    if objLed.isSetColor( "GREEN" ):
        green = int( mode )
        status["GREEN"] = green

    # db
    led_db = LED_nomdle()
    led_db.red = red
    led_db.yellow = yellow
    led_db.green = green
    led_db.status = str(status)
    led_db.time = time

    db.session.add( led_db )
    db.session.commit()

    return render_template("led.html", color = color, mode = mode)

@app.route('/register', methods=['GET', 'POST'])     # app의 main route가 '/'가 된다는 것이다.
def register():

    if request.method=="POST":
        userid = request.form.get("userid")
        username = request.form.get("username")
        password = request.form.get("password")
        re_password = request.form.get("re-password")

        if( userid and username and password and re_password ) and ( password == re_password ):
            fcuser = Fcuser()
            fcuser.userid = userid
            fcuser.username = username
            fcuser.password = password
            print( userid )
            print( username)
            print( password )
            print( re_password)

            db.session.add( fcuser )
            db.session.commit()

            return redirect('/')

    return render_template("register.html")

@app.route('/', methods = ["GET", "POST"])     # app의 main route가 '/'가 된다는 것이다.
def hello():
    return render_template("hello.html")

if __name__=="__main__":
    print("app.py start!")
    # 현재 파일이 실행되는 경로
    basedir = os.path.abspath(os.path.dirname(__file__))        # 절대 경로 ( abspath )로 현재파일( __file__ )의 디렉토리 경로( dirname )를 이용하겠다.
    print( "basedir:{}".format(basedir) )

    # db파일이 저장되는 경로
    dbfile = os.path.join( basedir, "db.sqlite")                # basedir ( /home/hanelso/smb_dir/FlaskEx )에  db.sqlite 를 연결한다. -> /home/hanelso/smb_dir/FlaskEx/db.sqlite
    print("file:{}".format(dbfile))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True                  # 요청 받은 것에 대해서 응답을 할때를 Teardown 이라고 하는데 이때 commit을 하겠다는 의미
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)
    db.app = app
    db.create_all()
    app.run( host="0.0.0.0", port = 5008, debug= True )


