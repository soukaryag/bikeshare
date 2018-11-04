## PROPERTY OF SOUKARYA GHOSH ##
## THIS .py FILE HOUSES ALL FUNCTIONS THAT PARSE THE PROVIDED CSV FOR VARIOUS DATA MEASURES ##


import pandas as pd
import geopy.distance

def getStartEndCoords():

    filename = "metro-bike-share-trip-data.csv"

    df = pd.read_csv(filename, sep=",", index_col='Ending Station ID', low_memory=False)
    #columns = df.keys()

    # print(columns)
    # print(df)
    # temp = df['Ending Station ID'].tolist()
    # temp = [x for x in temp if str(x) != 'nan']
    # temp = [int(x) for x in temp]

    # ALL THE STATION IDs AS INTS, CREATED AS A LIST HERE IN THE INTEREST OF SAVING TIME, AS THE CSV WILL NOT CHANGE
    allStations = [3005, 3006, 3007, 3008, 3009, 3010, 3011, 3014, 3016, 3018, 3019, 3020, 3021, 3022, 3023, 3024,
                   3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3042,
                   3045, 3046, 3047, 3048, 3049, 3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3062, 3063,
                   3064, 3065, 3066, 3067, 3068, 3069, 3074, 3075, 3076, 3077, 3078, 3079, 3080, 3081, 3082, 4108]

    geoCodeEnd = []
    for station in allStations:
        temp = []

        freq = len(df.at[float(station), "Ending Station Latitude"])
        lat = (df.at[float(station), "Ending Station Latitude"])[0]
        lng = (df.at[float(station), "Ending Station Longitude"])[0]

        if str(lat) != 'nan' and str(lng) != 'nan':
            temp.append([float(lat), float(lng)])
            temp.append(freq)
            geoCodeEnd.append(temp)



    #STARTING the second read
    dfS = pd.read_csv(filename, sep=",", index_col='Starting Station ID', low_memory=False)

    geoCodeStart = []
    for station in allStations:
        tempS = []

        freqS = len(dfS.at[float(station), "Starting Station Latitude"])
        lat = (dfS.at[float(station), "Starting Station Latitude"])[0]
        lng = (dfS.at[float(station), "Starting Station Longitude"])[0]

        if str(lat) != 'nan' and str(lng) != 'nan':
                tempS.append([float(lat), float(lng)])
                tempS.append(freqS)
                geoCodeStart.append(tempS)



    return geoCodeEnd, allStations, geoCodeStart

def getRegularRiders():
    filename = "metro-bike-share-trip-data.csv"

    df = pd.read_csv(filename, sep=",", low_memory=False)

    a = df.loc[df['Passholder Type'] != "Walk-up"]
    return len(a.index) / 182  ##182 is the number of days in the given period minus weekends and holidays


def avgDistance():
    filename = "metro-bike-share-trip-data.csv"

    df = pd.read_csv(filename, sep=",",  low_memory=False)
    df = df[["Duration", "Starting Station Latitude", "Starting Station Longitude", "Ending Station Latitude", "Ending Station Longitude"]]

    ##DISTANCE CALCULATION MODIFIED FROM STACK OVERFLOW
    sum = 0
    count = 0
    time = 0
    for index, row in df.iterrows():
        lat1 = row["Starting Station Latitude"]
        lat2 = row["Ending Station Latitude"]
        lon1 = row["Starting Station Longitude"]
        lon2 = row["Ending Station Longitude"]
        if str(lat1) != 'nan' and str(lat2) != 'nan' and str(lon1) != 'nan' and str(lon2) != 'nan':
            coords_1 = (lat1, lon1)
            coords_2 = (lat2, lon2)

            dist = geopy.distance.vincenty(coords_1, coords_2).miles
            if dist > 0:
                time = time + row["Duration"]
                sum = sum + dist
                count = count + 1

    return (sum/count), (time/count)


def pieChartPassHolder():
    filename = "metro-bike-share-trip-data.csv"

    df = pd.read_csv(filename, sep=",", low_memory=False)
    df = df[["Passholder Type"]]
    w = len((df.loc[df['Passholder Type'] == "Walk-up"]).index)
    f = len((df.loc[df['Passholder Type'] == "Flex Pass"]).index)
    m = len((df.loc[df['Passholder Type'] == "Monthly Pass"]).index)
    s = len((df.loc[df['Passholder Type'] == "Staff Annual"]).index)

    return [w, f, m, s]


def pieChartTripRoute():
    filename = "metro-bike-share-trip-data.csv"

    df = pd.read_csv(filename, sep=",", low_memory=False)
    df = df[["Trip Route Category"]]
    o = len((df.loc[df["Trip Route Category"] == "One Way"]).index)
    r = len((df.loc[df["Trip Route Category"] == "Round Trip"]).index)

    return [o, r]


def lineByMonth():
    totals = {7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    filename = "metro-bike-share-trip-data.csv"

    df = pd.read_csv(filename, sep=",", converters= {'Start Time': pd.to_datetime}, low_memory=False)
    for index, row in df.iterrows():
        totals[((row["Start Time"]).month)] += 1

    return totals

#print(getRegularRiders())