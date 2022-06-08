import pandas as pd
import webbrowser
# !pip install dash
import dash
from dash import html
from dash.dependencies import Input, Output


# Declaring Global variables
project_name = None
app = dash.Dash()

# Defining My Functions
def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('scrappedReviews.csv')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_app_ui():
    main_layout = html.Div(
    [
    html.H1(id='Main_title', children = "Sentiment Analysis with Insights"),
    html.Button(id= 'button_review', children = 'Find Review', n_clicks=0)
    ]    
    )
    
    return main_layout

'''
Event Handling 
When some clicks the button call my method update_app_ui

Wiring 
Object      Event    Function 
Button      Click    update_app_ui

Decorators and callbacks mechanism is a way to implment wiring in python
Input  === Arguments to your callback
Output === return of your callback 

'''
@app.callback(
    Output( 'button_review'   , 'children'     ),
    [
    Input( 'button_review'    ,  'n_clicks'    )
    ]
    )
def update_app_ui(n_clicks):
    
    print("Data Type = ", str(type(n_clicks)))
    print("Value = ", str(n_clicks))
    
    if (n_clicks > 0 ):
        return "Someone has clicked the button = " + str(n_clicks) + " times" 
    else:
        return "Sentiment Analysis with Insights"



# Main Function to control the Flow of your Project
def main():
    print("Start of your project")
    load_model()
    open_browser()
    #update_app_ui()
    
    
    global scrappedReviews
    global project_name
    global app
    
    project_name = "Sentiment Analysis with Insights"
    #print("My project name = ", project_name)
    #print('my scrapped data = ', scrappedReviews.sample(5) )
    
    # favicon  == 16x16 icon ----> favicon.ico  ----> assests
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server()
    
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
    
        
# Calling the main function 
if __name__ == '__main__':
    main()