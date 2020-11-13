import dash_html_components as html
import dash_core_components as dcc

# for nav bar styling
import dash_bootstrap_components as dbc

def getComponent(bodyContent):
	bodyComponent = html.Div(
		html.Div(bodyContent, id = "body-content-id"),
		style = {
			"padding-bottom": "2em",
			"min-height": "90vh"
		},
		className = "mx-3",
		id = "body-id",
		key = "body-key"
	)
	return bodyComponent
