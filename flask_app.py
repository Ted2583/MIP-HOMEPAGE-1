from flask import Flask, render_template, request, url_for
import pymysql as s

app = Flask(__name__)

## KO
@app.route('/')
def home():
    return render_template('landingpage.html')

@app.route('/main2')
def home2():
    return render_template('template.html')

@app.route('/intro')
def intro():
    return render_template('into.html')
@app.route('/intro2')
def intro2():
    return render_template('into2.html')

@app.route('/intro3')
def intro3():
    return render_template('into3.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/support')
def support():
    return render_template('support.html')

## VN
@app.route('/main-vn')
def home_vn():
    return render_template('landingpage-VN.html')

@app.route('/main2-vn')
def home2_vn():
    return render_template('template-VN.html')

@app.route('/intro-vn')
def intro_vn():
    return render_template('into-VN.html')

@app.route('/intro2-vn')
def intro2_vn():
    return render_template('into2-VN.html')

@app.route('/intro3-vn')
def intro3_vn():
    return render_template('into3-VN.html')

@app.route('/product-vn')
def product_vn():
    return render_template('product-VN.html')

@app.route('/support-vn')
def support_vn():
    return render_template('support-VN.html')

## EN
@app.route('/main-en')
def home_en():
    return render_template('landingpage - EN.html')

@app.route('/main2-en')
def home2_en():
    return render_template('template - EN.html')

@app.route('/intro-en')
def intro_en():
    return render_template('into - EN.html')
@app.route('/intro2-en')
def intro2_en():
    return render_template('into2 - EN.html')

@app.route('/intro3-en')
def intro3_en():
    return render_template('into3 - EN.html')

@app.route('/product-en')
def product_en():
    return render_template('product - EN.html')

@app.route('/support-en')
def support_en():
    return render_template('support - EN.html')






@app.route('/board', methods=['POST'])
def calulate() :
    temp1=request.form['name1']
    temp11 = request.form['name2']
    temp2=request.form['email']
    temp3=request.form['message']

    print(temp1+" "+temp11)
    try :
        if len(temp1 + " " + temp11) == 2 :
            print("ge4")
            raise Exception

        elif temp2.find("@") < 0 :
            print("ge3")
            raise Exception

        elif temp2.find(".") < 0 :
            print("ge")
            raise Exception

        elif len(temp1 + " " + temp11) < 2 :
            print("ge2")
            raise Exception


    except Exception as e :
        return render_template("input-alert.html")

    except :
        raise

    else:
        conn = s.connect(host='localhost', user='root',
                         password='zaiguru39@', db='my_db', charset='utf8')
        curs = conn.cursor()
        sql = "select * from test"
        curs.execute(sql)
        data = curs.fetchall()
        sql = "INSERT INTO test (username, adress, contents) VALUES (%s,%s,%s)"
        val = (temp1 + " " + temp11, temp2, temp3)
        curs.execute(sql, val)
        conn.commit()
        conn.close()
        return render_template("input-alert2.html")

    return 99999









if __name__ == '__main__':
    app.run(debug=True)