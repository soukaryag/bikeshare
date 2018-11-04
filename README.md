# Bike Share Data

Welcome to my webapp for the Los Angeles Bike Share program.
This app is meant to inform you about various usage statistics within the Bike Share business.
This app was built using the Python Flask library in conjunction with html5, css, and javascript.
There is also an extensive use of the Pandas and Numpy libraries for Python for data analysis.
The app is deployed using Heroku, and can be visited here:
<a target="_blank">https://bikeshare-data.herokuapp.com/</a>

*Please keep in mind that this is on a free server, so long load times and potential crahses with too much load are to be expected*

## The Website
<b>Home</b>

Explore the map of Los Angeles with markers specifying Bike Share locations. 
Switch to the heat map modes to see which stops are the most popular among customers.

<b>Navigation</b>

Navigate the website using the slide out navigation bar housed in the top banner.
Or simply use the links in the footer for easy access to any page!

<b>Statistics and Graphs</b>

View various metrics about the Bike Share business by going to the 'Statistics' or 'Graphs'
page. Use the 'Click Arrow to View' button to bring up the various cards housing the 
information. A short description and implication of each metric is provided in the page
as well!

<b>About Me</b>

Visit this page to find out more about me and to reach out to me as well!

## The Code
<b>deploy.py</b>:
This is the main file. The Flask app is initialized here with a blueprint, the html code is called for each page and the blueprint is applied to the app to create the whole of the website

<b>parseCSV.py</b>:
This python file is heavily based around the Pandas library, using it parse and return the data of interest. This file houses the various methods that are called in deploy.py asking for certain types of data (i.e. average distance, regular riders, etc.)

<b>retLocations.py</b>:
This file coverts all locations from the csv into a JSON structure and returns it to deploy.py for ease of use.

<b>templates</b>:
This folder houses all of the html files, which include JavaScript code to perform the various front-end functions of the website

<b>static\css</b>:
This folder houses all of the CSS code to beautify the webapp. NOTE: the CSS does not work well with Safari, please use Firefox or Chrome for best performance. A good portion of the CSS code is taken from various online sources and modified to fit my usecase.

<b>static\image</b>:
Includes the images from https://pxhere.com/ that make up the banners on each page of the  website.

<b>static\js</b>:
Houses a single external JavaScript file that allows info boxes to be shown on the map rendering on the Home page.

<b>metro-bike-share-trip-data.csv</b>:
The main data source for all of the analysis, some external data used from https://bikeshare.metro.net/ and https://www.wunderground.com/history/monthly/us/ca/los-angeles-downtown/KCQT

<b>Procfile</b>
Allows for webapp to be deployed to Heroku

<b>requirements.txt</b>
List of all the external libraries used in the process of building the site.
