#import relevant library for getting API data
import requests
import plotly.graph_objs as go
from collections import defaultdict

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """ Connects to the World Bank API, Cleans the Data and Creates plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    #specifying format, lines and timeframe
    payload = {'format': 'json','per_page': '1000', 'date':'1990:2020'}

    #url from where to pick up API data
    r_payload = requests.get('http://api.worldbank.org/v2/country/ARB;AFR;EUU;CAN;NAC;CHN/indicator/SP.POP.TOTL.', params=payload)

    # put the results in a dictionary where each country contains a list of all the x values and all the y values
    # this will make it easier to plot the results
    
    data = defaultdict(list)

    for entry in r_payload.json()[1]:
        # check if country is already in dictionary. If so, append the new x and y values to the lists
        if data[entry['country']['value']]:
            data[entry['country']['value']][0].append(int(entry['date']))
            data[entry['country']['value']][1].append(float(entry['value']))       
        else: # if country not in dictionary, then initialize the lists that will hold the x and y values
            data[entry['country']['value']] = [[],[]] 
    
    #create country list to use
    country_list = []
    for country in data:
        country_list.append(country)

    #create list for graph_one
    graph_one = []

    #create graph one scatter plot
    for country in data:
        graph_one.append(
            go.Scatter(
                x = data[country][0],
                y = data[country][1],
                mode = 'lines',
                name = country
            )
        )

    #create layout one for graph_one
    layout_one = dict(title = 'Total Population <br> per Person 1990 to 2019',
                      xaxis = dict(title = 'Year',
                      autotick=False, tick0=1990, dtick=5),
                      yaxis = dict(title = 'Total Population'),
                      )


    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    

    return figures
