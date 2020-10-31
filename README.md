# Bayern Corona Grabber
This is a little project to help to create some statistics about corona cases in Bavaria
Data source is: [lgl.bayern.de](https://www.lgl.bayern.de/)

Also, please don't expect much code quality as this is my first real project here that I made mostly from scratch.
So it's kinda hacky.

## Usage

Just install docker and run it:

```
docker run -d --name corona_exporter -p <whatever_port_you_want>:80 razurac/bayern-corona-grabber-py
```
 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



