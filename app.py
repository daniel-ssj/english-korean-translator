from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from translator import translate
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

class TextArea(FlaskForm):
    text = TextAreaField('Enter text to translate')
    submit = SubmitField('Translate')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = TextArea()
    value = ''
    if form.is_submitted():
        for key, value in request.form.items():
            value = translate(value)
            break
        print(value)
        return render_template('textarea.html', form=form, value=value)
    return render_template('textarea.html', form=form)

if __name__ == '__main__':
    app.run()
