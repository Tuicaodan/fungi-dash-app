import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np


# -------------------------------------------------------------------------------------------------------------------
# Filter Data
df_tidy_data = pd.read_csv('./Data/tidy data.csv')
df_tidy_data_wo24 = df_tidy_data.loc[df_tidy_data['Hours'] != 24]
df_AUC_tidy_data = pd.read_csv('./Data/AUC tidy data.csv')
df_Modidif = pd.read_csv('./Data/AUC Modidiff tidy data.csv')
df_Nofungidif = pd.read_csv('./Data/AUC NoFungiDiff tidy data.csv')
df_ZOI_data = pd.read_csv('./Data/ZOI tidy data.csv')
df_ZOI_data = df_ZOI_data.sort_values(['Incubation_time', 'ICMP','BioRep'])
df_ZOI_data_2 = pd.read_csv('./Data/ZOI tidy data.csv')
df_ZOI_data_2 = df_ZOI_data_2.sort_values(['Incubation_time', 'ICMP','BioRep'])

df_ZOI_data_2_fungi = df_ZOI_data_2.loc[df_ZOI_data_2['ICMP'] != "CON"]
df_ZOI_control_data_all = df_ZOI_data_2.loc[df_ZOI_data_2['ICMP'] == 'CON']

ICMP_array = df_tidy_data.sort_values('ICMP')['ICMP'].unique()
CON_index = ICMP_array.size-1
ICMP_array = np.delete(ICMP_array, CON_index)


###########################################################################
# filter pilot data
df_pilot_tidy_data = pd.read_csv('./pilot_test_scripts_and_data/pilot_tidy_data.csv')

df_pilot_tidy_data_wo24 = df_pilot_tidy_data.loc[df_pilot_tidy_data['Hours'] != 24]
df_pilot_AUC_tidy_data = pd.read_csv('./pilot_test_scripts_and_data/pilot_AUC_tidy_data.csv')
df_pilot_AUC_tidy_data = df_pilot_AUC_tidy_data.sort_values(['Incubation_time', 'ICMP','BioRep'])
df_pilot_Modidif = pd.read_csv('./pilot_test_scripts_and_data/pilot_AUC_Modidiff_tidy_data.csv')
df_pilot_Nofungidif = pd.read_csv('./pilot_test_scripts_and_data/pilot_AUC_NoFungiDiff_tidy_data.csv')


df_pilot_ZOI_data = pd.read_csv('./pilot_test_scripts_and_data/pilot_ZOI_tidy_data.csv')
df_pilot_ZOI_data = df_pilot_ZOI_data.sort_values(['Incubation_time', 'ICMP','BioRep'])

df_pilot_ZOI_data_fungi = df_pilot_ZOI_data.loc[df_pilot_ZOI_data['ICMP'] != "CON"]
df_pilot_ZOI_control_data_all = df_pilot_ZOI_data.loc[df_pilot_ZOI_data['ICMP'] == 'CON']

df_pilot_Modidif_ab = df_pilot_Modidif.loc[df_pilot_Modidif['Bacteria'] == 'A. baumannii']
df_pilot_Modidif_ec = df_pilot_Modidif.loc[df_pilot_Modidif['Bacteria'] == 'E. coli']
df_pilot_Modidif_pa = df_pilot_Modidif.loc[df_pilot_Modidif['Bacteria'] == 'P. aeruginosa']
df_pilot_Modidif_sa = df_pilot_Modidif.loc[df_pilot_Modidif['Bacteria'] == 'S. aureus']

AUC_pilot_dif_ab_graph = px.strip(
    data_frame=df_pilot_Modidif_ab,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. A. baumannii (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=400,
)

# img_bytes = AUC_pilot_dif_ab_graph.to_image(format="png")
# AUC_pilot_dif_ab_graph.write_image("/Users/diao_q/Dropbox (Uni of Auckland)/BSL-AntibioticDiscovery/Team Fungi/Judy/Python stuff/venv/images/test1.png")


AUC_pilot_dif_ec_graph = px.strip(
    data_frame=df_pilot_Modidif_ec,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. E. coli (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=400,
)

AUC_pilot_dif_pa_graph = px.strip(
    data_frame=df_pilot_Modidif_pa,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. P. aeruginosa (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=400,
)

AUC_pilot_dif_sa_graph = px.strip(
    data_frame=df_pilot_Modidif_sa,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. S. aureus (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=400,
)

df_pilot_Nofungidif_ab = df_pilot_Nofungidif.loc[df_pilot_Nofungidif['Bacteria'] == 'A. baumannii']
df_pilot_Nofungidif_ec = df_pilot_Nofungidif.loc[df_pilot_Nofungidif['Bacteria'] == 'E. coli']
df_pilot_Nofungidif_pa = df_pilot_Nofungidif.loc[df_pilot_Nofungidif['Bacteria'] == 'P. aeruginosa']
df_pilot_Nofungidif_sa = df_pilot_Nofungidif.loc[df_pilot_Nofungidif['Bacteria'] == 'S. aureus']

AUC_pilot_Nofungidif_ab_graph = px.strip(
    data_frame=df_pilot_Nofungidif_ab,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi vs. A. baumannii (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=400,
)

AUC_pilot_Nofungidif_ec_graph = px.strip(
    data_frame=df_pilot_Nofungidif_ec,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi vs. E. coli (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=400,
)

AUC_pilot_Nofungidif_pa_graph = px.strip(
    data_frame=df_pilot_Nofungidif_pa,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi vs. P. aeruginosa (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=400,
)

AUC_pilot_Nofungidif_sa_graph = px.strip(
    data_frame=df_pilot_Nofungidif_sa,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi vs. S. aureus (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=400,
)

df_noControl_pilot_ZOI_data = df_pilot_ZOI_data.loc[df_pilot_ZOI_data['ICMP'] != "CON"]
df_noControl_pilot_ZOI_data['ICMP'] = 'ICMP ' + df_noControl_pilot_ZOI_data['ICMP'].astype(str)

df_noControl_pilot_ZOI_data_ec = df_noControl_pilot_ZOI_data.loc[df_noControl_pilot_ZOI_data['Bacteria'] == "E. coli"]
df_noControl_pilot_ZOI_data_sa = df_noControl_pilot_ZOI_data.loc[df_noControl_pilot_ZOI_data['Bacteria'] == "S. aureus"]
df_noControl_pilot_ZOI_data_ab = df_noControl_pilot_ZOI_data.loc[df_noControl_pilot_ZOI_data['Bacteria'] == "A. baumannii"]
df_noControl_pilot_ZOI_data_pa = df_noControl_pilot_ZOI_data.loc[df_noControl_pilot_ZOI_data['Bacteria'] == "P. aeruginosa"]

pilot_ZOI_ec_graph = px.strip(
    data_frame=df_noControl_pilot_ZOI_data_ec,
    x= "ICMP",
    y='ZOI_mm',
    hover_data=['Additives', 'Incubation_time', 'TechRep', 'BioRep'],
    title=' Fungi supernatant ZOI again E.coli (mm)',
    color='Additives',
    template='seaborn',
    height=400,
)

pilot_ZOI_sa_graph = px.strip(
    data_frame=df_noControl_pilot_ZOI_data_sa,
    x='ICMP',
    y='ZOI_mm',
    hover_data=['Additives', 'Incubation_time', 'TechRep', 'BioRep'],
    title=' Fungi supernatant ZOI again S. aureus (mm)',
    color='Additives',
    template='seaborn',
    height=400,
)

pilot_ZOI_ab_graph = px.strip(
    data_frame=df_noControl_pilot_ZOI_data_ab,
    x= "ICMP",
    y='ZOI_mm',
    hover_data=['Additives', 'Incubation_time', 'TechRep', 'BioRep'],
    title=' Fungi supernatant ZOI again A. baumannii (mm)',
    color='Additives',
    template='seaborn',
    height=400,
)

pilot_ZOI_pa_graph = px.strip(
    data_frame=df_noControl_pilot_ZOI_data_pa,
    x='ICMP',
    y='ZOI_mm',
    hover_data=['Additives', 'Incubation_time', 'TechRep', 'BioRep'],
    title=' Fungi supernatant ZOI again P. aeruginosa (mm)',
    color='Additives',
    template='seaborn',
    height=400,
)


############################################################################









df_Modidif_ab = df_Modidif.loc[df_Modidif['Bacteria'] == 'A. baumannii']
df_Modidif_ec = df_Modidif.loc[df_Modidif['Bacteria'] == 'E. coli']
df_Modidif_pa = df_Modidif.loc[df_Modidif['Bacteria'] == 'P. aeruginosa']
df_Modidif_sa = df_Modidif.loc[df_Modidif['Bacteria'] == 'S. aureus']


df_noControl_ZOI_data = df_ZOI_data.loc[df_ZOI_data['ICMP'] != "CON"]
df_noControl_ZOI_data['ICMP'] = 'ICMP ' + df_noControl_ZOI_data['ICMP'].astype(str)

df_noControl_ZOI_data_ec = df_noControl_ZOI_data.loc[df_noControl_ZOI_data['Bacteria'] == "E. coli"]
df_noControl_ZOI_data_sa = df_noControl_ZOI_data.loc[df_noControl_ZOI_data['Bacteria'] == "S. aureus"]


AUC_dif_ab_graph = px.strip(
    data_frame=df_Modidif_ab,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. A. baumannii (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=800,
)


AUC_dif_ec_graph = px.strip(
    data_frame=df_Modidif_ec,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. E. coli (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=800,
)

AUC_dif_pa_graph = px.strip(
    data_frame=df_Modidif_pa,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. P. aeruginosa (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=800,
)

AUC_dif_sa_graph = px.strip(
    data_frame=df_Modidif_sa,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. S. aureus (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=800,
)




df_Nofungidif_ab = df_Nofungidif.loc[df_Nofungidif['Bacteria'] == 'A. baumannii']
df_Nofungidif_ec = df_Nofungidif.loc[df_Nofungidif['Bacteria'] == 'E. coli']
df_Nofungidif_pa = df_Nofungidif.loc[df_Nofungidif['Bacteria'] == 'P. aeruginosa']
df_Nofungidif_sa = df_Nofungidif.loc[df_Nofungidif['Bacteria'] == 'S. aureus']

AUC_Nofungidif_ab_graph = px.strip(
    data_frame=df_Nofungidif_ab,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. A. baumannii (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=800,
)

AUC_Nofungidif_ec_graph = px.strip(
    data_frame=df_Nofungidif_ec,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. E. coli (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=800,
)

AUC_Nofungidif_pa_graph = px.strip(
    data_frame=df_Nofungidif_pa,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. P. aeruginosa (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=800,
)

AUC_Nofungidif_sa_graph = px.strip(
    data_frame=df_Nofungidif_sa,
    x='Additives',
    y='AUC Difference',
    hover_data=['ICMP', 'BioRep', 'Incubation_time', 'TechRep'],
    title=' Fungi w Additives vs. S. aureus (AUC difference)',
    color='ICMP',
    template='seaborn',
    height=800,
)



ZOI_noControl_ec_graph = px.strip(
    data_frame=df_noControl_ZOI_data_ec,
    x= "ICMP",
    y='ZOI_mm',
    hover_data=['Additives', 'Incubation_time', 'TechRep', 'BioRep'],
    title=' Fungi supernatant ZOI again E.coli (mm)',
    color='Additives',
    template='seaborn',
    height=400,
)

ZOI_noControl_sa_graph = px.strip(
    data_frame=df_noControl_ZOI_data_sa,
    x='ICMP',
    y='ZOI_mm',
    hover_data=['Additives', 'Incubation_time', 'TechRep', 'BioRep'],
    title=' Fungi supernatant ZOI again S. aureus (mm)',
    color='Additives',
    template='seaborn',
    height=400,
)







# --------------------------------------------------------------------------------------------------------------------
# Lunch Dash
external_stylesheets =['./venv/assets/bWLwgP.css', dbc.themes.SUPERHERO]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

# --------------------------------------------------------------------------------------------------------------------
# Define sections

card_title = dbc.Card(
    [
        dbc.CardBody(
            [
                    html.H1("Stimulating ICMP Fungi with LPS, LTA, and Autoclaved Bacteria", className="display-4"),
                    html.Hr(className="my-2"),
                    html.P("ICMP fungi were incubated with 0.1 or 100 ng/mL LPS or LTA, and autoclaved bacteria to see if this stimulates antibacterial activity by the fungi against Acinetobacter baumannii, Escherichia coli, Pseudomonas aeruginosa, and Staphylococcus aureus."
                           " The fungi were left to grow in PDB with the additives at room temperature for a total of 2 weeks and the supernatants were collected at 3, 7, and 14 days to see whether there were time-dependent effects."
                           " The samples were then incubated with bioluminescent bacteria and light activity was measured at 0, 2, 4, and 6 hours."
                    ),
                html.Hr(className="my-2"),

                html.P(dbc.Button("Learn more", color="primary"), className="lead"),
                ],

        ),


    ],
    color="Primary",
    inverse=True,
)

card_main = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Fungi Supernatant Activities (AUC)", tab_id="tab-3"),
                    dbc.Tab(label="Additives Effects Comparison", tab_id="tab-1"),
                    dbc.Tab(label="Fungi Supernantant Activities (ZOI)", tab_id="tab-4"),
                    dbc.Tab(label="Single Fungi Data", tab_id="tab-2"),
                    dbc.Tab(label="Pilot Data", tab_id="tab-5"),
                    dbc.Tab(label="Pilot Single Fungi Data", tab_id="tab-6"),


                ],
                id="card-tabs",
                card=True,
                active_tab="tab-3",
            )
        ),
        dbc.CardBody(
            html.P(id="card-content", className="card-text"),
        ),

    ],
    color="Primary",
    inverse=True,
    outline=False,
)

# --------------------------------------------------------------------------------------------------------------------
# Setup Layout
app.layout = html.Div([
    # dbc.Row([dbc.Col(jumbotron, width={'size': 10, 'offset': 1})]),
    dbc.Row([dbc.Col(card_title, width={'size': 10, 'offset': 1})]),
    dbc.Row([dbc.Col(card_main, width={'size': 10, 'offset': 1})]),
    ])


# --------------------------------------------------------------------------------------------------------------------
# Tabs callback section
@app.callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")],)

def tab_content(active_tab):


# --------------------------------------------------------------------------------------------------------------------
# Tab 1 content
    if active_tab == 'tab-1':
        children = (

            html.H6("Additives effects comparison:", className="card-subtitle"),
            html.P(
                "An overview of the effects of the additives for all the fungi and all biological replicates compared to no additives.",
                className="card-text",
            ),

            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_dif_ab_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_dif_ec_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_dif_pa_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_dif_sa_graph),
            ]),

        )

# --------------------------------------------------------------------------------------------------------------------
# Tab 5 content
    if active_tab == 'tab-5':
        children = (

            html.H6("Pilot Data", className="card-subtitle"),
            html.P(
                "An overview of the Pilot Data",
                className="card-text",
            ),

            html.H3("Additives effects comparison:", className="card-subtitle"),
            html.P(
                "An overview of the effects of the additives for all the fungi and all biological replicates compared to no additives.",
                className="card-text",
            ),
            html.Br(),

            html.Div([
                dcc.Graph(figure=AUC_pilot_dif_ab_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_pilot_dif_ec_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_pilot_dif_pa_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_pilot_dif_sa_graph),
            ]),

            html.Br(),
            html.H3("Fungi supernatant activities:", className="card-subtitle"),
            html.P(
                "An overview of fungi activity for every condition compared to the 'No fungi' control.",
                className="card-text",
            ),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_pilot_Nofungidif_ab_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_pilot_Nofungidif_ec_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_pilot_Nofungidif_pa_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_pilot_Nofungidif_sa_graph),
            ]),

            #Pilot ZOI data
            html.Br(),
            html.H3("Fungi supernatant ZOI:", className="card-subtitle"),
            html.P(
                "An overview of ZOI activity for the fungi.",
                className="card-text",
            ),
            html.Br(),
            html.Div([
                dcc.Graph(figure=pilot_ZOI_ab_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=pilot_ZOI_ec_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=pilot_ZOI_pa_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=pilot_ZOI_sa_graph),
            ]),



        )

# --------------------------------------------------------------------------------------------------------------------
# Tab 3 content
    if active_tab == 'tab-3':
        children = (

            html.H6("Fungi supernatant activities:", className="card-subtitle"),
            html.P(
                "An overview of fungi activity for every condition compared to the 'No fungi' control.",
                className="card-text",
            ),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_Nofungidif_ab_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_Nofungidif_ec_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_Nofungidif_pa_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=AUC_Nofungidif_sa_graph),
            ]),

        )

# --------------------------------------------------------------------------------------------------------------------
# Tab 4 content
    if active_tab == 'tab-4':
        children = (

            html.H6("Fungi supernatant activities:", className="card-subtitle"),
            html.P(
                "An overview of ZOI activity for the fungi.",
                className="card-text",
            ),
            html.Br(),
            html.Div([
                dcc.Graph(figure=ZOI_noControl_ec_graph),
            ]),
            html.Br(),
            html.Div([
                dcc.Graph(figure=ZOI_noControl_sa_graph),
            ]),

        )

# --------------------------------------------------------------------------------------------------------------------
# Tab 2 content
# single Fungi Data
    if active_tab == 'tab-2':
        children = (
        html.H6("Individual fungi results:", className="card-subtitle"),
        html.P(
            'Choose the ICMP isolate you want to look at along with the incubation time and the bacteria it was tested for activity against.',
            className="card-text",
        ),
        html.Br(),

        html.Label(['Choose the fungi:'], style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='fungiID_dropdown',
                     options=[{'label': x, 'value': x} for x in ICMP_array],
                     value='5181',
                     multi=False,
                     disabled=False,
                     clearable=True,
                     searchable=True,
                     placeholder='Choose the fungi...',
                     className='form-dropdown',
                     style={'width': "100%",
                            'color': 'black', },
                     optionHeight=35,  # height/space between dropdown options
                     ),


        html.Br(),
        html.Label(['Choose the bacteria:'], style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='bacteria_dropdown',
                     options=[
                         {'label': 'A. baumannii', 'value': 'A. baumannii'},
                         {'label': 'E. coli', 'value': 'E. coli'},
                         {'label': 'P. aeruginosa', 'value': 'P. aeruginosa'},
                         {'label': 'S. aureus', 'value': 'S. aureus'},
                     ],
                     value='A. baumannii',
                     multi=False,
                     disabled=False,
                     clearable=False,
                     searchable=False,
                     placeholder='Choose the bacteria...',
                     className='form-dropdown',
                     style={'width': "100%",
                            'color': 'black', },
                     ),
        html.Br(),
        html.H6("AUC graphs:", className="card-subtitle"),
        html.Div([
            dcc.Graph(id='fungi_AUC_graph'),
        ]),

        html.Br(),

        html.H6("ZOI graphs:", className="card-subtitle"),
        html.Div([
            dcc.Graph(id='fungi_ZOI_ec_graph'),
            dcc.Graph(id='fungi_ZOI_sa_graph'),
        ]),

        html.Br(),

        html.H6("growth curves:", className="card-subtitle"),
        html.Br(),
        html.Label(['Choose the Fungi incubation time:'],
                   style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='FungiAge_dropdown',
                     options=[{'label': x, 'value': x} for x in
                              df_tidy_data.sort_values('Incubation_time')['Incubation_time'].unique()],
                     value='Day 3',
                     multi=False,
                     disabled=False,
                     clearable=False,
                     searchable=False,
                     placeholder='Choose the Fungi incubation time...',
                     className='form-dropdown',
                     style={'width': "100%",
                            ''
                            'color': 'black', },
                     ),
        html.Br(),

        html.Label(['Choose the BioRep:'], style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='BioRep_dropdown',
                     options=[{'label': x, 'value': x} for x in df_tidy_data.sort_values('BioRep')['BioRep'].unique()],
                     value=1,
                     multi=False,
                     disabled=False,
                     clearable=False,
                     searchable=False,
                     placeholder='Choose the BioRep...',
                     className='form-dropdown',
                     style={'width': "100%",
                            'color': 'black', },
                     ),
        html.Br(),
        html.Label(['Choose the TechRep:'], style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='TechRep_dropdown',
                     options=[{'label': x, 'value': x} for x in
                              df_tidy_data.sort_values('TechRep')['TechRep'].unique()],
                     value=1,
                     multi=False,
                     disabled=False,
                     clearable=False,
                     searchable=False,
                     placeholder='Choose the TechRep...',
                     className='form-dropdown',
                     style={'width': "100%",
                            'color': 'black', },
                     ),
        html.Br(),
        html.Div([
            dcc.Graph(id='fungi_gc_graph'),
        ]),

    )


# --------------------------------------------------------------------------------------------------------------------
# Tab 6 content
# Pilot single Fungi Data
    if active_tab == 'tab-6':
        children = (
        # html.P(
        #     "Check the single fungi results",
        #     className="card-text",
        # ),
        html.H6("Pilot individual fungi results:", className="card-subtitle"),
        html.P(
            'Choose the ICMP isolate you want to look at along with the incubation time and the bacteria it was tested for activity against.',
            className="card-text",
        ),
        html.Br(),

        html.Label(['Choose the fungi:'], style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='pilot_fungiID_dropdown',
                     options=[{'label': x, 'value': x} for x in df_pilot_tidy_data.sort_values('ICMP')['ICMP'].unique()],
                     value='1155',
                     multi=False,
                     disabled=False,
                     clearable=True,
                     searchable=True,
                     placeholder='Choose the fungi...',
                     className='form-dropdown',
                     style={'width': "100%",
                            'color': 'black', },
                     optionHeight=35,  # height/space between dropdown options
                     ),


        html.Br(),
        html.Label(['Choose the bacteria:'], style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='pilot_bacteria_dropdown',
                     options=[
                         {'label': 'A. baumannii', 'value': 'A. baumannii'},
                         {'label': 'E. coli', 'value': 'E. coli'},
                         {'label': 'P. aeruginosa', 'value': 'P. aeruginosa'},
                         {'label': 'S. aureus', 'value': 'S. aureus'},
                     ],
                     value='A. baumannii',
                     multi=False,
                     disabled=False,
                     clearable=False,
                     searchable=False,
                     placeholder='Choose the bacteria...',
                     className='form-dropdown',
                     style={'width': "100%",
                            'color': 'black', },
                     ),
        html.Br(),
        html.H6("AUC graphs:", className="card-subtitle"),
        html.Div([
            dcc.Graph(id='pilot_fungi_AUC_graph'),
        ]),

        #pilot ZOI data
        html.Br(),

        html.H6("Pilot ZOI graphs:", className="card-subtitle"),
        html.Div([
            dcc.Graph(id='pilot_ZOI_ab_graph'),
            dcc.Graph(id='pilot_ZOI_ec_graph'),
            dcc.Graph(id='pilot_ZOI_pa_graph'),
            dcc.Graph(id='pilot_ZOI_sa_graph'),
        ]),

        html.Br(),

        html.H6("growth curves:", className="card-subtitle"),
        html.Br(),
        html.Label(['Choose the Fungi incubation time:'],
                   style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='pilot_FungiAge_dropdown',
                     options=[{'label': x, 'value': x} for x in
                              df_pilot_tidy_data.sort_values('Incubation_time')['Incubation_time'].unique()],
                     value='Day 1',
                     multi=False,
                     disabled=False,
                     clearable=False,
                     searchable=False,
                     placeholder='Choose the Fungi incubation time...',
                     className='form-dropdown',
                     style={'width': "100%",
                            ''
                            'color': 'black', },
                     ),
        html.Br(),

        html.Label(['Choose the BioRep:'], style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='pilot_BioRep_dropdown',
                     options=[{'label': x, 'value': x} for x in df_pilot_tidy_data.sort_values('BioRep')['BioRep'].unique()],
                     value=1,
                     multi=False,
                     disabled=False,
                     clearable=False,
                     searchable=False,
                     placeholder='Choose the BioRep...',
                     className='form-dropdown',
                     style={'width': "100%",
                            'color': 'black', },
                     ),
        html.Br(),
        html.Label(['Choose the TechRep:'], style={'font-weight': 'bold', "text-align": "center", 'font-size': 18}),
        dcc.Dropdown(id='pilot_TechRep_dropdown',
                     options=[{'label': x, 'value': x} for x in
                              df_pilot_tidy_data.sort_values('TechRep')['TechRep'].unique()],
                     value=1,
                     multi=False,
                     disabled=False,
                     clearable=False,
                     searchable=False,
                     placeholder='Choose the TechRep...',
                     className='form-dropdown',
                     style={'width': "100%",
                            'color': 'black', },
                     ),
        html.Br(),
        html.Div([
            dcc.Graph(id='pilot_fungi_gc_graph'),
        ]),

    )

    return children


# --------------------------------------------------------------------------------------------------------------------
# Single fungi results callback section

@app.callback(
    [Output('fungi_AUC_graph', 'figure'),
    Output('fungi_ZOI_ec_graph', 'figure'),
    Output('fungi_ZOI_sa_graph', 'figure'),
     Output('fungi_gc_graph', 'figure')],
    [Input('fungiID_dropdown', 'value'),
     Input('FungiAge_dropdown', 'value'),
     Input('BioRep_dropdown', 'value'),
     Input('TechRep_dropdown', 'value'),
     Input('bacteria_dropdown', 'value'),
     ]
)
def build_graph(ID_chosen, FungiAge_chosen, BioRep_chosen, TechRep_chosen, Bacteria_chosen):
    df_fungi_ICMP_GC = df_tidy_data_wo24.loc[df_tidy_data_wo24['ICMP'] == str(ID_chosen)]
    df_fungi_age_GC = df_fungi_ICMP_GC.loc[df_fungi_ICMP_GC['Incubation_time'] == str(FungiAge_chosen)]
    df_fungi_BioRep_GC = df_fungi_age_GC.loc[df_fungi_age_GC['BioRep'] == BioRep_chosen]
    df_fungi_SingleRep_GC = df_fungi_BioRep_GC.loc[df_fungi_BioRep_GC['TechRep'] == TechRep_chosen]
    df_fungi_single_GC = df_fungi_SingleRep_GC.loc[df_fungi_SingleRep_GC['Bacteria'] == str(Bacteria_chosen)]

    ConDate = df_fungi_single_GC.iloc[2, 1]
    df_control_data_all = df_tidy_data_wo24.loc[df_tidy_data_wo24['ICMP'] == 'CON']
    df_control_data = df_control_data_all.loc[df_control_data_all['Test_Date'] == ConDate]
    df_control_additives_data = df_control_data.loc[df_control_data['Additives'] == 'No Fungi control']
    df_control_additives_BioRep = df_control_additives_data.loc[df_control_additives_data['BioRep'] == BioRep_chosen]
    df_control_additives_BioRep = df_control_additives_BioRep.loc[
        df_control_additives_BioRep['Incubation_time'] == str(FungiAge_chosen)]
    df_control_additives_BioRep_bac = df_control_additives_BioRep.loc[
        df_control_additives_BioRep['Bacteria'] == str(Bacteria_chosen)]

    df_control_additives_BioRep_bac_TechRep1 = df_control_additives_BioRep_bac.loc[
        df_control_additives_BioRep_bac['TechRep'] == 1]
    df_control_additives_BioRep_bac_TechRep2 = df_control_additives_BioRep_bac.loc[
        df_control_additives_BioRep_bac['TechRep'] == 2]
    df_control_additives_BioRep_bac_TechRep3 = df_control_additives_BioRep_bac.loc[
        df_control_additives_BioRep_bac['TechRep'] == 3]
    df_control_additives_BioRep_bac_TechRep4 = df_control_additives_BioRep_bac.loc[
        df_control_additives_BioRep_bac['TechRep'] == 4]

    df_control_MHB_data = df_control_data.loc[df_control_data['Additives'] == 'MHB control']
    df_control_MHB_BioRep = df_control_MHB_data.loc[df_control_MHB_data['BioRep'] == BioRep_chosen]
    df_control_MHB_BioRep = df_control_MHB_BioRep.loc[
        df_control_MHB_BioRep['Incubation_time'] == str(FungiAge_chosen)]
    df_control_MHB_BioRep_bac = df_control_MHB_BioRep.loc[df_control_MHB_BioRep['Bacteria'] == str(Bacteria_chosen)]
    df_control_MHB_BioRep_bac_TechRep1 = df_control_MHB_BioRep_bac.loc[df_control_MHB_BioRep_bac['TechRep'] == 1]
    df_control_MHB_BioRep_bac_TechRep2 = df_control_MHB_BioRep_bac.loc[df_control_MHB_BioRep_bac['TechRep'] == 2]

    fungi_gc_graph = px.line(
        data_frame=df_fungi_single_GC,
        x="Hours",
        y="RLU",
        color='Additives',
        log_y=True,
        title='ICMP ' + ID_chosen + '(' + FungiAge_chosen + ') vs. ' + Bacteria_chosen + ' Growth Curves, BioRep #' + str(
            BioRep_chosen) + ' TechRep #' + str(TechRep_chosen),
        template='seaborn')
    fungi_gc_graph.add_scatter(x=df_control_additives_BioRep_bac_TechRep1['Hours'],
                               y=df_control_additives_BioRep_bac_TechRep1['RLU'], mode='lines',
                               name='No Fungi control #1', line=dict(color="#C0C0C0"))
    fungi_gc_graph.add_scatter(x=df_control_additives_BioRep_bac_TechRep2['Hours'],
                               y=df_control_additives_BioRep_bac_TechRep2['RLU'], mode='lines',
                               name='No Fungi control #2', line=dict(color="#C0C0C0"))
    fungi_gc_graph.add_scatter(x=df_control_additives_BioRep_bac_TechRep3['Hours'],
                               y=df_control_additives_BioRep_bac_TechRep3['RLU'], mode='lines',
                               name='No Fungi control #3', line=dict(color="#C0C0C0"))
    fungi_gc_graph.add_scatter(x=df_control_additives_BioRep_bac_TechRep4['Hours'],
                               y=df_control_additives_BioRep_bac_TechRep4['RLU'], mode='lines',
                               name='No Fungi control #4', line=dict(color="#C0C0C0"))
    fungi_gc_graph.add_scatter(x=df_control_MHB_BioRep_bac_TechRep1['Hours'],
                               y=df_control_MHB_BioRep_bac_TechRep1['RLU'], mode='lines',
                               name='MHB control #1', line=dict(color="#C0C0C0"))
    fungi_gc_graph.add_scatter(x=df_control_MHB_BioRep_bac_TechRep2['Hours'],
                               y=df_control_MHB_BioRep_bac_TechRep2['RLU'], mode='lines',
                               name='MHB control #2', line=dict(color="#C0C0C0"))

    #*******************************************************************************************************************
    #AUC graph build up
    df_fungi_ICMP_AUC = df_AUC_tidy_data.loc[df_AUC_tidy_data['ICMP'] == str(ID_chosen)]
    # df_fungi_age_AUC = df_fungi_ICMP_AUC.loc[df_fungi_ICMP_AUC['Incubation_time'] == str(FungiAge_chosen)]
    df_fungi_AUC = df_fungi_ICMP_AUC.loc[df_fungi_ICMP_AUC['Bacteria'] == str(Bacteria_chosen)]

    #Pull the control data on the same test date
    df_AUC_control_data_all = df_AUC_tidy_data.loc[df_AUC_tidy_data['ICMP'] == 'CON']

    df_AUC_control_data = []
    TestDate_pool = [x for x in df_fungi_AUC.sort_values('Test_Date')['Test_Date'].unique()]
    for TestDate in TestDate_pool:
        df_AUC_control_data_pool = df_AUC_control_data_all.loc[df_AUC_control_data_all['Test_Date'] == TestDate]
        df_AUC_control_data.append(df_AUC_control_data_pool)

    try:
        df_AUC_control_data = pd.concat(df_AUC_control_data, ignore_index=True)
    except:
        print("Nothing to concat on")

    # df_AUC_control_FungiAge = df_AUC_control_data.loc[
    #     df_AUC_control_data['Incubation_time'] == str(FungiAge_chosen)]
    df_AUC_control_FungiAge_bac = df_AUC_control_data.loc[df_AUC_control_data['Bacteria'] == str(Bacteria_chosen)]

    df_fungi_AUC_wCon = pd.concat([df_fungi_AUC, df_AUC_control_FungiAge_bac], ignore_index=True)


    fungi_AUC_graph = px.box(
        data_frame=df_fungi_AUC_wCon,
        x='Additives',
        y='AUC',
        log_y=True,
        hover_data=['TechRep', 'BioRep'],
        title='ICMP ' + ID_chosen + ' vs. ' + Bacteria_chosen + ' AUC',
        color='Incubation_time',
        # height=600,
        template='seaborn',
        points="all"
    )


    # *******************************************************************************************************************
    # ZOI graph build up

    df_fungi_ICMP_ZOI = df_ZOI_data_2_fungi.loc[df_ZOI_data_2_fungi['ICMP'] == str(ID_chosen)]


    TestDate_pool_ZOI = [y for y in df_fungi_ICMP_ZOI.sort_values('Test_Date')['Test_Date'].unique()]

    df_control_ZOI = []
    for TestDate_ZOI in TestDate_pool_ZOI:
        df_ZOI_control_data = df_ZOI_control_data_all.loc[df_ZOI_control_data_all['Test_Date'] == TestDate_ZOI]
        df_control_ZOI.append(df_ZOI_control_data)

    df_control_ZOI_pool = pd.concat(df_control_ZOI, ignore_index=True)

    df_fungi_ICMP_ZOI_wCON = pd.concat([df_fungi_ICMP_ZOI, df_control_ZOI_pool], ignore_index=True)

    df_fungi_ICMP_ZOI_ec = df_fungi_ICMP_ZOI_wCON.loc[df_fungi_ICMP_ZOI_wCON['Bacteria'] == 'E. coli']
    df_fungi_ICMP_ZOI_sa = df_fungi_ICMP_ZOI_wCON.loc[df_fungi_ICMP_ZOI_wCON['Bacteria'] == 'S. aureus']



    fungi_ZOI_ec_graph = px.strip(
        data_frame=df_fungi_ICMP_ZOI_ec,
        x='Additives',
        y='ZOI_mm',
        hover_data=['Incubation_time', 'TechRep', 'BioRep'],
        title='ICMP ' + ID_chosen + ' vs. E. coli ZOI (mm)',
        color='Incubation_time',
        # height=600,
        template='seaborn',
    )

    fungi_ZOI_sa_graph = px.strip(
        data_frame=df_fungi_ICMP_ZOI_sa,
        x='Additives',
        y='ZOI_mm',
        hover_data=['Incubation_time', 'TechRep', 'BioRep'],
        title='ICMP ' + ID_chosen + ' vs. S. aureus ZOI (mm)',
        color='Incubation_time',
        # height=600,
        template='seaborn',
    )
    return  fungi_AUC_graph, fungi_ZOI_ec_graph, fungi_ZOI_sa_graph, fungi_gc_graph


# --------------------------------------------------------------------------------------------------------------------
# pilot single fungi results callback section

@app.callback(
    [Output('pilot_fungi_AUC_graph', 'figure'),
    Output('pilot_ZOI_ab_graph', 'figure'),
    Output('pilot_ZOI_ec_graph', 'figure'),
    Output('pilot_ZOI_pa_graph', 'figure'),
    Output('pilot_ZOI_sa_graph', 'figure'),
     Output('pilot_fungi_gc_graph', 'figure')],
    [Input('pilot_fungiID_dropdown', 'value'),
     Input('pilot_FungiAge_dropdown', 'value'),
     Input('pilot_BioRep_dropdown', 'value'),
     Input('pilot_TechRep_dropdown', 'value'),
     Input('pilot_bacteria_dropdown', 'value'),
     ]
)
def build_graph(ID_chosen, FungiAge_chosen, BioRep_chosen, TechRep_chosen, Bacteria_chosen):
    df_fungi_ICMP_GC = df_pilot_tidy_data_wo24.loc[df_pilot_tidy_data_wo24['ICMP'] == str(ID_chosen)]
    df_fungi_age_GC = df_fungi_ICMP_GC.loc[df_fungi_ICMP_GC['Incubation_time'] == str(FungiAge_chosen)]
    df_fungi_BioRep_GC = df_fungi_age_GC.loc[df_fungi_age_GC['BioRep'] == BioRep_chosen]
    df_fungi_SingleRep_GC = df_fungi_BioRep_GC.loc[df_fungi_BioRep_GC['TechRep'] == TechRep_chosen]
    df_fungi_single_GC = df_fungi_SingleRep_GC.loc[df_fungi_SingleRep_GC['Bacteria'] == str(Bacteria_chosen)]

    ConDate = df_fungi_single_GC.iloc[2, 1]
    df_control_data_all = df_pilot_tidy_data_wo24.loc[df_pilot_tidy_data_wo24['ICMP'] == 'CON']
    df_control_data = df_control_data_all.loc[df_control_data_all['Test_Date'] == ConDate]
    df_control_additives_data = df_control_data.loc[df_control_data['Additives'] == 'No Fungi control']
    df_control_additives_BioRep = df_control_additives_data.loc[df_control_additives_data['BioRep'] == BioRep_chosen]
    df_control_additives_BioRep = df_control_additives_BioRep.loc[
        df_control_additives_BioRep['Incubation_time'] == str(FungiAge_chosen)]
    df_control_additives_BioRep_bac = df_control_additives_BioRep.loc[
        df_control_additives_BioRep['Bacteria'] == str(Bacteria_chosen)]

    df_control_additives_BioRep_bac_TechRep1 = df_control_additives_BioRep_bac.loc[
        df_control_additives_BioRep_bac['TechRep'] == 1]
    df_control_additives_BioRep_bac_TechRep2 = df_control_additives_BioRep_bac.loc[
        df_control_additives_BioRep_bac['TechRep'] == 2]
    df_control_additives_BioRep_bac_TechRep3 = df_control_additives_BioRep_bac.loc[
        df_control_additives_BioRep_bac['TechRep'] == 3]
    df_control_additives_BioRep_bac_TechRep4 = df_control_additives_BioRep_bac.loc[
        df_control_additives_BioRep_bac['TechRep'] == 4]

    df_control_MHB_data = df_control_data.loc[df_control_data['Additives'] == 'MHB control']
    df_control_MHB_BioRep = df_control_MHB_data.loc[df_control_MHB_data['BioRep'] == BioRep_chosen]
    df_control_MHB_BioRep = df_control_MHB_BioRep.loc[
        df_control_MHB_BioRep['Incubation_time'] == str(FungiAge_chosen)]
    df_control_MHB_BioRep_bac = df_control_MHB_BioRep.loc[df_control_MHB_BioRep['Bacteria'] == str(Bacteria_chosen)]
    df_control_MHB_BioRep_bac_TechRep1 = df_control_MHB_BioRep_bac.loc[df_control_MHB_BioRep_bac['TechRep'] == 1]
    df_control_MHB_BioRep_bac_TechRep2 = df_control_MHB_BioRep_bac.loc[df_control_MHB_BioRep_bac['TechRep'] == 2]

    pilot_fungi_gc_graph = px.line(
        data_frame=df_fungi_single_GC,
        x="Hours",
        y="RLU",
        color='Additives',
        log_y=True,
        title='ICMP ' + ID_chosen + '(' + FungiAge_chosen + ') vs. ' + Bacteria_chosen + ' Growth Curves, BioRep #' + str(
            BioRep_chosen) + ' TechRep #' + str(TechRep_chosen),
        template='seaborn')
    pilot_fungi_gc_graph.add_scatter(x=df_control_additives_BioRep_bac_TechRep1['Hours'],
                               y=df_control_additives_BioRep_bac_TechRep1['RLU'], mode='lines',
                               name='No Fungi control #1', line=dict(color="#C0C0C0"))
    pilot_fungi_gc_graph.add_scatter(x=df_control_additives_BioRep_bac_TechRep2['Hours'],
                               y=df_control_additives_BioRep_bac_TechRep2['RLU'], mode='lines',
                               name='No Fungi control #2', line=dict(color="#C0C0C0"))
    pilot_fungi_gc_graph.add_scatter(x=df_control_additives_BioRep_bac_TechRep3['Hours'],
                               y=df_control_additives_BioRep_bac_TechRep3['RLU'], mode='lines',
                               name='No Fungi control #3', line=dict(color="#C0C0C0"))
    pilot_fungi_gc_graph.add_scatter(x=df_control_additives_BioRep_bac_TechRep4['Hours'],
                               y=df_control_additives_BioRep_bac_TechRep4['RLU'], mode='lines',
                               name='No Fungi control #4', line=dict(color="#C0C0C0"))
    pilot_fungi_gc_graph.add_scatter(x=df_control_MHB_BioRep_bac_TechRep1['Hours'],
                               y=df_control_MHB_BioRep_bac_TechRep1['RLU'], mode='lines',
                               name='MHB control #1', line=dict(color="#C0C0C0"))
    pilot_fungi_gc_graph.add_scatter(x=df_control_MHB_BioRep_bac_TechRep2['Hours'],
                               y=df_control_MHB_BioRep_bac_TechRep2['RLU'], mode='lines',
                               name='MHB control #2', line=dict(color="#C0C0C0"))

    #*******************************************************************************************************************
    #AUC graph build up
    df_fungi_ICMP_AUC = df_pilot_AUC_tidy_data.loc[df_pilot_AUC_tidy_data['ICMP'] == str(ID_chosen)]
    # df_fungi_age_AUC = df_fungi_ICMP_AUC.loc[df_fungi_ICMP_AUC['Incubation_time'] == str(FungiAge_chosen)]
    df_fungi_AUC = df_fungi_ICMP_AUC.loc[df_fungi_ICMP_AUC['Bacteria'] == str(Bacteria_chosen)]

    #Pull the control data on the same test date
    df_AUC_control_data_all = df_pilot_AUC_tidy_data.loc[df_pilot_AUC_tidy_data['ICMP'] == 'CON']

    df_AUC_control_data = []
    TestDate_pool = [x for x in df_fungi_AUC.sort_values('Test_Date')['Test_Date'].unique()]
    for TestDate in TestDate_pool:
        df_AUC_control_data_pool = df_AUC_control_data_all.loc[df_AUC_control_data_all['Test_Date'] == TestDate]
        df_AUC_control_data.append(df_AUC_control_data_pool)

    df_AUC_control_data = pd.concat(df_AUC_control_data, ignore_index=True)

    # df_AUC_control_FungiAge = df_AUC_control_data.loc[
    #     df_AUC_control_data['Incubation_time'] == str(FungiAge_chosen)]
    df_AUC_control_FungiAge_bac = df_AUC_control_data.loc[df_AUC_control_data['Bacteria'] == str(Bacteria_chosen)]

    df_fungi_AUC_wCon = pd.concat([df_fungi_AUC, df_AUC_control_FungiAge_bac], ignore_index=True)


    pilot_fungi_AUC_graph = px.box(
        data_frame=df_fungi_AUC_wCon,
        x='Additives',
        y='AUC',
        log_y=True,
        hover_data=['TechRep', 'BioRep'],
        title='ICMP ' + ID_chosen + ' vs. ' + Bacteria_chosen + ' AUC',
        color='Incubation_time',
        # height=600,
        template='seaborn',
        points="all"
    )

    #*******************************************************************************************************************
    # ZOI graph build up

    try:
        df_pilot_ICMP_ZOI = df_pilot_ZOI_data_fungi.loc[df_pilot_ZOI_data_fungi['ICMP'] == str(ID_chosen)]

        TestDate_pool_pilot_ZOI = [y for y in df_pilot_ICMP_ZOI.sort_values('Test_Date')['Test_Date'].unique()]

        df_pilot_control_ZOI = []
        for TestDate_pilot_ZOI in TestDate_pool_pilot_ZOI:
            df_pilot_ZOI_control_data = df_pilot_ZOI_control_data_all.loc[df_pilot_ZOI_control_data_all['Test_Date'] == TestDate_pilot_ZOI]
            df_pilot_control_ZOI.append(df_pilot_ZOI_control_data)


        df_pilot_control_ZOI_pool = pd.concat(df_pilot_control_ZOI, ignore_index=True)

        df_pilot_ICMP_ZOI_wCON = pd.concat([df_pilot_ICMP_ZOI, df_pilot_control_ZOI_pool], ignore_index=True)

        df_pilot_ICMP_ZOI_ec = df_pilot_ICMP_ZOI_wCON.loc[df_pilot_ICMP_ZOI_wCON['Bacteria'] == 'E. coli']
        df_pilot_ICMP_ZOI_sa = df_pilot_ICMP_ZOI_wCON.loc[df_pilot_ICMP_ZOI_wCON['Bacteria'] == 'S. aureus']
        df_pilot_ICMP_ZOI_ab = df_pilot_ICMP_ZOI_wCON.loc[df_pilot_ICMP_ZOI_wCON['Bacteria'] == 'A. baumannii']
        df_pilot_ICMP_ZOI_pa = df_pilot_ICMP_ZOI_wCON.loc[df_pilot_ICMP_ZOI_wCON['Bacteria'] == 'P. aeruginosa']

        pilot_ZOI_ec_graph = px.strip(
            data_frame=df_pilot_ICMP_ZOI_ec,
            x='Additives',
            y='ZOI_mm',
            hover_data=['Incubation_time', 'TechRep', 'BioRep'],
            title='ICMP ' + ID_chosen + ' vs. E. coli ZOI (mm)',
            color='Incubation_time',
            # height=600,
            template='seaborn',
        )

        pilot_ZOI_sa_graph = px.strip(
            data_frame=df_pilot_ICMP_ZOI_sa,
            x='Additives',
            y='ZOI_mm',
            hover_data=['Incubation_time', 'TechRep', 'BioRep'],
            title='ICMP ' + ID_chosen + ' vs. S. aureus ZOI (mm)',
            color='Incubation_time',
            # height=600,
            template='seaborn',
        )

        pilot_ZOI_ab_graph = px.strip(
                data_frame=df_pilot_ICMP_ZOI_ab,
                x='Additives',
                y='ZOI_mm',
                hover_data=['Incubation_time', 'TechRep', 'BioRep'],
                title='ICMP ' + ID_chosen + ' vs. A. baumannii ZOI (mm)',
                color='Incubation_time',
                # height=600,
                template='seaborn',
            )

        pilot_ZOI_pa_graph = px.strip(
                data_frame=df_pilot_ICMP_ZOI_pa,
                x='Additives',
                y='ZOI_mm',
                hover_data=['Incubation_time', 'TechRep', 'BioRep'],
                title='ICMP ' + ID_chosen + ' vs. P. aeruginosa ZOI (mm)',
                color='Incubation_time',
                # height=600,
                template='seaborn',
        )
    except:
        pilot_ZOI_ec_graph = px.strip()
        pilot_ZOI_sa_graph = px.strip()
        pilot_ZOI_ab_graph = px.strip()
        pilot_ZOI_pa_graph = px.strip()

    return pilot_fungi_AUC_graph, pilot_ZOI_ec_graph, pilot_ZOI_sa_graph, pilot_ZOI_ab_graph, pilot_ZOI_pa_graph, pilot_fungi_gc_graph





if __name__ == "__main__":
    app.run_server(debug=True)

