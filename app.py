from faker import Faker
from flask import Flask

app = Flask(__name__)
faker = Faker()

@app.route("/")
def index() -> str:
    return f"<h1>Hello, {faker.name()}!</h1><h3>{faker.text()}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
