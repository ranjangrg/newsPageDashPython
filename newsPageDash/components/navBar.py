import dash_html_components as html
import dash_core_components as dcc

# for nav bar styling
import dash_bootstrap_components as dbc

def getComponent():
	linksComponent = dbc.Row(
		[
			dbc.Col(dbc.NavLink("home", href="/home")),
			dbc.Col(dbc.NavLink("news", href="/news")),
			dbc.Col(dbc.NavLink("profile", href="/profile")),
		],
		no_gutters=True,
		className="ml-auto flex-nowrap mt-3 mt-md-0",
		align="center",
		justify="between"
	)
	navBarComponent = dbc.NavbarSimple(
		linksComponent,
		brand="Bonker News",
		brand_href="/home",
		color="dark",
		dark=True,
		key = "navbar-key"
	)
	return navBarComponent