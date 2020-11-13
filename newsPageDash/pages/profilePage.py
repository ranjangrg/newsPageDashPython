import dash
import dash_html_components as html
import dash_core_components as dcc

# for nav bar styling
import dash_bootstrap_components as dbc

from components import titleBar, navBar, body, footer

pageTitle = html.H1(
	"Profile Page",
	className = "pt-2"
)
testBtn = dbc.Button("Continue", id = "profile-page-btn-id", n_clicks=0)
pageContent = html.Div(
	children = [
		html.P("This is your profile page.", id="profile-page-content-id"),
		testBtn
	]
)

pageComponent = html.Div(
	[
		pageTitle,
		html.Hr(),	
		pageContent,
	],
	className = "mx-5"
)

def getContent():
	titleBarComponent = titleBar.getComponent()
	navBarComponent = navBar.getComponent()
	bodyComponent = body.getComponent(pageComponent)
	footerComponent = footer.getComponent()

	finalContentChildren = [
		dcc.Location(id="url", refresh=False),
		navBarComponent,
		bodyComponent,
		footerComponent
	]
	return finalContentChildren