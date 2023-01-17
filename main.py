from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from csv_class import ReadCSV
from forms import GenerateForm

app = Flask(__name__)
app.secret_key = "TommyShelby"
Bootstrap(app)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_page():
    csv_data = ReadCSV()
    new_form = GenerateForm()
    if new_form.validate_on_submit():
        new_data = [
            new_form.cafe_name.data,
            new_form.cafe_location.data,
            new_form.cafe_open.data,
            new_form.cafe_close.data,
            new_form.cafe_coffee.data,
            new_form.cafe_wifi.data,
            new_form.cafe_power.data
        ]
        csv_data.append_csv(new_data)
        return redirect(url_for('cafe_page'))
    return render_template("add.html", form=new_form)


@app.route("/cafe")
def cafe_page():
    csv_tool = ReadCSV()
    csv_data = csv_tool.read_csv()
    return render_template("cafes.html", cafe_data=csv_data)


if __name__ == "__main__":
    app.run(debug=True)
