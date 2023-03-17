from flask import *

app = Flask(__name__)

# 메인 페이지
@app.route('/',methods=['POST','GET'])
def Home() :
    return render_template("test.html")

app.run(debug=True)