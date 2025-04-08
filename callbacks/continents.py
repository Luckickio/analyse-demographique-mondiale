from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

def register_continents_callbacks(app, df):
    """
    Registers callbacks for continental analysis.

    Args:
        app: Dash application instance
        df: Main DataFrame
    """
    @app.callback(
        Output('continents-container', 'children'),
        [Input('continents-dropdown', 'value')]
    )
    def update_continents(selected_value):
        continent_translation = df.continent_translation
        continent_color_map = df.continent_color_map
        
        color_map = {continent_translation[continent]: continent_color_map[continent] 
                     for continent in df["Continent"].unique()}
        
        if selected_value == 'continent-evolution':
            continent_population = df.groupby(["Year", "Continent_FR"])["Population"].sum().reset_index()
            continent_population['Population Rank'] = continent_population.groupby("Year")["Population"].rank(
                method="first", ascending=False)
            continent_population = continent_population.sort_values(by=["Year", "Population Rank"])
            
            fig = px.bar(
                continent_population,
                x="Year",
                y="Population",
                color="Continent_FR",
                title="Évolution de la population par continent",
                labels={"Population": "Population", "Year": "Année", "Continent_FR": "Continent"},
                barmode="stack",
                color_discrete_map=color_map
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray"),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                height=600
            )
        
        elif selected_value == 'continent-countries':
            countries_per_continent = df.groupby(["Year", "Continent_FR"])["Country"].nunique().reset_index()
            
            fig = px.bar(
                countries_per_continent,
                x="Continent_FR",
                y="Country",
                color="Continent_FR",
                title="Nombre de pays par continent (1960–2018)",
                labels={"Country": "Nombre de pays", "Continent_FR": "Continent", "Year": "Année"},
                animation_frame="Year",
                color_discrete_map=color_map
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray"),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                transition_duration=500,
                height=600
            )
        
        return dcc.Graph(figure=fig)