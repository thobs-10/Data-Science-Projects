# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 01:31:09 2022

@author: Thobela Sixpence
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# create a function that will shorten the lenghht of category names
# basically we getting rid of countries with fewer developers, developers less than the cutoff
def shorten_categories(categories, cuttoff):
    # have a dictionary to map the categories
    category_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cuttoff:
            # keep the country
            category_map[categories.index[i]] = categories.index[i]
        else:
            category_map[categories.index[i]] = 'Other'
    
    return category_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

@st.cache
def load_data():
    
    # load the dataset
    df = pd.read_csv(r"C:\Users\Cash Crusaders\Desktop\My Portfolio\Projects\Data Science Projects\Data Science Project 1 - Software Developer Salary Prediction\Dataset\survey_results_public.csv")
    # keep the columns we want
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    # get rows of salaey that are not null
    df = df[df["ConvertedComp"].notnull()]
    # drop the null values since they are nnot many
    df = df.dropna()
    # change the name of the salary column so it becomes clear
    df = df[df["Employment"] == "Employed full-time"]
    # drop the employment column
    df = df.drop("Employment", axis=1)


    # shorten the categories
    country_map = shorten_categories(df.Country.value_counts(), 400)
    #  apply the cleaning of country
    df["Country"] = df["Country"].map(country_map)
    # clean the salary column
    df = df[df["ConvertedComp"] <= 250000]
    df = df[df["ConvertedComp"] >= 10000]
    # keep all the countries that not 'Other'
    df = df[df["Country"] != "Other"]
    
    # clean the experience column
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    # clean the education column
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    # use the tuple to rename the column salary so it is less confusing
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    
    return df


# call the function
df = load_data()

# create a function responsible to show the explore page
def explore_page_show():
    
    st.title("Explore Software Engineer Salaries")

    st.write("""### Stack Overflow Developer Survey 2020""")
    
    # get the data from the countries
    data = df["Country"].value_counts()
    
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.write("""#### Number of Data from different countries""")
    
    st.pyplot(fig1)
    
    st.write("""#### Mean Salary Based On Country""")
     
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    
    st.write("""#### Mean Salary Based On Experience""")

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
