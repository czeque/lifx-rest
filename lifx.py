from flask import Flask
from flask_restful import Api, Resource, reqparse

import sys
from time import sleep
from lifxlan import LifxLAN, Light, BLUE, GREEN

app = Flask(__name__)
api = Api(app)

def toggle_light_color(light, interval=1, num_cycles=10):
    original_color = light.get_color()
    rapid = True if interval < 1 else False
    for i in range(num_cycles):
        light.set_color(BLUE, rapid=rapid)
        sleep(interval)
        light.set_color(GREEN, rapid=rapid)
        sleep(interval)
    light.set_color(original_color)


scenes = [
    {
        "name": "den-on",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "den-off",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]


#class Scene(Resource):
#    def get(self, name):
#        for scene in scenes:
#            if(name == scene["name"]):
#                lifx = LifxLAN()
#                devices = lifx.get_lights()
#                bulb = devices[0]
#                bulb.set_power("on")
#                toggle_light_color(bulb, 0.2)
#                return scene["name"] + " activated", 200
#        return "Scene not found", 404

class Scene(Resource):
    def get(self, name):
            if(name == "den-on"):
                light = Light("d0:73:d5:26:91:07", "10.10.1.152")
                toggle_light_color(light, 0.2)
                return "den-on activated", 200
            return "Scene not found", 404

api.add_resource(Scene, "/scene/<string:name>")

app.run(debug=True)
