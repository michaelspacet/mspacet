# Days 1-3 -> Examination of datetime module

## Day 1 

### Exploring basics of datetime module

```python
from datetime import datetime, timedelta, date
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
str(today + t)
```

## Day 3

### Creating a countdown timer

```python
from datetime import timedelta
import time

def countdown_time(number_of_seconds):

	""" Function to countdown until a specific user-defined time """

	important_time = timedelta(0, number_of_seconds).seconds

	while important_time > 0:
		print('Not quite time yet. There are still {} seconds to go!'.format(important_time))
		time.sleep(1)
		important_time -= 1

	if important_time == 0:
		print('Finally, it is time for that important event!')

countdown_time(10)
```
