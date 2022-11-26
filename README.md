Starting November 28th, 2022, free dynos will no longer be available. This project was on a free plan.

## Installation
The code should run with no issues using Python versions 3.*.

Used extensions/frameworks:
- plotly for python vizualisations
- flask for back-end of web-app
- bootstrap for front-end of web-app
- requests for handling API connection

The code is also deployed to the web with heroku.

## Project Motivation
For this project, I was using World Bank Data to showcase how to connect to an API and deploy a data web-app to share key results with anyone on the web.

## File Descriptions
- myapp.py: basic routing information
- folder static: holds images used in the web-app
- index.html: holdes basic html of the web-app front-end
- \__init__.py: initializes flask from "myapp" with the specified routes
- routes.py: specifies the url and connects back-end with front-end
- wrangle_data.py: code responsible for cleaning data and making plots for web-app
- flask: a virtual environment for deploying the app into the web

## Results
The final data dashboard deployed to the web is available [here](https://pmherpwbdashboard.herokuapp.com/).

## Licensing, Authors, Acknowledgements
I must give credit to World Bank for the data. You can find the data [here](https://data.worldbank.org/indicator).

Licensing for the data and other descriptive information are available [here](https://datacatalog.worldbank.org/public-licenses#:~:text=The%20World%20Bank%20Group%20makes,are%20available%20under%20other%20licenses.).
