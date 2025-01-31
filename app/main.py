from flask import Flask
from faker import Faker
from faker.providers.emoji import Provider as EmojiProvider

app = Flask(__name__)
faker = Faker()


@app.route("/")
def hello():
    return faker.emoji()