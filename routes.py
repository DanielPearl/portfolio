from flask import *
from jinja2 import Template
from forms import ContactForm
from flask_mail import Mail, Message

mail = Mail()
app = Flask(__name__)
app.secret_key = "supersecretsecretkey"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'danielaaronpearl@gmail.com'
app.config['MAIL_PASSWORD'] = 'ellie1ellie'

mail.init_app(app)


@app.route("/portfolio/")
def portfolio():
    return render_template('portfolio.html', portfolio="selected")

@app.route("/about/")
def about():
    return render_template('about.html', about="selected")

@app.route("/contact/", methods=['GET','POST'])
def contact():
    form = ContactForm()

    if request.method == "POST":
        if form.validate() == False:

            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='danielaaronpearl@gmail.com', recipients=['danielaaronpearl@gmail.com'])

            msg.body = """
            From: {0} <{1}>
            {2}
            """.format(form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == "GET":
        return render_template('contact.html', form=form, contact="selected")

if __name__ == '__main__':
    app.run(debug=True)
