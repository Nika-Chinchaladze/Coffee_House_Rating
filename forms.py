from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL


MY_COFFEE = [("☕", "☕"), ("☕☕", "☕☕"), ("☕☕☕", "☕☕☕"), ("☕☕☕☕", "☕☕☕☕")]
MY_WIFI = [("💪", "💪"), ("💪💪", "💪💪"), ("💪💪💪", "💪💪💪"), ("💪💪💪💪", "💪💪💪💪")]
MY_POWER = [("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"), ("🔌🔌🔌🔌", "🔌🔌🔌🔌")]


class GenerateForm(FlaskForm):
    cafe_name = StringField("Cafe Name", validators=[DataRequired()])
    cafe_location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(),
                                                                                  URL(message="Invalid URL")])
    cafe_open = StringField("Opening Time e.g. 10:00AM", validators=[DataRequired()])
    cafe_close = StringField("Closing Time e.g. 7:30PM", validators=[DataRequired()])
    cafe_coffee = SelectField("Coffee Rating", choices=MY_COFFEE, validators=[DataRequired()])
    cafe_wifi = SelectField("WiFi Strength Rating", choices=MY_WIFI, validators=[DataRequired()])
    cafe_power = SelectField("Power Socket Availability", choices=MY_POWER, validators=[DataRequired()])
    submit = SubmitField("Submit")
