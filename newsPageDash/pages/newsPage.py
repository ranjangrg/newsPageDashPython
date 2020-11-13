import dash_html_components as html
import dash_core_components as dcc

# for nav bar styling
import dash_bootstrap_components as dbc

from components import navBar, body, footer

from lorem_text import lorem

def generateNewsComponent():
	wordCount = 24
	newsComponent = html.Div(
		html.Div(
			children = [
				html.Img(src="/assets/images/default.png", alt="...", className="img-rounded img-thumbnail"),
				html.H4(lorem.words(5), className="card-title"), 
				html.H6("by " + lorem.words(2), className="card-subtitle mb-2 text-muted"), 
				html.Hr(),
				html.P(lorem.words(wordCount), 
					className="card-text")
			],
			className = "card-body"
		),
		className = "card w-25"
	)
	return newsComponent

def generateNewsListComponent(count):
	preNewsComponent = html.Div("* Randomly generated texts.", className = "lead")
	newsList = []
	for idx in range(count):
		newsList.append(generateNewsComponent())

	newsListComponent = html.Div(
		newsList,
		className = "row",
		style = {
			"padding": "2em"
		},
		key = "news-list-key"
	)
	contentComponent = html.Div(
		children = [
			preNewsComponent,
			newsListComponent
		],
		key = "news-content-key"
	)
	return contentComponent

def getContent():
	navBarComponent = navBar.getComponent()
	bodyComponent = body.getComponent(generateNewsListComponent(8))
	footerComponent = footer.getComponent()

	finalContentChildren = [
		dcc.Location(id="url", refresh=False),
		navBarComponent,	
		bodyComponent,
		footerComponent
	]
	return finalContentChildren