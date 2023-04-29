from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/members")
def members():
    return {"members": ["Samantha", "Avinash", "Luna", "Sean", "Yong Ho"]}


@app.route("/cars")
def cars():
    return {
        "cars": {
            "Avinash": ["2020 Subaru BRZ PP", "2000 BMW 328CI"],
            "Samantha": ["2005 Toyota Camry 2.4L"],
            "Sean": ["2000 Toyota MR-2 Spyder"],
            "Yong Ho": ["2007 Honda Civic Si (FA5)"],
        },
    }
