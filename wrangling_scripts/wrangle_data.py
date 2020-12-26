#import relevant library for getting API data
import requests
import plotly.graph_objs as go
from collections import defaultdict

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`
def clean_plot(graph_name, layout_name, url_string, format, per_page, date, title, x_label, y_label):
      """
      Cleans and plots graphs from API data of World Bank with Plotly

      Args:
        - url_string (string): url to API data
        - format (string): type of data, xml or json
        - per_page (string): number of results per page
        - date (string): timeframe from year to year
        - graph_name (string): name of graph to be plotted
        - layout_name (string): name of layout for the plotted graph
      Return:
        - graph_name
        - layout_name
      """
      payload = {'format': format,'per_page': per_page, 'date': date}

      r_payload = requests.get(url_string, params=payload)

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
      graph_name = []

      #create graph one scatter plot
      for country in data:
          graph_name.append(
              go.Scatter(
                  x = data[country][0],
                  y = data[country][1],
                  mode = 'lines',
                  name = country
              )
          )

      #create layout one for graph_one
      layout_name = dict(title = title,
                        xaxis = dict(title = x_label,
                        autotick=False, tick0=1990, dtick=4),
                        yaxis = dict(title = y_label),
                        )

      return graph_name, layout_name


def return_figures():
    """ Connects to the World Bank API, Cleans the Data and Creates plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    #graph 1
    graph_one, layout_one = clean_plot(graph_name='graph_one', 
                                        layout_name='layout_one', 
                                        url_string='http://api.worldbank.org/v2/country/ARB;AFR;EUU;CAN;NAC;CHN/indicator/SP.POP.TOTL.', 
                                        format='json', 
                                        per_page='1000', 
                                        date='1990:2020', 
                                        title='Total Population <br> per Person 1990 to 2019', 
                                        x_label='Year', 
                                        y_label='Total Population'
               )
    
    #graph 2
    graph_two, layout_two = clean_plot(graph_name='graph_two',
                                        layout_name='layout_two',
                                        url_string='http://api.worldbank.org/v2/country/ARB;AFR;EUU;CAN;NAC;CHN/indicator/EN.ATM.CO2E.KT.',
                                        format='json',
                                        per_page='1000',
                                        date='1990:2017',
                                        title='CO2 emission <br> per Year 1990 to 2017',
                                        x_label='Year',
                                        y_label='CO2 emission'
                                      )

    #graph 3
    graph_three, layout_three = clean_plot(graph_name='graph_three',
                                        layout_name='layout_three',
                                        url_string='http://api.worldbank.org/v2/country/ARB;AFR;EUU;CAN;NAC;CHN/indicator/AG.LND.FRST.ZS.',
                                        format='json',
                                        per_page='1000',
                                        date='1990:2017',
                                        title='Forest area <br> Percent of Total Land Area 1990 to 2017',
                                        x_label='Year',
                                        y_label='Forest Area'
                                      )

    #graph 4
    graph_four, layout_four = clean_plot(graph_name='graph_four',
                                        layout_name='layout_four',
                                        url_string='http://api.worldbank.org/v2/country/ARB;AFR;EUU;CAN;NAC;CHN/indicator/EG.ELC.RNEW.ZS.',
                                        format='json',
                                        per_page='1000',
                                        date='1990:2015',
                                        title='Renewable Energy Output <br> Percent of Total Energy 1990 to 2015',
                                        x_label='Year',
                                        y_label='Renewable Energy'
                                      )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures