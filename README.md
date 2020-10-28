# Bayern Corona Grabber
This is a little project to help to create some statistics about corona cases in Bavaria
Data source is: [lgl.bayern.de](https://www.lgl.bayern.de/)

My end goal is, to turn this into an exporter for prometheus, but for now I only made the data collecting part.

Also, please don't expect much code quality as this is my first real project here that I made mostly from scratch.
So it's kinda hacky.

## Installation
Since I don't know yet know how to make stuff into a Module.
For now, just put the stats_grabber.py next to your projects code and import it:
```python
import stats_grabber
```

## Usage

There are two functions you can call: 
````python
stats_grabber.get_data()
````
This will return a list with the table header and the raw data the following format:
[headings, data]
Both headings and data are a list in itself.

The other function:
````python
stats_grabber.json_out()
````
will give you the data a bit more processed as JSON output
 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



