# python.learning_instagram
# shifting characters

from collections import deque
text = 'python learning'
dquText = deque(list(text))
dquText.rotate(2)
print(dquText)

print(''.join(dquText))