## PROPERTY OF SOUKARYA GHOSH ##
## MAIN FILE FOR THE PROGRAM, CALLS ALL MAJOR METHODS AND INITIATES THE FLASK APP WHILE CALLING HTML FILES ##

from flask import Flask
from flask import Blueprint, render_template
import bikeShareData.parseCSV as pcsv

app = Flask(__name__)

bp = Blueprint(__name__, __name__, template_folder='templates')


## CREATION OF A CITY CLASS, MODULAR SO YOU CAN ADD MORE CITIES IN THE FUTURE FOR BIKESHARE DATA
class City:
    def __init__(self, key, name, lat, lng, scale):
        self.key = key;
        self.name = name;
        self.lat = lat;
        self.lng = lng;
        self.scale = scale


cities = [City('LA', 'Los Angeles', 34.045231, -118.247731, 14)]

cities_by_key = {city.key: city for city in cities}

### PULLS THE LOCATIONS FROM A LOCAL TEXT FILE ###
temp = pcsv.getStartEndCoords()
loc = temp[0]  # [ [[coords], freq] , [[coords], freq] , [[coords], freq] , .... , [[coords], freq] ]  ##FORMAT
locS = temp[2]
locName = temp[1]  # [3005, 3006, 3007 ... ]  ##FORMAT
locNameConv = {3005: '7th & Flower', 3006: 'Olive & 8th', 3007: '5th & Grand', 3008: 'Figueroa & 9th',
               3010: '11th & Maple', 3011: 'Figueroa & Pico', 3013: 'Anaheim & Avalon ',
               3014: 'Union Station West Portal', 3016: 'Los Angeles & Temple', 3018: 'Grand & Olympic',
               3019: '12th & Hill', 3020: 'Hill & Washington', 3022: '3rd & Santa Fe', 3023: '1st & Judge John Aiso',
               3024: 'Hope & 1st', 3025: 'Grand & Washington', 3026: 'Figueroa & Cesar Chavez', 3027: 'Spring & 3rd',
               3028: 'Grand & Temple', 3029: 'Main & 4th', 3030: 'Main & 1st', 3031: '7th & Spring', 3032: 'Hope & 6th',
               3033: 'Main & 9th', 3034: 'Hope & 11th', 3035: 'Figueroa & 8th', 3036: 'Willow St & Mateo St',
               3037: 'Imperial & 7th', 3038: 'Main & 5th', 3040: 'Wilshire & Witmer', 3042: '1st & Central',
               3045: '18th & San Pedro', 3046: '2nd & Hill', 3047: 'Pico & Flower', 3048: '5th & Hewitt',
               3049: '2nd & Figueroa', 3051: '7th & Broadway', 3052: '7th & Bixel', 3054: 'Factory Place & Alameda',
               3056: 'Grand & 14th', 3057: '18th & Figueroa', 3058: 'Industrial St & Mateo St', 3062: '3rd & San Pedro',
               3063: 'Olive & 5th', 3064: 'Grand & 7th', 3065: 'New High & Ord', 3066: 'Spring & College',
               3067: 'Main & 6th', 3068: 'Grand & 3rd', 3069: 'Broadway & 3rd', 3074: 'Hope & Olympic',
               3075: 'Broadway & 9th', 3076: '9th & Los Angeles', 3077: '8th & Wall', 3078: 'Hill & College',
               3081: 'Stanford & 12th', 3082: 'Traction & Rose', 4125: "Banning's Landing", 4126: 'Cabrillo Beach',
               4127: 'Catalina Express', 4129: 'Crafted 22nd St Park', 4130: 'DoubleTree Hotel',
               4131: 'Downtown Harbor', 4132: 'Fanfare Fountain', 4133: "Ports O'Call", 4134: 'USS IOWA',
               4135: 'Waterfront Park (East)', 4136: 'Waterfront Park (West)', 4202: 'Abbot Kinney & Cadiz',
               4204: 'Washington & Abbot Kinney', 4205: 'Venice & Lincoln', 4206: 'California & Lincoln',
               4207: 'Rose & 7th', 4208: 'Rose & Rennie', 4209: 'Rose & Main', 4210: 'Ocean Front Walk & North Venice',
               4211: 'Pacific & North Venice', 4212: 'Windward & Main', 4213: '7th & Westminster',
               4214: 'Ocean Front Walk & Navy', 4215: 'Downtown Santa Monica Expo Line Station',
               4216: '17th St / SMC Expo Line Station', 4220: 'Park & Echo Park', 4227: 'Grand / LATTC',
               4245: 'University & Hoover', 4246: '32nd & Figueroa', 4248: '29th & Ellendale',
               4249: 'Figueroa & McCarthy Way', 4250: 'Severance & Adams', 4254: 'Hoover & 29th',
               4267: '28th & University', 4273: 'Hoover & 32nd', 4222: 'Venice: Artists & Fleas'}


#FIND the most popular end station
popEndStation = [[[[], 0], ""], [[[], 0], ""], [[[], 0], ""], [[[], 0], ""]]  # initialized with placeholders
for entry in range(0, len(loc)):
    tracker = -1  # variable to tell which index of popEndStation to replace
    possibleInserts = 0
    for check in range(0, 4):
        if (popEndStation[check][0][1] < loc[entry][1]):
            if tracker == -1:
                tracker = check
            else:
                if popEndStation[check][0][1] < popEndStation[tracker][0][1]:
                    tracker = check
    if tracker != -1:
        tempEnd = []
        tempEnd.append(loc[entry])
        tempEnd.append(locNameConv[locName[entry]])
        popEndStation[tracker] = tempEnd

##FIND the most popular start station
popStartStation = [[[[], 0], ""], [[[], 0], ""], [[[], 0], ""], [[[], 0], ""]]  # initialized with placeholders
for entry in range(0, len(locS)):
    tracker = -1  # variable to tell which index of popEndStation to replace
    possibleInserts = 0
    for check in range(0, 4):
        if (popStartStation[check][0][1] < locS[entry][1]):
            if tracker == -1:
                tracker = check
            else:
                if popStartStation[check][0][1] < popStartStation[tracker][0][1]:
                    tracker = check
    if tracker != -1:
        tempStart = []
        tempStart.append(locS[entry])
        tempStart.append(locNameConv[locName[entry]])
        popStartStation[tracker] = tempStart


def convertToPercentage(lst):
    #assuming a certain list syntax
    max = 0
    for x in range(0, len(lst)):
        if lst[x][0][1] > max:
            max = lst[x][0][1]

    for x in range(0, len(lst)):
        prc = (100*(lst[x][0][1] / max)) - 10
        lst[x][0][1] = (100*(lst[x][0][1] / max)) - 10

    return lst

def scale(lst):
    # assuming a certain list syntax
    min = 101
    for x in range(0, len(lst)):
        if lst[x][0][1] < min:
            min = lst[x][0][1]
    min = min - 20
    scl = 100/(100-min)
    for x in range(0, len(lst)):
        prc = lst[x][0][1] - min
        lst[x][0][1] = str(prc*scl) + "%"

    return lst


popStartStation = scale(convertToPercentage(popStartStation))
popEndStation = scale(convertToPercentage(popEndStation))


regRiders = pcsv.getRegularRiders()   #182 workdays #84 holidays/weekend days

avgDist, avgTime = pcsv.avgDistance()
avgTime = round((avgTime/60),2)
avgDist = round(avgDist, 2)

avgSpeed = round((avgDist / (avgTime/60)), 1)  #avg speed in miles/hour

pieArrPH = pcsv.pieChartPassHolder()

pieArrTR = pcsv.pieChartTripRoute()

line = pcsv.lineByMonth()

@bp.route('/')
def show_point():
    city = cities_by_key.get('LA')
    return render_template('pointParticle.html', city=city, loc=loc, locName=locName, locNameConv=locNameConv,
                           mapName="Bikeshare Locations")


@bp.route("/start_heat")
def show_heatStart():
    city = cities_by_key.get('LA')
    return render_template('heat.html', city=city, loc=loc, locName=locName, locNameConv=locNameConv,
                           mapName="Starting Station Heatmap")

@bp.route("/stop_heat")
def show_heatStop():
    city = cities_by_key.get('LA')
    return render_template('heat.html', city=city, loc=locS, locName=locName, locNameConv=locNameConv,
                           mapName="Stopping Station Heatmap")


@bp.route("/stats")
def show_stat():
    return render_template('stats.html', popStartStation=popStartStation, popEndStation=popEndStation,
                           regRiders=regRiders, avgDist=avgDist, avgTime=avgTime, avgSpeed=avgSpeed,
                           pageName="Statistics")


@bp.route("/graphs")
def show_grph():
    return render_template('graph.html', pieArrPH=pieArrPH, pieArrTR=pieArrTR, line=line,
                           pageName="Graphs")


@bp.route("/aboutme")
def show_cntct():
    return render_template('aboutme.html', pageName="About Me")


app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
