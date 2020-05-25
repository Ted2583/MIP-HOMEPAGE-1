from flask import Flask, render_template, request, url_for
import pymysql as s

app = Flask(__name__)

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




@app.route('/board', methods=['POST'])
def calulate() :
    temp1=request.form['name1']
    temp11 = request.form['name2']
    temp2=request.form['email']
    temp3=request.form['message']

    print(temp1+" "+temp11)
    print(temp2)
    print(temp3)

    conn = s.connect(host='localhost', user='root',
                     password='zaiguru39@', db='my_db', charset='utf8')
    curs = conn.cursor()
    sql = "select * from test"
    curs.execute(sql)

    data = curs.fetchall()
    print(data)  # 첫번째 row

    sql = "INSERT INTO test (username, adress, contents) VALUES (%s,%s,%s)"
    val = (temp1+" "+temp11, temp2, temp3)
    curs.execute(sql, val)

    print(curs.rowcount, "record inserted.")

    conn.commit()
    print(1)
    conn.close()

    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True)