import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc

# for nav bar styling
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import pandas as pd

#from components import newsList, footer
from pages import homePage, newsPage, profilePage


# for nav bar styles
from bootstrapThemes import bootstrapThemes
currentStyleCSS = bootstrapThemes[5]
app = dash.Dash(__name__, external_stylesheets=[currentStyleCSS])

finalContentChildren = homePage.getContent()

app.layout = html.Div(
	children = finalContentChildren,
	id = "main-app-div"
)

@app.callback(
	dash.dependencies.Output("main-app-div", "children"),
	[
		dash.dependencies.Input("url", "pathname")
	]
)
def renderPageFromUrl(path):
	if (path == "/news"):
		return newsPage.getContent()
	elif (path == "/profile"):
		return profilePage.getContent()
	return homePage.getContent()

if __name__ == '__main__':
	app.run_server(host="192.168.0.67", port=3000, debug=True)