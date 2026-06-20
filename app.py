from dash import Dash, dcc, html
import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title="Relación entre PIB per cápita y esperanza de vida"
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Gapminder - Todos los países",
        style={"textAlign": "center"}
    ),
    dcc.Graph(figure=fig)
])

server = app.server

if __name__ == "__main__":
    app.run(debug=True)