# Days 1-3 - Examination of datetime module

## Day 1 

### Exploring basics of datetime module

```python
from datetime import datetime, timedelta, time, data
```

```python
today = datetime.today()
today
```

#### Algebra with dates
```python
xmas = date(2020, 2, 16)
print('There are {} days until xmas'.format((xmas - today.date()).days))
```

```python
if xmas is not today.date():
	print('Not xmas yet mate. It is {} days away.'.format((xmas - today.date()).days))
else:
	print('Now it is xmas. Merry today!')
```

## Day 2

### Looking at timedelta in more detail

#### How many days until 100 days of code is complete..?!
```python
t = timedelta(days=98, hours=23)
t
```

#### t.hours doesn't work -> timedelta works in either days or seconds
```python
t.seconds/3600
```

#### Can add datetimes and timedeltas and format it as a string
```python
str(toady + t)
```
