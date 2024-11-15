import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df.loc[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    number_of_bachelors = df['education'].value_counts().loc['Bachelors']
    percentage_bachelors = round(number_of_bachelors/df.shape[0]* 100 ,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[ (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')].shape[0]
    lower_education = df[ (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')].shape[0]

    # percentage with salary >50K
    higher_education_rich = round(df[ ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')].shape[0]/higher_education*100,1)
    lower_education_rich = round(df[ (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate') & (df['salary'] == '>50K')].shape[0]/lower_education*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]

    rich_percentage = round(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0]/num_min_workers*100,1)

    # What country has the highest percentage of people that earn >50K?

    serie1 = df['native-country'].value_counts()
    serie2 = df[df['salary'] == '>50K']['native-country'].value_counts()

    df1 = serie1.reset_index()
    df2 = serie2.reset_index()

    df1.columns = ["Country", "Population"]
    df2.columns = ["Country", "Number of Rich"]

    df_final = pd.merge(df1, df2, on="Country")
    df_final.index = df_final['Country']

    percentage = round(df_final["Number of Rich"] / df_final['Population']* 100,1)

    df_final['Percentage of Rich'] = percentage


    highest_earning_country = df_final['Percentage of Rich'].idxmax()

    highest_earning_country_percentage = df_final['Percentage of Rich'].max()

    # Identify the most popular occupation for those who earn >50K in India.
    selection = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = selection['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data(print_data=True)