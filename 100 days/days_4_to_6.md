# Days 4-6 -> Exploring collections module

## Day 4

### Exploring namedtuuples

```python
from collections import defaultdict, namedtuple, Counter, deque
import random
```

#### namedtuples allow you to essentially create classes without methods

```python
User = namedtuple('User', 'name role')
user = User(name='Michael', role='Data Scientist')
user.name
```

```python
f'{user.name} is a {user.role}'
```

### Defaultdicts

#### Normal diotionaries will often throw a KeyError. Example:

```python
users = {'Michael': 'Data Scientist', 
		 'Robert': 'Tosser'}
users['Mike']  # Will give a KeyError
```

```python
users.get('Mike')  # Will not give a KeyError and will return None but is hard to deal with when building a collection
```

```python
challenges_done = [('Michael', 45), ('Robert', 7),
                   ('Michael', 12), ('Robert', 88)]
```

```python
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
challenges
```

### Counter

#### Already quite familar with this but good revision

```python
Jose = """ Tottenham boss Jose Mourinho hopes that the absence of key players means RB Leipzig will underestimate his side in their Champions League last-16 tie. Spurs will be without their first-choice forward line with Son Heung-min joining Harry Kane on the sidelines. The South Korea international has had surgery on a broken arm and could miss the rest of the season. They are probably thinking, Wow, now is the time to kill them, said Mourinho. """
Jose = Jose.split()
```

```python
Counter(Jose).most_common(5)
```

### Deque 

#### Deque is more efficient when dealing with large lists

```python
lst = list(range(10000000))
deq = deque(range(10000000))
```

```python
def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

%timeit insert_and_delete(lst)

%timeit insert_and_delete(deq)  # This is 2 orders of magnitude faster. Can notice this in the terminal
```
