import dash_html_components as html
import dash_core_components as dcc

# for nav bar styling
import dash_bootstrap_components as dbc

def getComponent():
	footerComponent = dbc.NavbarSimple(
		dbc.NavItem(
			"© 2020 Ranjan Gurung.",
			className = "light page-footer font-small text-center small text-muted",
			style = {
				"color": "white"
			}
		),
		color="dark",
		dark=True,
		#fixed = "bottom",
		key = "footer-key"
	)
	return footerComponent