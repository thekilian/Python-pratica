# working with pandas

# pip install pandas
import pandas
# load json file into dataframe
df = pandas.read_json('file.json')
type(pandas.read_json('file.json'))
# <class 'pandas.core.frame.DataFrame'>
# export csv file with to_csv()
df.to_csv('hello.csv')
# export pickle file with to_pickle()
df.to_pickle('hello.csv')