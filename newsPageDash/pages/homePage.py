import dash_html_components as html
import dash_core_components as dcc

# for nav bar styling
import dash_bootstrap_components as dbc

from components import titleBar, navBar, body, footer

# for random paragraphs
from lorem_text import lorem

firstLineContent = html.P("""
	Welcome to our news page. Randomly generated Lorem Ipsum paragrams follows.
"""	
)

pageContent = html.Div(
	[
		firstLineContent,
		html.P(lorem.paragraph()), html.P(lorem.paragraph()), html.P(lorem.paragraph()),
		html.P(lorem.paragraph()), html.P(lorem.paragraph()), html.P(lorem.paragraph()),
		html.P(lorem.paragraph()), html.P(lorem.paragraph()), html.P(lorem.paragraph()),
		html.P(lorem.paragraph()), html.P(lorem.paragraph()), html.P(lorem.paragraph())
	]
)

def getContent():
	navBarComponent = navBar.getComponent()
	titleBarComponent = titleBar.getComponent()
	bodyComponent = body.getComponent(pageContent)
	footerComponent = footer.getComponent()

	finalContentChildren = [
		dcc.Location(id="url", refresh=False),
		navBarComponent,
		titleBarComponent,	
		bodyComponent,
		footerComponent
	]
	return finalContentChildren