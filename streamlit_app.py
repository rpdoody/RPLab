import streamlit as st

page1 = st.Page("home.py", title="Home", icon="⚾")
page2 = st.Page("pages/kbo_sim.py", title="KBO Simulation", icon="📊")
page3 = st.Page("pages/mlb_sim.py", title="MLB Simulation", icon="📈")

pg = st.navigation([page1, page2, page3])
pg.run()
