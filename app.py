######----------------------->>>>>>>>>>>>>import libraries>>>>>>>>>>>>-------------------##########
import streamlit as st                                                     
from datetime import datetime
from re import T, U
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker                                                                                  
import pandas as pd                                                             
import plotly.express as px
import matplotlib as mpl
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
from traitlets.traitlets import TraitType
from database import Report                                                       
from visualization import *                                                                                                                                                                                 
from AnalyseData import Analyse   

#--------------------------------------database connection--------------------------------------------------

engine=create_engine('sqlite:///db.sqlite3')            
Session =sessionmaker(bind=engine)                      
sess=Session()   
                                       
######---------------------------------->>>>page- setup>>>>>-------------------------------#########

st.set_page_config(page_title="COVID-19 WORLD VACCINATION PROGRESS VISUALIZATION",page_icon="🏥", layout="wide")
sidebar=st.sidebar
today=datetime.today()
d=today.strftime("%B %d,%Y %H:%M:%S")
sidebar.write(d)
st.sidebar.header('<i>Covid-19 World Vaccination Progress Visualization</i>',anchor="vaccination progress",)
st.sidebar.image('image/tenor.gif',use_column_width=True)

######--------------------------->>>>>>>>>header>>>>>>>>>>>>>------------------------------#########

with st.spinner("Loading Data..."):
    st.markdown("""
        <style>
            .mainhead{
                font-family: Courgette ,Book Antiqua ;
                #letter-spacing:.1px;
                word-spacing:1px;
                color :#e67363; 
                text-shadow: 1px -1px 1px white, 1px -1px 2px white;
                font-size:40px;
            }
        </style>
    """, unsafe_allow_html=True)

with st.spinner("loading data...."):
   st.markdown("""
            <style>
                .detail{
                    font-size:20px;
                    letter-spacing:.1px;
                    word-spacing:1px;
                    font-family:Calibri;
                    color:#74cb35;
                    display:inline-block;
                        }
            </style>
            """, unsafe_allow_html=True)

st.markdown('<h1 class="mainhead"> <i>Covid-19 World Vaccination Progress Visualization</i> </h1> ',unsafe_allow_html=True)
col1,col2=st.beta_columns([5,10])
with col1:
    st.image('image/tenor (1).gif',width=300,)
with col2:
    col=st.beta_container()
    with col:
        st.markdown("""
                    <style>
                        .content{
                                    margin-top:5%;
                                    letter-spacing:.1px;
                                    word-spacing:1px;
                                    color: indianred;
                                    margin-left:5%;}
                    </style>
                    """, unsafe_allow_html=True)
        st.markdown('<p class="content">Hey There ! <br> Welcome To My Project.This Project is all about Covid-19 World Vaccination Progress Visualization.<BR>We will be analyzing the vaccination progress across the world on the basis of country,dates,total vaccinations,people daily vaccinated total vaccinated per hundred,fully vaccinated per million.<br>Our motive is to give you idea about the vaccination progress ,how many peoples are vaccinated ,how many of left.<br>One last tip,if you are on a mobile device,switch over to landscape for viewing ease.Give it a go!</p>',unsafe_allow_html=True )
        st.markdown('<p class="content" style="float:right">MADE BY DIVYA SRIVASTAVA</P>',unsafe_allow_html=True)
st.markdown("")
st.markdown("_______")

#-------------------------------------------------------choice 0--------------------------------------
def AboutProject():
    with  st.spinner("Loading Data............"):
        st.markdown(""" 
            <style>
                .head{
                    font-family: Calibri, Book Antiqua; 
                    font-size:4vh;
                    padding-top:2%;
                    padding-bottom:2%;
                    font-weight:light;
                    color:#ffc68a;
                    #text-align:center;
                    
                    }
            </style>
            """, unsafe_allow_html=True)
        st.markdown('<p class ="head">About Project</p>',unsafe_allow_html=True) 
        st.markdown('<p class="content"> My project is "Covid-19 World Vaccination Progress Visualization" .I can make a data analytics tool.  It is helpful for people who want to get the summarize data for covid 19 vaccination progress .It is also helpful for many researchers ,programmers , health professionals and statistians that tracking the spread of virus in different regions of the world . The aim of this project is to  -<li>Track the progress of covid-19 vaccination</li><li>Vaccination progress and public sentiments about vaccines </li><li>Factors that influence vaccination - politics , demography , economy </li> The project aims to convey the analysis of different ongoing vaccination programs around the globe . The python libraries used in the exploratory data analysis include :-<li>NumPy</li><li>Pandas</li><li>Matplotlib</li><li>folium</li><li>Plotly</li> The objectives of the following project includes <li> Which country started vaccinating its citizens first ?</li><li> Which country has the highest vaccinated people ?</li><li> What are the different categories of vaccines offered ?</li><li> Which vaccine is used by various countries ?</li> </p>',unsafe_allow_html=True)
        st.markdown("_____________________________________________________________________________")

#-----------------------------choice 1--------------------------------------------------#

def viewDataset():
    with  st.spinner("Loading Data............"):
        st.markdown(""" 
            <style>
                .head{
                    font-family: Calibri, Book Antiqua; 
                    font-size:4vh;
                    padding-top:2%;
                    padding-bottom:2%;
                    font-weight:light;
                    color:#ffc68a;
                    #text-align:center;
                    
                    }
            </style>
            """, unsafe_allow_html=True)
      
        st.markdown('<p class="head"> DataSet Used In This Project  </p>',unsafe_allow_html=True)
        st.markdown('<p class="content">This dataset is belongs to vaccination progress of different country  and the vaccine manufacturers in the world which help the peoples who want to get the summarize data of vaccination progress.These datasets we are taken from kaggle website.Here is the link: https://www.kaggle.com/</p>',unsafe_allow_html=True)
        datasets=['Country Data','Manufacturers Data']
        selData=st.selectbox(options=datasets,label='Select Dataset to View')
        if selData == datasets[0]:
            dataframe = analysis_cnt.getDataframe()
            showDetails(dataframe)
        elif selData == datasets[1]:
            dataframe = analysis_mnf.getDataframe()
            showDetails(dataframe)

def showDetails(dataframe):
    with st.spinner("Loading data.........."):
        st.markdown(""" 
                <style>
                    .block{
                            font-family: Book Antiqua; 
                            font-size:24px;
                            padding-top:11%;
                            font-weight:light;
                            color:lightblue;
                        }
                </style>
                    """, unsafe_allow_html=True)
        st.dataframe(dataframe[:5000])
        st.markdown('<p class="head"> Number of rows and columns in dataset </p>',unsafe_allow_html=True)
        cols = st.beta_columns(4)
        cols[0].markdown('<p class="block"> Number of Rows : <br> </p>', unsafe_allow_html=True)
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown('<p class= "block"> Number of Columns : <br></p>', unsafe_allow_html=True)
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.markdown('<p class= "head"> Summary </p>', unsafe_allow_html=True)
        st.markdown("")
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                    'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.markdown('<p class="head">Dataset Columns</p>',unsafe_allow_html=True)
        for col, t in zip(dataframe.columns, types):
                st.markdown(f"## {col}")
                cols = st.beta_columns(4)
                cols[0].markdown('#### Unique Values :')
                cols[1].markdown(f"## {dataframe[col].unique().size}")
                cols[2].markdown('#### Type :')
                cols[3].markdown(f"## {t}")
                st.markdown("___")       
        
#----------------------------------------choice 2------------------------------------------------------
def analyseManufacturers():

    st.header('Vaccine Manufacturers Total Count')

    data = analysis_mnf.getMnfCount()
    st.plotly_chart(plotBar(data, "Pfizer is the most popular Vaccine Manufacturer","No. of Vaccinations", "Manufacturer"), use_container_width=True)

    st.header('Increase in Vaccine Manufacturing over time')
    st.image('plotImages/man_line.png', use_column_width=True)
    st.markdown("---------------------------")

#------------------------------------------------------------choice 3----------------------------------

def countrywiseAnalysis():

    st.header('Overall Total Vaccinations')
    data = analysis_cnt.getCountryVaccinations()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 countries with most Vaccinations','Country Name', 'No. of Vaccinations'))

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total Vaccination in world countries','Country Name', 'No. of Vaccinations'))
    st.markdown("---")

    st.header('Total People Vaccinated')
    data = analysis_cnt.getPeopleVaccinated()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most People Vaccinated',
                             'Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(
        data, 'Total people Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total Fully Vaccinated People')
    data = analysis_cnt.getPeopleFullyVaccinated()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most Fully Vaccinated People','Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total people fully Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Overall Total Vaccinations')
    data = analysis_cnt.getCountryVaccinations_100()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 countries with most Vaccinations','Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total Vaccination in world countries',
                                   'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total People Vaccinated')
    data = analysis_cnt.getPeopleVaccinated_100()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most People Vaccinated','Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total people Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total Fully Vaccinated People')
    data = analysis_cnt.getPeopleFullyVaccinated_100()
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most Fully Vaccinated People','Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total people fully Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'))
    st.markdown("---")

    st.header('Daily Vaccinations in Countries')
    st.image('plotImages/daily_vacc_line.png', use_column_width=True)

    st.header('Fully Vaccinated Peoples in Countries')
    st.image('plotImages/fully_vacc_line.png', use_column_width=True)

    st.header('No. of Vaccinated People in Countries')
    st.image('plotImages/people_vacc_line.png', use_column_width=True)

    st.header('Total Vaccinations done in Countries')
    st.image('plotImages/total_vacc_line.png', use_column_width=True)

    st.header('Vaccination done per 100 in Countries')
    st.image('plotImages/total_per100_line.png', use_column_width=True)
    st.markdown("-----------------------------")

#-----------------------------------------choice 4-----------------------------------------------

def vaccineAnalysis():
    st.header('Country Vaccinations with respect to vaccine Manufacturer')
    selVaccine = st.selectbox(options=analysis_cnt.getVaccines(), label="Choose vaccine to continue")

    st.header('Overall Total Vaccinations')
    data = analysis_cnt.getCountryVaccinations_vaccine(selVaccine)
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 countries with most Vaccinations','Country Name', 'No. of Vaccinations'))

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total Vaccination in world countries','Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total People Vaccinated')
    data = analysis_cnt.getPeopleVaccinated_vaccine(selVaccine)
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most People Vaccinated','Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total people Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")

    st.header('Total Fully Vaccinated People')
    data = analysis_cnt.getPeopleFullyVaccinated_vaccine(selVaccine)
    st.plotly_chart(plotBarh(data.head(20), 'Top 20 Countries with Most Fully Vaccinated People','Country Name', 'No. of Vaccinations'), use_container_width=True)

    st.text("")
    st.plotly_chart(plotChloropeth(data, 'Total people fully Vaccinated in world countries', 'Country Name', 'No. of Vaccinations'), use_container_width=True)
    st.markdown("---")


#----------------------------------sidebar header----------------------

sidebar.header('Choose Your Option')
options = ['About Project','View Dataset', 'Analyse Manufacturers','Analyse Country', 'Analyse Country By Vaccine']
choice = sidebar.selectbox(options=options, label="Choose Action")

with st.spinner("Please Wait for Some Time..."):
    analysis_mnf = Analyse("datasets\manufacturer.csv")
    analysis_cnt = Analyse("datasets\country.csv")

    if choice == options[0]:
        AboutProject()
    elif choice ==  options[1]:
        viewDataset()
    elif choice == options[2]:
        analyseManufacturers()
    elif choice == options[3]:
        countrywiseAnalysis()
    elif choice == options[4]:
        vaccineAnalysis()






















#---------------------------------------univariate -column- selection---------------------------------# 
df=pd.read_csv('datasets\country.csv',parse_dates=['date'],dayfirst=True,index_col="date",)
df.drop(['iso_code','vaccines','source_name','source_website'],axis=1,inplace=True)
df.fillna(value=0,inplace=True)
st.sidebar.header('Choose Actions')
if st.sidebar.checkbox('Univariate analysis '):
    st.sidebar.subheader("Univariate analysis (change over time)")
    cols=['total_vaccinations',
          'people_vaccinated',
          'people_fully_vaccinated',
          'daily_vaccinations_raw',
          'daily_vaccinations',
          'total_vaccinations_per_hundred',
          'people_vaccinated_per_hundred',
          'people_fully_vaccinated_per_hundred',
          'daily_vaccinations_per_million']

    col=st.sidebar.selectbox("select a column ",cols)
    range=st.sidebar.selectbox("select a range to display",['D','3D','W','2W','M','2M'])
    st.markdown(" ")
    st.header("Univariate analysis ( change over time ) 👇")

    st.markdown("")
    sub_df=df[col].resample(range).mean()
    c=st.beta_columns(2)
    c[0].write(f" Univariate analysis  of  {col}  in  range  of  {range} 👇 ")
    c[0].write(sub_df)

    fig=px.bar(sub_df,x=sub_df.index,y=col)
    c[1].plotly_chart(fig,figsize=(7,5))

    st.markdown("______________________________________________________________________")

#----------------------------bivariate -analysis--------------------------------------------------#

cols=['total_vaccinations',
         'people_vaccinated',
         'people_fully_vaccinated',
         'daily_vaccinations_raw',
         'daily_vaccinations',
         'total_vaccinations_per_hundred',
         'people_vaccinated_per_hundred',
         'people_fully_vaccinated_per_hundred',
         'daily_vaccinations_per_million'] 

if st.sidebar.checkbox('Bivariate analysis'):
    st.sidebar.subheader("Bivariate analysis (change over time)")
    selection=st.sidebar.multiselect("select two columns ",cols)
    if len(selection) == 2:
        st.header("Bivariate analysis ( change over time ) 👇")

        fig = px.scatter(df,x=selection[0],y=selection[1])
        
        cols = st.beta_columns(2)
        cols[0].write("Selected columns data and plots")
        cols[0].write(df[[selection[0],selection[1]]])
        cols[1].plotly_chart(fig,use_container_width=True)
        
        st.markdown("_____________________________________")

#--------------------------------comparison -plot--------------------------------------------------#

cols=['total_vaccinations',
         'people_vaccinated',
         'people_fully_vaccinated',
         'daily_vaccinations_raw',
         'daily_vaccinations',
         'total_vaccinations_per_hundred',
         'people_vaccinated_per_hundred',
         'people_fully_vaccinated_per_hundred',
         'daily_vaccinations_per_million'] 
if st.sidebar.checkbox("Comparison Plots"):
    st.sidebar.subheader("Comparison Plots")
    cols =st.sidebar.multiselect("Select Two Columns ",cols)
    kind = st.sidebar.selectbox("Select Plot Type",['area','line','bar','hist','box'])
    if len(cols) >= 2:
        st.header("Comparison Plots 👇")
        fig,ax = plt.subplots(figsize=(7,5))
        c = st.beta_columns(2)
        st.subheader(f"Comparison plots of {cols} , {kind} type 👆")  
    
        c[0].write(df[cols].resample('W').count())
        df[cols].resample('W').sum().plot(kind=kind,ax=ax,legend=True,title=f"{cols[0]} vs {cols[1]}")
        c[1].pyplot(fig)
        st.markdown("__________________________________________________________")
#----------------------------geographic-visualization-------------------------------------------#
if st.sidebar.checkbox("Geographic Visualization"):
    st.sidebar.subheader("Geographic Visualization")
    cols=['total_vaccinations',
    'people_vaccinated',
    'people_fully_vaccinated',
    'daily_vaccinations_raw',
    'daily_vaccinations',
    'total_vaccinations_per_hundred',
    'people_vaccinated_per_hundred',
    'people_fully_vaccinated_per_hundred',
    'daily_vaccinations_per_million']
    col = st.sidebar.selectbox("select a column for map",cols)
    geodata = df.groupby('country')[col].sum()
    st.header("Geographic Visualization 👇")
    if col:
        map = folium.Map(location=[0,0], zoom_start=2)
        map.choropleth(
        geo_data='world_countries.json',
        name='choropleth',
        data=geodata,
        columns=[geodata.index,col],
        key_on='feature.properties.name',
        fill_color='Set1',
        fill_opacity=.5,
        line_opacity=0.2,
        line_color='blue',
        legend_name=col)
        st.subheader(f"Geo Visualization of {col} ")
        folium_static(map,width=1000)
        





























# git clone https://github.com/deepali1232/covid-19-vaccination-progress-app.git