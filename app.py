from flask import Flask, render_template, request
import model
app = Flask(__name__)

pred_val = 0
@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/', methods = ['POST'])
def submit():
    if request.method == "POST":
        name = request.form["nama_komoditas"]
        tahun = request.form["tahun"]
        tahun = int(tahun)
        pred_val = model.predict(tahun)
        pred_val = "{:.3f}".format(pred_val)
    return render_template("index.html", name = name, tahun = tahun, pred_val = pred_val)


if __name__ == "__main__":
    app.run()