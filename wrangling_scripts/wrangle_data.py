#import relevant library for getting API data
import requests
import plotly.graph_objs as go
from collections import defaultdict
from wrangling_scripts.clean_plot import clean_plot

def return_figures():
    """Creates plotly visualizations

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