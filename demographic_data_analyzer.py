import pandas as pd

def calculate_demographic_data(print_data=True):
    # Column names (because adult.data has NO header row)
    columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week",
        "native-country", "salary"
    ]

    # Read data from file (adult.data is comma-separated, just no .csv extension)
    df = pd.read_csv(
        "adult.data",
        names=columns,
        skipinitialspace=True
    )

    # How many people of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df["education"].eq("Bachelors").mean()) * 100, 1
    )

    # What percentage of people with advanced education make more than 50K?
    advanced_edu = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_salary = df["salary"] == ">50K"

    higher_education_rich = round((df[advanced_edu & higher_salary].shape[0] /
                                  df[advanced_edu].shape[0]) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round((df[~advanced_edu & higher_salary].shape[0] /
                                 df[~advanced_edu].shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = int(df["hours-per-week"].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((min_workers[min_workers["salary"] == ">50K"].shape[0] /
                             min_workers.shape[0]) * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_total = df["native-country"].value_counts()
    country_rich = df[df["salary"] == ">50K"]["native-country"].value_counts()

    country_percentage = (country_rich / country_total * 100).fillna(0)
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"] \
        .value_counts().idxmax()

    # Print results (optional)
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
