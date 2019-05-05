'''
10 basic Python examples that will help you learn fast

https://www.makeuseof.com/tag/basic-python-examples-learn-fast/
'''

# String formatting
name = 'Repys'
job = 'Coder'

# concatenate (not Pythonic)
'''
title = name + ' the ' + job
print(title)
'''

# format() method
'''
The {} is a placeholder that gets replaced by the parameters of the format() method in sequential order. The first {} gets replaced by the name parameter and the second {} gets replaced by the job parameter. You can have as many {}s and parameters as you want as long as the count matches.

What’s nice is that the parameters don’t have to be strings. They can be anything that can be represented as strings, so you could include an integer if you wish:
'''

age = 99
title = "{} the {} of {} years".format(name, job, age)
print(title)

# String joining