
def register_callbacks(app, df, df_clean, df_timelapse):
    """
    Registers all the callbacks for the application.

    Args:
        app: Dash application instance
        df: Main DataFrame
        df_clean: Cleaned DataFrame
        df_timelapse: Timelapse DataFrame
    """
    from callbacks.choropleth import register_choropleth_callbacks
    from callbacks.countries import register_countries_callbacks
    from callbacks.continents import register_continents_callbacks
    from callbacks.global_trends import register_global_callbacks
    
    register_choropleth_callbacks(app, df, df_timelapse)
    register_countries_callbacks(app, df, df_clean)
    register_continents_callbacks(app, df)
    register_global_callbacks(app, df)