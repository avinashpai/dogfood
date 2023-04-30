from flask_restx import Resource, Api, abort
from werkzeug.routing import BaseConverter

api = Api()


@api.route("/members", methods=["GET"])
@api.route("/members/<string:member>", methods=["POST", "DELETE"])
@api.route("/members/<string:member>/<string:new_member>", methods=["PUT"])
class Members(Resource):
    members_list = ["Avinash", "Samantha", "Luna", "Sean", "Yong Ho"]

    def get(self):
        return {"members": self.members_list}

    def post(self, member: str):
        if member not in self.members_list:
            self.members_list.append(member)
            return f"Successfully added {member}"
        else:
            abort(409, "Member already exists")

    def put(self, member: str, new_member: str):
        if member in self.members_list:
            self.members_list[self.members_list.index(member)] = new_member
            return f"Successfully Updated {member} to {new_member}"
        else:
            abort(404, "Member not found")

    def delete(self, member: str):
        if member in self.members_list:
            self.members_list.remove(member)
            return f"Successfully removed {member}"
        else:
            abort(404, "Member not found")


@api.route("/cars", methods=["GET"])
@api.route("/cars/<string:owner>", methods=["GET", "DELETE"])
@api.route("/cars/<string:owner>/<string:car>", methods=["DELETE"])
@api.route("/cars/<string:owner>/<str_list:cars>", methods=["POST"])
@api.route("/cars/<string:owner>/<string:new_car>", methods=["PUT"])
@api.route("/cars/<string:owner>/<string:new_car>/<string:old_car>", methods=["PUT"])
class Cars(Resource):
    catalog = {
        "Avinash": ["2020 Subaru BRZ PP", "2000 BMW 328CI"],
        "Samantha": ["2005 Toyota Camry 2.4L"],
        "Sean": ["2000 Toyota MR-2 Spyder"],
        "Yong Ho": ["2007 Honda Civic Si (FA5)"],
    }

    def get(self, owner: str = None):
        if owner is None:
            return {"cars": self.catalog}
        if owner in self.catalog:
            return {owner: self.catalog[owner]}
        abort(404, "Owner not found")

    def post(self, owner: str, cars: list[str]):
        if owner not in self.catalog:
            self.catalog[owner] = cars
            return f"Added {owner} and their {', '.join(cars)}"
        abort(409, "Owner already exists")

    def delete(self, owner: str):
        if owner in self.catalog:
            del self.catalog[owner]
        abort(404, "Owner not found")

    def delete(self, owner: str, car: str = None):
        if owner in self.catalog:
            if car is None:
                del self.catalog[owner]
                return f"Successfully removed {owner}"

            if car in self.catalog[owner]:
                self.catalog[owner].remove(car)
                return f"Sucessfully removed {car} from {owner}"

            abort(404, "Car not found")
        abort(404, "Owner not found")

    # NOTE: You can own multiple of the same car
    def put(self, owner: str, new_car: str, old_car: str = None):
        if owner in self.catalog:
            if old_car is None:
                self.catalog[owner].append(new_car)
                return f"Added {owner}'s new {new_car}"

            cars = self.catalog[owner]
            if old_car in cars:
                cars[cars.index(old_car)] = new_car
                return f"Replaced {owner}'s old {old_car} with {new_car}"

            abort(404, "Car not found")
        abort(404, "Owner not found")
