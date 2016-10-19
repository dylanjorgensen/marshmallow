import pandas as pd


# Create simple dataframe
if True:
    data = [1,2,3,4,5,6,7,8,9]
    df = pd.DataFrame(data, columns=["hello"])  # "hello" becomes the header row

    # df['new'] = df["x"] * 2
    # df["x_factorial"] = df["hello"].apply(np.math.factorial)
    # df["is_even"] = df["hello"] % 2
    # df["odd_even"] = df["is_even"].map({1:"odd", 0:"even"})
    print df


# Create from external file
if True:
    df = pandas.read_csv('titanic_data.csv')


# Create a dataframe from Series from list
if False:
    ages = [28, 32, 25]
    hats = [True, False, False]
    people = ['Sarah', 'Mike', 'Chrisna']
    df = pd.DataFrame({'age'  : pd.Series(ages),
                       'hats' : pd.Series(hats),
                       'name' : pd.Series(people),
                      })
    print df


# Data frame from a dictionary with arrays
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    # print football


