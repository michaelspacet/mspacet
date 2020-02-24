# Days 7-9 -> Data Structures

## Day 7

### Basics of lists, tuples and dictionaries - Watched the refresher videos but happy to skip making notes on this

## Day 8

### Solutions to PyBite 21 - https://codechalleng.es/bites/21/

```python
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
       
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    
    return [cars[_][0] for _ in cars]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    
    return sorted([j for i in cars.values() for j in i if grep.lower() in j.lower()])
    

def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
       
    return {key:sorted(value) for key, value in cars.items()}
```
