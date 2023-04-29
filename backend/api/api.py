from flask_restx import Resource, Api

api = Api()


@api.route("/members")
class Members(Resource):
    def get(self):
        return {"members": ["Samantha", "Avinash", "Luna", "Sean", "Yong Ho"]}


@api.route("/cars")
class Cars(Resource):
    def get(self):
        return {
            "cars": {
                "Avinash": ["2020 Subaru BRZ PP", "2000 BMW 328CI"],
                "Samantha": ["2005 Toyota Camry 2.4L"],
                "Sean": ["2000 Toyota MR-2 Spyder"],
                "Yong Ho": ["2007 Honda Civic Si (FA5)"],
            },
        }
