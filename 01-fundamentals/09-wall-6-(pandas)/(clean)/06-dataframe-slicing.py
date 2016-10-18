import pandas as pd

# Indexing, ordering and deleting
if False:
    ages = [28, 32, 25]
    hats = [True, False, False]
    people = ['Sarah', 'Mike', 'Chrisna']
    df = pd.DataFrame({'age'  : pd.Series(ages),
                       'hats' : pd.Series(hats),
                       'name' : pd.Series(people),
                      })

    # print list(data.index) #  Returns index numbers
    # df.index.get_values()

    # df.ix[:,['float_col','int_col']] #  Selecting a subset of columns with header
    # df['float_col']

    # df.rename(columns={'Squared Values' : 'topman'}, inplace = True) # Rename an index

    # ordered_df = pd.DataFrame(df, columns=('name', 'hats', 'age'))
    # print df

    # print df.set_index('hats')
    # print [df['people'] == 'Mike'].sort('mike', ascending=False).head()

    #df = df.drop("is_even", 1) # is a axsis

# Grouping
    # Group dataframe by location, sum entry totals and sort by most busy
    # df_group = df.groupby('station')
    # df_agg = df_group.aggregate({'ENTRIESn_hourly': np.sum}).sort('ENTRIESn_hourly', ascending=False)
    # df['UNIT'].unique()



# Slicing
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    # print football['year']
    # print football.year  # shorthand for football['year']
    # print football[['year', 'wins', 'losses']]

    # print football.iloc[[0]] # Primarily integer position based (from 0 to length-1 of the axis)
    # print football.loc[0] # primarily label column
    # print football.loc[[0]] # primarily label row
    # print football.loc[0][1] # Exact value
    # print football.loc[3, 'year']
    # print football[3:5] # Prints all columns but only rows 3-5

    # print football[football.wins > 10] # Prints only where wins are greater than 10
    # print football[(football.wins > 10) & (football.team == "Packers")]
    # print df.iloc[3:7,0:15] # Slice row then column display
    # print football[(football.year == 2011) & (football.wins == 10)]


# Deleting rows, columns and values
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    # print football.drop('year', 1)
    # print football.drop(['year', 'team', 'losses'], 1)



# Imputation
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)

    # print football = football.replace(4, np.nan) # Replaces the 4 in 'wins' with NaN
    # print football['wins'] = football['wins'].fillna(99) # Replaces 'NaN' with int 99
    # print football = football.fillna(99) # Replaces 'NaN' with int 99
    # print football



# Filtering
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    df = pd.DataFrame(data)

    # df[df["team"] == "Bears"]  # Interchangeable syntax the same result
    # df[df.team == "Bears"]  # Interchangeable syntax the same result

    print df[(df.team == "Bears") | (df.wins == 11)]  # This or that
    print df[(df.team == "Bears") & (df.wins == 11)]  # This and that
    # df[df['day_week'].isin([3, 6])]  # Filter by array of values
    # df_weekday = df({'A' : [5,6,3,4], 'B' : [1,2,3, 5]})  # Filter by an array, of arrays

