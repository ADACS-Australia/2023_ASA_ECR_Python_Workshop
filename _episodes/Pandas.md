---
title: "The Pandas module"
teaching: 90
exercises: 0
questions:
- "What is Pandas?"
objectives:
- "TBD"
- "TBD"
keypoints:
- "TBD"
- "TBD"
---

For a longer and more complete version of what will be covered in this session, please refer to lessons 3-6 of [this software carpentry course](https://datacarpentry.org/python-ecology-lesson).

## What is Pandas?
The Python data analysis library ([Pandas](https://pandas.pydata.org/)), is designed to be a fast, powerful, flexible, and easy to use data analysis tool built for Python.
Pandas is [NumFOCUS](https://numfocus.org/) sponsored project (as are Numpy, Scipy, Matplotlib, and Astropy), and will therefore tend to "play nice" with these other packages.
The Pandas library provides data structures, produces high quality plots with
[Matplotlib](https://matplotlib.org) and integrates nicely with other libraries
that use [NumPy](https://numpy.org/) arrays.
There are additionally many packages that are built on top of Pandas to address specialized needs (see [ecosystem](https://pandas.pydata.org/community/ecosystem.html)).

Pandas is a great solution for many of your data analysis and visualization needs however it is designed for tabular data.
Alternatives to Pandas include:

| module | notes |
| -- | -- |
| [Numpy](https://numpy.org/) | ndarrays can have up to 32 dimensions, but need to be of a single data type | 
| [Vaex](https://vaex.readthedocs.io/en/latest/) | DataFrames like Pandas, with lazy evaluation of **billions** of rows per second. Desiged for big data. Uses memory mapping.|
| [Dask](https://www.dask.org/) | Focus on scalability and portability across architectures (laptop/desktop/cloud/HPC). Lazy evaluation, and workflow management.  |
| [Xarray](https://docs.xarray.dev/en/stable/) | For working with labelled multi-dimensional arrays. Like FITS but actually good! | 


Pandas provides a few different data structures that are useful for this lesson with the main one being the **DataFrame**.
A DataFrame is a 2-dimensional data structure that can store data in columns.
Each column can have a different data type, but, just like tables in a database, the data within a single column must have a consistent type.
A DataFrame always has an index (0-based) for rows.


## Our data
We will be using files from the [Portal Project Teaching Database](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459).
Normally this lesson would have you download the `surveys.csv` file from [here](https://ndownloader.figshare.com/files/2292172), however we just learned about databses, so we'll instead download the file `portal_mammals.sqlite` from [this link](https://figshare.com/ndownloader/files/11188550).


### Exploring our data

> ## Explore our database
> Open our `portal_mammals.sqlite` files with sqlite3 or upload it to [sqliteonline](https://sqliteonline.com/).
>
> View the schema of the data base by looking at the columns and data types for each of the three tables.
>
> There are no explicit foreign key constraints on this database, however, should be able to identify which columns in the `surveys` table link to each of the `plots` and `species` tables.
{: .challenge}

We now connect to the data base and read it into a Pandas DataFrame:
~~~
# import our modules
import sqlite3
import pandas as pd

# connect to the database
con = sqlite3.connect('portal_mammals.sqlite')

# execute a query and save the results to a dataframe
surveys_df = pd.read_sql("SELECT * FROM surveys", con)
~~~
{: .language-python}

Pandas is aware of the environment it's being run in, so will give slightly different out put when you are running via `python3`, `ipython3`, or a `jupyter` notebook.
Jupyter will give the nicest output and it will be more interactive than the iPython note book, while the output you get from a python script will be just text.
Use whatever you prefer.

If you execute the above code you should see the following output:
~~~
      record_id month day year  plot_id species_id  sex hindfoot_length weight
0             1     7  16 1977        2         NL    M            32.0    NaN
1             2     7  16 1977        3         NL    M            33.0    NaN
2             3     7  16 1977        2         DM    F            37.0    NaN
3             4     7  16 1977        7         DM    M            36.0    NaN
4             5     7  16 1977        3         DM    M            35.0    NaN
...         ...   ... ...  ...      ...        ...  ...             ...    ...
35544     35545    12  31 2002       15         AH  NaN             NaN    NaN
35545     35546    12  31 2002       15         AH  NaN             NaN    NaN
35546     35547    12  31 2002       10         RM    F            15.0   14.0
35547     35548    12  31 2002        7         DO    M            36.0   51.0
35548     35549    12  31 2002        5        NaN  NaN             NaN    NaN

[35549 rows x 9 columns]
~~~
{: .output}

We can see that there were 35,549 rows parsed.
Each row has 9 columns.
The first column is the index of the DataFrame.
The index is used to identify the position of the data, but it is not an actual column of the DataFrame (it was not the database which we read).
The ellipsis (...) tell you that Pandas is intentionally not showing all the output, but just the head/tail of the table.
If we have many columns (or a narrower screen) then Pandas will skip columns as well.

You can also use `surveys_df.head()` to view only the first few rows of the dataset in an output that is easier to fit in one window.
After doing this, you can see that pandas has neatly formatted the data to fit our screen:

~~~
surveys_df.head() # The head() method displays the first several lines of a file. It
                  # is discussed below.
~~~

~~~
   record_id  month  day  year  plot_id species_id sex  hindfoot_length  \
5          6      7   16  1977        1         PF   M             14.0
6          7      7   16  1977        2         PE   F              NaN
7          8      7   16  1977        1         DM   M             37.0
8          9      7   16  1977        1         DM   F             34.0
9         10      7   16  1977        6         PF   F             20.0

   weight
5     NaN
6     NaN
7     NaN
8     NaN
9     NaN
~~~
{: .output
}
### Exploring Our Species Survey Data
What kind of things does `surveys_df` contain?
DataFrames have an attribute called `dtypes` that answers this:

~~~
surveys_df.dtypes
~~~
{: .language-python}

~~~
record_id            int64
month                int64
day                  int64
year                 int64
plot_id              int64
species_id          object
sex                 object
hindfoot_length    float64
weight             float64
dtype: object
~~~
{: .output}

All the values in a single column have the same type.
For example, values in the month column have type `int64`.
Cells in the month column cannot have fractional values, but values in weight and hindfoot\_length columns can, because they have type `float64`.
The `object` type doesn't have a very helpful name, but in this case it represents strings (such as 'M' and 'F' in the case of sex).

#### Useful Ways to View DataFrame Objects in Python

There are many ways to summarize and access the data stored in DataFrames,
using **attributes** and **methods** provided by the DataFrame object.

Attributes are features of an object. For example, the `shape` attribute will output
the size (the number of rows and columns) of an object. To access an attribute,
use the DataFrame object name followed by the attribute name `df_object.attribute`.
For example, using the DataFrame `surveys_df` and attribute `columns`, an index
of all the column names in the DataFrame can be accessed with `surveys_df.columns`.

Methods are like functions, but they only work on particular kinds of objects. As
an example, **the `head()` method** works on DataFrames. Methods are called in a
similar fashion to attributes, using the syntax `df_object.method()`. Using
`surveys_df.head()` gets the first few rows in the DataFrame `surveys_df`
using the `head()` method. With a method, we can supply extra information
in the parentheses to control behaviour.

Let's look at the data using these.

> ## Challenge - DataFrames
> 
> Using our DataFrame `surveys_df`, try out the **attributes** & **methods** below to see what they return.
> 
> 1. `surveys_df.columns`
> 
> 2. `surveys_df.shape` Take note of the output of `shape` - what format does it
>   return the shape of the DataFrame in?
>   
>  HINT: [More on tuples, here][python-datastructures].
> 
> 3. `surveys_df.head()` Also, what does `surveys_df.head(15)` do?
> 
> 4. `surveys_df.tail()`
>
> > ## Solution
> > 1. `surveys_df.columns` provides the names of the columns in the DataFrame.
> > 2. `surveys_df.shape` provides the dimensions of the DataFrame as a tuple 
> >    in `(r,c)` format,
> >    where `r` is the number of rows and `c` the number of columns.
> > 3. `surveys_df.head()` returns the first 5 lines of the DataFrame, 
> >    annotated with column and row labels.
> >    Adding an integer as an argument to the function 
> >    specifies the number of lines to display from the top of the DataFrame, 
> >    e.g. `surveys_df.head(15)` will return the first 15 lines.
> > 4. `surveys_df.tail()` will display the last 5 lines, 
> >    and behaves similarly to the `head()` method.
> {: .solution}
{: .challenge}

### Calculating Statistics From Data In A Pandas DataFrame

We've read our data into Python.
Next, let's perform some quick summary statistics to learn more about the data that we're working with.
We might want to know how many animals were collected in each site, or how many of each species were caught.
We can perform summary stats quickly using groups.
But first we need to figure out what we want to group by.

Let's begin by exploring our data:
~~~
# Look at the column names
surveys_df.columns
~~~
{: .language-python}

which **returns**:
~~~
Index(['record_id', 'month', 'day', 'year', 'plot_id', 'species_id', 'sex',
       'hindfoot_length', 'weight'],
      dtype='object')
~~~
{: .output}

Let's get a list of all the species.
The `pd.unique` function tells us all of the unique values in the `species_id` column.

~~~
pd.unique(surveys_df['species_id'])
# OR
surveys_df['species_id'].unique()
~~~

which **returns**:

~~~
array(['NL', 'DM', 'PF', 'PE', 'DS', 'PP', 'SH', 'OT', 'DO', 'OX', 'SS',
       'OL', 'RM', nan, 'SA', 'PM', 'AH', 'DX', 'AB', 'CB', 'CM', 'CQ',
       'RF', 'PC', 'PG', 'PH', 'PU', 'CV', 'UR', 'UP', 'ZL', 'UL', 'CS',
       'SC', 'BA', 'SF', 'RO', 'AS', 'SO', 'PI', 'ST', 'CU', 'SU', 'RX',
       'PB', 'PL', 'PX', 'CT', 'US'], dtype=object)
~~~
{: .output}

> ## Challenge - Statistics
> 1. Create a list of unique site IDs ("plot\_id") found in the surveys data. Call it
>   `site_names`. How many unique sites are there in the data? How many unique
>   species are in the data?
> 
> 2. What is the difference between `len(site_names)` and `surveys_df['plot_id'].nunique()`?
>
> > ## Solution
> > 1. `site_names = pd.unique(surveys_df["plot_id"])`
> >   - How many unique sites are in the data? 
> >     `site_names.size` or `len(site_names)` provide the answer: 24
> >   - How many unique species are in the data?
> >     `len(pd.unique(surveys_df["species_id"]))` tells us there are 49 species
> > 2. `len(site_names)` and `surveys_df['plot_id'].nunique()` 
> >    both provide the same output: 
> >    they are alternative ways of getting the unique values.
> >    The `nunique` method combines the count and unique value extraction,
> >    and can help avoid the creation of intermediate variables like `site_names`.
> {: .solution}
{: .challenge}

## Groups in Pandas

We often want to calculate summary statistics grouped by subsets or attributes within fields of our data.
For example, we might want to calculate the average weight of all individuals per site.

We can calculate basic statistics for all records in a single column using the syntax below:

~~~
surveys_df['weight'].describe()
~~~
{: .language-python}

gives **output**
~~~
count    32283.000000
mean        42.672428
std         36.631259
min          4.000000
25%         20.000000
50%         37.000000
75%         48.000000
max        280.000000
Name: weight, dtype: float64
~~~
{: .output}

We can also extract one specific metric if we wish:

~~~
surveys_df['weight'].min()
surveys_df['weight'].max()
surveys_df['weight'].mean()
surveys_df['weight'].std()
surveys_df['weight'].count()
~~~
{: .language-python}

But if we want to summarize by one or more variables, for example sex, we can use **Pandas' `.groupby` method**.
Once we've created a groupby DataFrame, we can quickly calculate summary statistics by a group of our choice.

~~~
# Group data by sex
grouped_data = surveys_df.groupby('sex')
~~~
{: .language-python}

The **pandas function `describe`** will return descriptive stats including: mean, median, max, min, std and count for a particular column in the data.
Pandas' `describe` function will only return summary values for columns containing numeric data.

~~~
# Summary statistics for all numeric columns by sex
grouped_data.describe()
# Provide the mean for each numeric column by sex
grouped_data.mean(numeric_only=True)
~~~
{: .language-python}

`grouped_data.mean(numeric_only=True)` **OUTPUT:**

~~~
        record_id     month        day         year    plot_id  \
sex
F    18036.412046  6.583047  16.007138  1990.644997  11.440854
M    17754.835601  6.392668  16.184286  1990.480401  11.098282

     hindfoot_length     weight
sex
F          28.836780  42.170555
M          29.709578  42.995379

~~~
{: .output}

The `groupby` command is powerful in that it allows us to quickly generate
summary stats.

> ## Challenge - Summary Data
> 
> 1. How many recorded individuals are female `F` and how many male `M`?
> 2. What happens when you group by two columns using the following syntax and
>   then calculate mean values?
> 
> - `grouped_data2 = surveys_df.groupby(['plot_id', 'sex'])`
> - `grouped_data2.mean(numeric_only=True)`
> 
> 3. Summarize weight values for each site in your data. HINT: you can use the
>   following syntax to only create summary statistics for one column in your data.
>   `by_site['weight'].describe()`
> 
> > ## Solution
> > 1. The first column of output from `grouped_data.describe()` (count) 
> >    tells us that the data contains 15690 records for female individuals
> >    and 17348 records for male individuals.
> >    - Note that these two numbers do not sum to 35549, 
> >      the total number of rows we know to be in the `surveys_df` DataFrame.
> >      Why do you think some records were excluded from the grouping?
> > 2. Calling the `mean()` method on data grouped by these two columns 
> >    calculates and returns
> >    the mean value for each combination of plot and sex. 
> >    - Note that the mean is not meaningful for some variables,
> >      e.g. day, month, and year. 
> >      You can specify particular columns and particular summary statistics
> >      using the `agg()` method (short for _aggregate_),
> >      e.g. to obtain 
> >      the last survey year, 
> >      median foot-length 
> >      and mean weight for each plot/sex combination:
> > 
> > ```python
> > surveys_df.groupby(['plot_id', 'sex']).agg({"year": 'max',
> >                                            "hindfoot_length": 'median',
> >                                            "weight": 'mean'})
> > ```
> > 
> > 3. `surveys_df.groupby(['plot_id'])['weight'].describe()`
> > 
> > ```output
> >           count       mean        std  min   25%   50%   75%    max
> > plot_id                                                            
> > 1        1903.0  51.822911  38.176670  4.0  30.0  44.0  53.0  231.0
> > 2        2074.0  52.251688  46.503602  5.0  24.0  41.0  50.0  278.0
> > 3        1710.0  32.654386  35.641630  4.0  14.0  23.0  36.0  250.0
> > 4        1866.0  47.928189  32.886598  4.0  30.0  43.0  50.0  200.0
> > 5        1092.0  40.947802  34.086616  5.0  21.0  37.0  48.0  248.0
> > 6        1463.0  36.738893  30.648310  5.0  18.0  30.0  45.0  243.0
> > 7         638.0  20.663009  21.315325  4.0  11.0  17.0  23.0  235.0
> > 8        1781.0  47.758001  33.192194  5.0  26.0  44.0  51.0  178.0
> > 9        1811.0  51.432358  33.724726  6.0  36.0  45.0  50.0  275.0
> > 10        279.0  18.541219  20.290806  4.0  10.0  12.0  21.0  237.0
> > 11       1793.0  43.451757  28.975514  5.0  26.0  42.0  48.0  212.0
> > 12       2219.0  49.496169  41.630035  6.0  26.0  42.0  50.0  280.0
> > 13       1371.0  40.445660  34.042767  5.0  20.5  33.0  45.0  241.0
> > 14       1728.0  46.277199  27.570389  5.0  36.0  44.0  49.0  222.0
> > 15        869.0  27.042578  35.178142  4.0  11.0  18.0  26.0  259.0
> > 16        480.0  24.585417  17.682334  4.0  12.0  20.0  34.0  158.0
> > 17       1893.0  47.889593  35.802399  4.0  27.0  42.0  50.0  216.0
> > 18       1351.0  40.005922  38.480856  5.0  17.5  30.0  44.0  256.0
> > 19       1084.0  21.105166  13.269840  4.0  11.0  19.0  27.0  139.0
> > 20       1222.0  48.665303  50.111539  5.0  17.0  31.0  47.0  223.0
> > 21       1029.0  24.627794  21.199819  4.0  10.0  22.0  31.0  190.0
> > 22       1298.0  54.146379  38.743967  5.0  29.0  42.0  54.0  212.0
> > 23        369.0  19.634146  18.382678  4.0  10.0  14.0  23.0  199.0
> > 24        960.0  43.679167  45.936588  4.0  19.0  27.5  45.0  251.0
> > ```
> > 
> {: .solution}
>
{: .challenge}

### Quickly Creating Summary Counts in Pandas

Let's next count the number of samples for each species.
We can do this in a few ways, but we'll use `groupby` combined with **a `count()` method**.

~~~
# Count the number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)
~~~
{: .language-python}

Or, we can also count just the rows that have the species "DO":

~~~
surveys_df.groupby('species_id')['record_id'].count()['DO']
~~~
{: .language-python}

> ## Challenge - Make a list
> 
> What's another way to create a list of species and associated `count` of the
> records in the data? Hint: you can perform `count`, `min`, etc. functions on
> groupby DataFrames in the same way you can perform them on regular DataFrames.
> 
> > ## Solution
> > 
> > As well as calling `count()` on the `record_id` column of the grouped DataFrame as above, an equivalent result can be obtained by extracting `record_id` from the result of `count()` called directly on the grouped DataFrame:
> > 
> > ~~~
> > surveys_df.groupby('species_id').count()['record_id']
> > ~~~
> > {: .language-python}
> > 
> > ~~~
> > species_id
> > AB      303
> > AH      437
> > AS        2
> > BA       46
> > CB       50
> > CM       13
> > CQ       16
> > CS        1
> > CT        1
> > CU        1
> > CV        1
> > DM    10596
> > DO     3027
> > DS     2504
> > DX       40
> > NL     1252
> > OL     1006
> > OT     2249
> > OX       12
> > PB     2891
> > PC       39
> > PE     1299
> > PF     1597
> > PG        8
> > PH       32
> > PI        9
> > PL       36
> > PM      899
> > PP     3123
> > PU        5
> > PX        6
> > RF       75
> > RM     2609
> > RO        8
> > RX        2
> > SA       75
> > SC        1
> > SF       43
> > SH      147
> > SO       43
> > SS      248
> > ST        1
> > SU        5
> > UL        4
> > UP        8
> > UR       10
> > US        4
> > ZL        2
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

## Quick & Easy Plotting Data Using Pandas

We can plot our summary stats using Pandas, too.

~~~
# Make sure figures appear inline in Jupyter Notebook
%matplotlib inline
# Create a quick bar chart
species_counts.plot(kind='bar');
~~~
{: .language-python}

![Counts per species]({{page.root}}{%link fig/PandasSpeciesCounts.png%})
Count per species site

We can also look at how many animals were captured in each site:

~~~
total_count = surveys_df.groupby('plot_id')['record_id'].nunique()
# Let's plot that too
total_count.plot(kind='bar');
~~~
{: .language-python}

> ## Challenge - Plots
> 
> 1. Create a plot of average weight across all species per site.
> 2. Create a plot of total males versus total females for the entire dataset.
>   
> > ## Solution
> > 
> > 1. `surveys_df.groupby('plot_id')["weight"].mean().plot(kind='bar')`
> > 
> > ![Grouped weight]({{page.root}}{%link fig/PandasGroupedWeight.png%})
> > 
> > 2. `surveys_df.groupby('sex').count()["record_id"].plot(kind='bar')`
> > 
> > ![Grouped Sex]({{page.root}}{%link fig/PandasGroupedSex.png%})
> {: .solution}
{: .challenge}


### Multiple grouping
Pandas doesn't limit us to one set of groups.
For example we could group our data by plot_id and by sex:
~~~
by_site_sex = surveys_df.groupby(['plot_id', 'sex'])
site_sex_count = by_site_sex['weight'].sum()
~~~
{: .language-python}

This calculates the sums of weights for each sex within each site as a table:
~~~
site  sex
plot_id  sex
1        F      38253
         M      59979
2        F      50144
         M      57250
3        F      27251
         M      28253
4        F      39796
         M      49377
<other sites removed for brevity>
~~~
{: .output}

This isn't the easiest to visualize, since what we really want is table with plot_id as rows, and sex as columns.
We can achieve this pivot operation by using the `.unstack()` function:

~~~
by_site_sex = surveys_df.groupby(['plot_id', 'sex'])
site_sex_count = by_site_sex['weight'].sum()
site_sex_count.unstack()
~~~
{: .language-python}

The `unstack` method above will display the following output:

```output
sex          F      M
plot_id
1        38253  59979
2        50144  57250
3        27251  28253
4        39796  49377
<other sites removed for brevity>
```

Rather than display it as a table, we can plot the above data by stacking the values of each sex as follows:

~~~
by_site_sex = surveys_df.groupby(['plot_id', 'sex'])
site_sex_count = by_site_sex['weight'].sum()
spc = site_sex_count.unstack()
s_plot = spc.plot(kind='bar', stacked=True, title="Total weight by site and sex")
s_plot.set_ylabel("Weight")
s_plot.set_xlabel("Plot")
~~~
{: .language-python}

![Unstacked plot]({{page.root}}{%link fig/WeightSexUnstacked.png%})


## Combining DataFrames
DataFrames:
- masking / slicing
- joining frames