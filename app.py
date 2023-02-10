import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='StartUp Analysis')

df = pd.read_csv('startup_cleaned.csv')


# converting to datetime--------------
df['date'] =pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month               
df['year'] = df['date'].dt.year


# #=============loading oveall analysisi when btn0 pressed================
#============================================================================
def load_overall_analysis():
    st.title('Overall analysis')
    st.markdown("Year 2015-2020")

    #total invested amount
    total = round(df['amount'].sum())

    #max amount infused in startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).values[0]

    #On an avg indian startup me kitne paise lagte hai
    avg_funding = df.groupby('startup')['amount'].sum().mean()

    #total no of satartups
    num_startups = df['startup'].nunique(())

    # st.markdown('#Similar Investors')

# 1 dusre ke niche a rahe make colmns
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Total', str(total) + 'Cr')
    with col2:
        st.metric('Max', str(max_funding) + 'Cr')      
    with col3:
        st.metric('Avg', str(round(avg_funding)) + 'Cr') 
    with col4:
        st.metric('Funded Startups', num_startups) 


# #-----------for plotting mom ------------------------
    st.header('MOM graph')

    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig5, ax5 = plt.subplots(figsize=(15,15))
    ax5.plot(temp_df['x_axis'], temp_df['amount'])
    plt.xticks(rotation=90)
    st.pyplot(fig5)


    st.header('Top sectors')
    selected_option = st.selectbox('select type', ['By count', 'By Invested amount'])
    if selected_option == 'By count':
        temp_df = df.groupby('vertical')['amount'].count().sort_values(ascending=False).head()

    else:
        temp_df = df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head()

    fig6, ax6 = plt.subplots(figsize=(10,10))
    ax6.pie(temp_df, labels=temp_df.index, autopct='%0.1f%%')
    st.pyplot(fig6)



    #-------------------city wise funding----------------------------
    city_funding=df[~(df['amount']==0)].groupby('city')['amount'].sum().sort_values(ascending=False)
    st.header('City Wise Funding')
    city_wise_funding_btn=st.selectbox('Type of Data',['DataFrame','Bar Graph'])
    if city_wise_funding_btn=='DataFrame':
        st.dataframe(city_funding)

    else:
        fig7, ax7 = plt.subplots(figsize=(20,20))
        ax7.bar(city_funding.index,city_funding.values,log= True)
        ax7.set_xlabel('Citys')
        ax7.set_ylabel('Crore Rupees')
        plt.xticks(rotation=90)
        st.pyplot(fig7)




#--------------------------year wise and overall (pie)-----------------------------

    st.title('Top Startups ')

    selected_option = st.selectbox('Select Type',['select_one','yearly','Overall'])
    if selected_option == 'yearly':

        st.header('Top startups from year 2015-2020')
        col1, col2 = st.columns(2)
        with col1:
            temp_df=df[df['year'] == 2015].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)

            fig9, ax10 = plt.subplots(figsize=(8,8))
            ax10.pie(temp_df, labels=temp_df.index, autopct='%0.1f%%')
            plt.title('year - 2015')
            st.pyplot(fig9)

        with col2:
            temp_df=df[df['year'] == 2016].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)

            fig9, ax10 = plt.subplots(figsize=(8,8))
            ax10.pie(temp_df, labels=temp_df.index, autopct='%0.1f%%')
            plt.title('year - 2016')
            st.pyplot(fig9)



        col3, col4 = st.columns(2)
        with col3:
            temp_df=df[df['year'] == 2017].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)

            fig9, ax10 = plt.subplots(figsize=(8,8))
            ax10.pie(temp_df, labels=temp_df.index, autopct='%0.1f%%')
            plt.title('year - 2017')
            st.pyplot(fig9)

        with col4:
            temp_df=df[df['year'] == 2018].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)

            fig9, ax10 = plt.subplots(figsize=(8,8))
            ax10.pie(temp_df, labels=temp_df.index, autopct='%0.1f%%')
            plt.title('year - 2018')
            st.pyplot(fig9)


        col5, col6 = st.columns(2)
        with col5:
            temp_df=df[df['year'] == 2019].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)

            fig9, ax10 = plt.subplots(figsize=(8,8))
            ax10.pie(temp_df, labels=temp_df.index, autopct='%0.1f%%')
            plt.title('year - 2019')
            st.pyplot(fig9)


        with col6:
            temp_df=df[df['year'] == 2020].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)

            fig9, ax10 = plt.subplots(figsize=(8,8))
            ax10.pie(temp_df, labels=temp_df.index, autopct='%0.1f%%')
            plt.title('year - 2020')
            st.pyplot(fig9)

    elif selected_option =='Overall':
        temp_df=df.groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        fig10, ax11 = plt.subplots(figsize=(10,10))
        ax11.pie(temp_df, labels=temp_df.index, autopct='%0.1f%%')
        st.pyplot(fig10)



# ====================loading Startup when button clickes=============================
#===================================================================================

def load_starutp_details(startup):
    st.title(startup)                #startup name done


#INDUSTRY
    df_temp=df.set_index('startup')
    st.dataframe(df_temp[df_temp.index == startup][['vertical', 'subvertical', 'city']])


#FUNDING ROUND
    st.title('Funding Rounds')
    st.dataframe(df_temp[df_temp.index == startup][['date', 'round', 'investors']])


#SIMILAR INVESTORS
    st.title('Similar Investors')
    df_temp1=df.set_index('startup')
    temp_df2 = df_temp1[df_temp1.index ==startup]['vertical'].values[0]
    st.dataframe(df_temp1[df_temp1['vertical'].isin([temp_df2])][['vertical', 'subvertical', 'city']].head())




# ====================loading investors when button clickes=============================
#===================================================================================
def load_investor_details(investor):
    st.title(investor)

#------------------ load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

#----------biggest investments
    col1, col2 = st.columns(2)

    with col1:
        # biggest investments
        big_series =df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots(figsize=(10,10))
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)


#------------for vertical------------------------------------
    with col2:
        verical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()

        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots(figsize=(10,10))
        ax1.pie(verical_series,labels=verical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)



    col3, col4 = st.columns(2)

    with col3:
#------------for city------------------------------------
        top_cities  = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()

        st.subheader('cities invested in')
        fig3, ax3 = plt.subplots(figsize=(10,10))
        ax3.pie(top_cities,labels=top_cities.index,autopct="%0.01f%%")
        st.pyplot(fig3)

    with col4:
#------------stage wala/round------------------------------------
        top_stages  = df[df['investors'].str.contains('investors')].groupby('round')['amount'].sum()

        st.subheader('Stages invested in')
        fig4, ax4 = plt.subplots(figsize=(10,10))
        ax4.pie(top_stages,labels=top_stages.index,autopct="%0.01f%%")

        st.pyplot(fig4)
    

    print(df.info())

    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YoY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)

    st.pyplot(fig2)


# #--------------------similar investors ---------------------------------
    # st.title('Similar Analysis')
    
#----------------------------------------------------


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One',['Select one','Overall Analysis', 'StartUp', 'Investor'])


#Note -- > refer ipynb  #investror_list
investors_list = sorted(set(df['investors'].str.split(',').sum()))
del investors_list[0]          #run only once


if option == 'Select one':
    st.title('Funding Analysis of Indian Startups')
    st.subheader('From 2015-2020')
    st.image('https://i.brecorder.com/primary/2022/01/61d3ea060de25.jpg')

elif option == 'Overall Analysis':
    load_overall_analysis()


elif option == 'StartUp':
    select_startup =st.sidebar.selectbox('select startUp', sorted(df['startup'].unique().tolist()))
    btn1 =st.sidebar.button('Find Startup Details')
    if btn1:
        load_starutp_details(select_startup)


else: #option== 'investor':
    selected_investors =st.sidebar.selectbox('Select Startup',investors_list)
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investors)





