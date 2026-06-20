
### Datetime objects
###### From string to datetime
- `import datetime from datetime`
	-	imports datetime object from the datetime module.
- `date_dt = datetime.strptime(given_date, '%m/%d/%Y')`
	- converts the string `given_date` into a datetime object named `date_dt`
	- the second argument is a time format string



###### From datetime to string
- `given_date = date_dt.strftime('%m/%d/%Y')`
	- converts a datetime object into a string with the given time string format



You may see more details on time string formats in this [documentation](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
###### Outputing into ISO
- `date_dt.isoformat()`
	- Use the `isoformat()` method on a datetime object to output it as ISO standard.


---
### Datetime Components
- Datetime components such as `day`, `month`, `year`, `hour`, `minute` and `second` are available as datetime instances.
- `date_dt.[component]` 
	- allows you to output a datetime component from a datetime object


###### Dealing with current time
- `datetime.now()`
	- The `.now()` method returns the current time.
	- `current_time = datetime.now()` assigns the current date and time to the variable `current_time`
- `datetime.utcnow()`
	- This method returns the current time along with the machine timezone.


---
### Timezones
- What is the difference between naive and aware datetime objects?
	- Naive datetime objects does not have a timezone (thus cannot be directly converted to another timezone) while aware datetime objects does have a timezone.


###### Importing timezone data in Python
- `from pytz import timezone`
	- Timezone data resides in `pytz` module. This line imports `timezone`.


###### Creating timezones
- `ny_tz = timezone('US/Eastern')`
	- You can create timezones by passing an argument to `timezone()`.


###### From Naive to Aware Datetime
```
record_dt = datetime.strptime(date, %m/%d/%Y)
ny_tz = timezone('US/Eastern')
ny_dt = record_dt.timezone(tzinfo = ny_tz)
```


The above line creates a naive datetime object `record_dt` and converts it into an aware datetime object `ny_dt`.

###### Changing timezones
```
ny_tz = timezone('US/Eastern')
la_tz = timezone('US/Pacific')
ny_dt = record_dt.timezone(tzinfo = ny_tz)
la_dt = ny_dt.astimezone(la_tz)
```
The above code converts timezone from US/Eastern to US/Pacific. This is possible by using the `.astimezone()` method and passing the desired timezone in it.


You may see all timezone names in this [Wikipedia article](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

---
### Timedelta objects
- `timedelta` objects are used to represent periods of time.
- You can add or subtract `timedelta` objects to `datetime` objects.


Creating timedelta objects
- `from datetime import timedelta`
	- Imports timedelta into python.
- `flashback = timedelta(days = 30)`
	- You can make timedelta objects using `timedelta()` function and passing a datetime instance into it.
	- This objects may be added or subtracted to a datetime object.

###### Adding and Subtracting Time
- `before = date_dt + flashback`
	- You may add/subtract a timedelta object from a datetime object.
- `time_diff = date_dt - date2_dt`
	- You can only subtract two datetime objects - doing so would mean finding the amount of time between these dates. To add dates, you need to make one of them into timedelta first.


---
### Pendulum library
- `.parse()` converts a string into a pendulum datetime object WITHOUT the need of a format string


###### Timezone hopping with pendulum
- `.in_timezone()` method converts a pendulum time object to a desired timezone
- `.now()` In pendulum, this method accepts a timezone you want to get a current time


###### Time periods in Pendulum
- `.in_XXX()` this method provide a time period. XXX can be any datetime instance (eg. in_days, in_hours, etc)
- `.in_words()` expresses a datetime into words





