import dash
from dash import dcc, html
from config import EXTERNAL_STYLESHEETS, PORT
from data_processing import load_and_process_data
from layouts import create_layout
from callbacks import register_callbacks

df, df_clean, df_timelapse = load_and_process_data()

app = dash.Dash(__name__, 
                external_stylesheets=EXTERNAL_STYLESHEETS,
                title="Analyse Démographique Mondiale")

app.layout = create_layout()

register_callbacks(app, df, df_clean, df_timelapse)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=PORT)