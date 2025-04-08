import pandas as pd
import pycountry
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
from config import G7_COUNTRIES, EMERGING_COUNTRIES

def register_countries_callbacks(app, df, df_clean):
    """
    Registers callbacks for country comparisons.

    Args:
        app: Dash application instance
        df: Main DataFrame
        df_clean: Cleaned DataFrame
    """
    @app.callback(
        Output('countries-container', 'children'),
        [Input('countries-dropdown', 'value')]
    )
    def update_countries(selected_value):
        country_translation = df.country_translation
        country_color_map = df.country_color_map
        
        if selected_value == 'top10':
            valid_iso3 = {country.alpha_3 for country in pycountry.countries}
            df_filtered = df[df["ISO3"].isin(valid_iso3)]
            
            top_countries = (
                df_filtered.groupby("Country")["Population"]
                .max()
                .sort_values(ascending=False)
                .head(10)
                .index.tolist()
            )
            
            df_top10 = df_filtered[df_filtered["Country"].isin(top_countries)]
            df_top10 = df_top10.sort_values(by=["Year", "Population"], ascending=[True, False])
            
            color_map = {country_translation[country]: country_color_map[country] for country in top_countries}
            
            fig = px.bar(
                df_top10,
                x="Country_FR",
                y="Population",
                color="Country_FR",
                animation_frame="Year",
                range_y=[0, df_filtered["Population"].max()],
                title="Top 10 pays les plus peuplés (ordre décroissant) – 1960 à 2018",
                labels={"Population": "Population", "Country_FR": "Pays", "Year": "Année"},
                color_discrete_map=color_map
            )
            
            fig.update_layout(
                xaxis_tickangle=-45,
                transition_duration=500,
                showlegend=True,
                xaxis={'categoryorder': 'total descending'},
                height=600
            )
        
        elif selected_value == 'g7':
            df_g7 = df_clean[df_clean["Country"].isin(G7_COUNTRIES)].copy()
            
            color_map = {country_translation[country]: country_color_map[country] 
                         for country in G7_COUNTRIES if country in df_clean["Country"].unique()}
            
            fig = px.line(
                df_g7,
                x="Year",
                y="Population",
                color="Country_FR",
                title="Évolution de la population des pays du G7",
                labels={"Population": "Population", "Year": "Année", "Country_FR": "Pays"},
                markers=True,
                color_discrete_map=color_map
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray"),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                showlegend=True,
                height=600
            )
        
        elif selected_value == 'emerging':
            df_emerging = df_clean[df_clean["Country"].isin(EMERGING_COUNTRIES)].copy()
            
            color_map = {country_translation[country]: country_color_map[country] 
                         for country in EMERGING_COUNTRIES if country in df_clean["Country"].unique()}
            
            fig = px.line(
                df_emerging,
                x="Year",
                y="Population",
                color="Country_FR",
                title="Évolution de la population des pays émergents",
                labels={"Population": "Population", "Year": "Année", "Country_FR": "Pays"},
                markers=True,
                color_discrete_map=color_map
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray"),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                height=600
            )
        
        elif selected_value == 'russia':
            russia_df = df_clean[(df_clean["Country"] == "Russian Federation") & (df_clean["Year"] >= 1991)].copy()
            russia_name_fr = country_translation.get("Russian Federation", "Fédération de Russie")
            
            fig = px.scatter(
                russia_df,
                x="Year",
                y="Population",
                title=f"Évolution de la population de la {russia_name_fr} depuis la chute de l'URSS (1991–2018)",
                labels={"Population": "Population", "Year": "Année", "Growth Rate (%)": "Taux de croissance (%)"},
                color="Growth Rate (%)",
                template="plotly"
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray"),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                height=600
            )
        
        elif selected_value == 'rwanda':
            rwanda_df = df_clean[df_clean["Country"] == "Rwanda"].copy()
            rwanda_name_fr = country_translation.get("Rwanda", "Rwanda")
            
            fig = px.scatter(
                rwanda_df,
                x="Year",
                y="Population",
                title=f"Impact du génocide {rwanda_name_fr} sur la population",
                labels={"Population": "Population", "Year": "Année", "Growth Rate (%)": "Taux de croissance (%)"},
                color="Growth Rate (%)",
                template="plotly"
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray"),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                height=600
            )
        
        elif selected_value == 'decline':
            df_fr = df.copy()
            
            pop_1960 = df_fr[df_fr['Year'] == 1960][['Country', 'Country_FR', 'Population']].set_index('Country')
            pop_2018 = df_fr[df_fr['Year'] == 2018][['Country', 'Country_FR', 'Population']].set_index('Country')
            
            pop_comparison = pd.DataFrame({
                'Country_FR': pop_1960['Country_FR'],
                'Population_1960': pop_1960['Population'],
                'Population_2018': pop_2018['Population']
            })
            
            pop_comparison['Growth'] = pop_comparison['Population_2018'] - pop_comparison['Population_1960']
            pop_comparison['Growth_Percentage'] = (pop_comparison['Growth'] / pop_comparison['Population_1960']) * 100
            
            seuil_stagnation = 3
            pop_comparison['Growth_Type'] = pop_comparison['Growth_Percentage'].apply(
                lambda x: 'Stagnation' if 0 <= x < seuil_stagnation else ('Déclin' if x < 0 else 'Croissance')
            )
            
            decline_or_stagnation = pop_comparison[pop_comparison['Growth_Type'].isin(['Stagnation', 'Déclin'])]
            
            fig = px.bar(
                decline_or_stagnation,
                x='Country_FR',
                y='Growth',
                title="Croissance démographique faible ou négative de 1960 à 2018",
                labels={"Growth": "Croissance de la population", "Country_FR": "Pays"},
                color='Growth',
                color_continuous_scale="RdBu"
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray", tickangle=-45),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                height=600
            )
        
        return dcc.Graph(figure=fig)