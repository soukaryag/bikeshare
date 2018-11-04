import json
import os

def run():
    crdir = os.getcwd()
    os.chdir("C:/Users/souka/Desktop/bikeshare/bikeshare/views")
    fl = open("locations.txt", "r")
    for line in fl:
        l = line
    fl.close()
    line = line.replace("'", "\"")
    line = line.replace("&", "and")
    json_acceptable_string = line.replace(":", "")
    data = json.loads(json_acceptable_string)
    os.chdir(crdir)
    return data