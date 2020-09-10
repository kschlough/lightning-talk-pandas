# steps:
# vagrant & navigate to src
# virtualenv env
# source env/bin/activate
# pip install pandas
# python3
# import pandas as pd

# test in interactive mode:
# import pandas as pd
# >>> d = {'col1': [1, 2], 'col2': [3, 4]}
# >>> df = pd.DataFrame(data=d)
# >>> print(df)


# sample pandas code
print("Create a dataframe from a dictionary using PANDAS:")
# import pandas library, once installed in virtual env
import pandas as pd
print("-------------------------------------------")
print("Number of animals on the farm each year")
# 
llamas = {"2020":16, "2019":30, "2018":5}
ferrets = {"2020":62, "2019":44, "2018":13}
# default indexing in the lefthand column, I wanted mine to be years
farm = {"llamas":llamas, "ferrets":ferrets}

# df stands for dataframe, pd was how we imported pandas above
df = pd.DataFrame(farm)
print(df)

# now try with a csv
pd.read_csv('animals_test_csv - Sheet1.csv')

# let's try with a bigger file - sample csv from https://support.spatialkey.com/spatialkey-sample-csv-data/
# company funding records
pd.read_csv('TechCrunchcontinentalUSA.csv')

# if you're in interactive, can save csv dataframe as a variable
# >>> df = pd.read_csv('TechCrunchcontinentalUSA.csv')
# >>> print(df)

# get info about your dataframe, such as:
# df.info() = columns names, data types 
# df.head(n) = first n rows, eg. df.head(10) returns first 10 rows (also works for df.tail(n))
# df.mean() = returns the mean of all columns
# df.max() and df.min() = returns the highest and lowest numbers in all columns (note this is also alphabetical)

# can also filter, sort, group by, and clean data
