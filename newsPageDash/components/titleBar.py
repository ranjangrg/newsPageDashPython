import dash_html_components as html
import dash_core_components as dcc

# for nav bar styling
import dash_bootstrap_components as dbc

def getComponent():
	titleBar = html.Div(
		children = [
			html.Span(
				children = [
					html.Img(
						src="/assets/images/logo.png", 
						className="img-thumbnail rounded",
						style = {
							"width": "4em",
							"position": "relative",
							"bottom": "1em"
						}	
					),
					html.H1("Bonker News", className="display-3", style = {
						"display": "inline-block",
						"position": "relative",
						"left": "0.1em"
					})
				]
			),
			html.Hr(className="my-2")
		],
		style = {
			"padding": "1em"
		},
		key = "title-bar-key"
	)
	return titleBar