from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/table/1")
def table1():
    return render_template("table1.html")

@app.route("/table/2")
def table2():
    return render_template("table2.html")

@app.route("/table/3")
def table3():
    return render_template("table3.html")

@app.route("/table/4")
def table4():
    return render_template("table4.html")

@app.route("/table/5")
def table5():
    return render_template("table5.html")

@app.route("/table/6")
def table6():
    return render_template("table6.html")

@app.route("/table/7")
def table7():
    return render_template("table7.html")

@app.route("/table/8")
def table8():
    return render_template("table8.html")

@app.route("/table/9")
def table9():
    return render_template("table9.html")

@app.route("/table/10")
def table10():
    return render_template("table10.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)