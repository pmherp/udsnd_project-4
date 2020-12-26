#import relevant libraries
import requests
import plotly.graph_objs as go
from collections import defaultdict



def clean_plot(graph_name, layout_name, url_string, format, per_page, mrv, title, x_label, y_label):
      """
      Cleans and plots graphs from API data of World Bank with Plotly

      Args:
        - url_string (string): url to API data
        - format (string): type of data, xml or json
        - per_page (string): number of results per page
        - mrv (string): most recent values (year)
        - graph_name (string): name of graph to be plotted
        - layout_name (string): name of layout for the plotted graph
      Returns:
        - graph_name
        - layout_name
      """
      payload = {'format': format,'per_page': per_page, 'mrv': mrv}

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
