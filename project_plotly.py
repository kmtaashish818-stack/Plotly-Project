import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px 
# python -m streamlit run "E:\python mysirg\intro.py\project_plotly.py"
# python -m streamlit run "E:\python mysirg\intro.py\plotly_project\project_plotly.py"

df=pd.read_csv('E:/python mysirg/intro.py/plotly_project/india.csv')

list_of_state=list(df['State'].unique())
list_of_state.insert(0,'overall India')

st.sidebar.title('India Map')

selected_state=st.sidebar.selectbox('Select a State',list_of_state)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot')

if plot:
    
    st.text('Size represent primary papameter')
    st.text("color represent secondary parameter")
    if selected_state=='overall India':
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,size_max=20,
                              color=secondary,zoom=3,mapbox_style="open-street-map",
                              width=1200,height=500,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=df[df['State']==selected_state]
        fig=px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',size=primary,size_max=20,
                                      color=secondary,zoom=5,mapbox_style="open-street-map",
                                      width=1200,height=500,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)