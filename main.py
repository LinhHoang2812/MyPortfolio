from flask import Flask, render_template, request
import smtplib
import os

my_email= os.environ["EMAIL"]
password= os.environ["PASSWORD"]

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="zoeylinh2812@gmail.com",
                                msg=f"Subject: New Message\n\nName:{name}\nEmail:{email}\nMessage:{message}")

        alert = "Succesfully sent your message"
        return render_template("index.html", alert=alert)

    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)