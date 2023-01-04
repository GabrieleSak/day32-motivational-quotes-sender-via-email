import random
import smtplib
from topsecret import *
import datetime as dt

WEEKDAY = 2

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Have a nice day!\n\n{message}"
        )


if day_of_week == WEEKDAY:
    with open("quotes.txt", "r") as quotes_file:
        data = quotes_file.read()
        quotes = data.split("\n")
    quote = random.choice(quotes)
    print(quote)
    send_email(quote)
