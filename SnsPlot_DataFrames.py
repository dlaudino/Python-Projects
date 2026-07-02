import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for index in range(0,len(df['Bruises'])):
    df['Bruises'][index] = str(df['Bruises'][index])
columns = df.columns.tolist()

for column in columns:
    print(column)

for column in columns:
    sns.countplot(x=column, data=df)

for column in columns:
    # print(column)
    sns.countplot(x = df[column], data=df)
    plt.show()
    plt.clf()

for column in columns:
    # print(column)
    sns.countplot(x = df[column], data=df)
    # rotates the value labels slightly so they don't overlap, also slightly increases font size
    plt.xticks(rotation=30, fontsize=10)
    # increases the variable label font size slightly to increase readability
    plt.xlabel(column, fontsize=12)
    plt.show()
    plt.clf()

for column in columns:
    # print(column)
    sns.countplot(x = df[column], data=df)
    # rotates the value labels slightly so they don't overlap, also slightly increases font size
    plt.xticks(rotation=30, fontsize=10)
    # increases the variable label font size slightly to increase readability
    plt.xlabel(column, fontsize=12)
    plt.title(column + " Value Counts")
    plt.show()
    plt.clf()

for column in columns:
    # print(column)
    sns.countplot(x = df[column], data=df, order=df[column].value_counts().index)
    # rotates the value labels slightly so they don't overlap, also slightly increases font size
    plt.xticks(rotation=30, fontsize=10)
    # increases the variable label font size slightly to increase readability
    plt.xlabel(column, fontsize=12)
    plt.title(column + " Value Counts")
    plt.show()
    plt.clf()
