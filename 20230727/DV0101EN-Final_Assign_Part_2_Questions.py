import dash
from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas as dataframe
df = pd.read_csv('historical_automobile_sales.csv')

# Get unique list of years in the table
year_list = df['Year'].unique().tolist()

# Define dropdown properties for Dash Core Components
# Reference: https://dash.plotly.com/dash-core-components
dropdown_statistics = dcc.Dropdown(
    id='dropdown-statistics',
    options=['Recession Period Statistics', 'Yearly Statistics'],
    value='Recession Period Statistics'
)

select_year = dcc.Dropdown(
    id='select-year',
    options=year_list,
    value='Select Year'
)

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Statistics Dashboard"

# app layout
app.layout = html.Div([
    html.H1('Automobile Statistics Dashboard'),
    html.Div([
        html.Label('Select Statistics:'),
        dropdown_statistics
    ]),
    html.Div([
        select_year
    ]),
    html.Div([
        html.Div(
            id='output-container',
            className='chart-grid',
            style={'display': 'flex', 'flexWrap': 'wrap'}
        )
    ]),
])


@callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def disable_year(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    else:
        return True


@callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-year', component_property='value'),
     Input(component_id='dropdown-statistics', component_property='value')]
)
def update_bar_chart(input_year, selected_statistics):
    if selected_statistics == 'Recession Period Statistics':
        recession_data = df[df['Recession'] == 1]

        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        fig1 = dcc.Graph(figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
                                        title='Automobile sales fluctuate over Recession Period'))

        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        fig2 = dcc.Graph(figure=px.bar(average_sales, x='Vehicle_Type', y='Automobile_Sales',
                                       title='average number of vehicles sold by vehicle type'))

        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        fig3 = dcc.Graph(figure=px.pie(exp_rec, names='Vehicle_Type', values='Advertising_Expenditure',
                                       title='total expenditure share by vehicle type during recessions'))

        # Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        # ................
        # ...................

        return fig1, fig2, fig3

    elif selected_statistics == 'Yearly Statistics':

        yearly_data = df[df['Year'] == input_year]

        # plot 1 Yearly Automobile sales using line chart for the whole period.
        yas = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
        chart1 = dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales'))

        # Plot 2 Total Monthly Automobile sales using line chart
        chart2 = dcc.Graph(figure=px.line(yearly_data, x='Month', y='Automobile_Sales'))

        # Plot bar chart for average number of vehicles sold during the given year
        avr_data = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        chart3 = dcc.Graph(figure=px.bar(avr_data, x='Vehicle_Type', y='Automobile_Sales',
                                         title='Average Vehicles Sold by Vehicle Type in the year {}'.format(
                                             input_year)))

        # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        chart4 = dcc.Graph(figure=px.pie(exp_data, values='Advertising_Expenditure', names='Vehicle_Type',
                                         title='Total Advertisement Expenditure'))

        return chart1, chart2, chart3, chart4
    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)
