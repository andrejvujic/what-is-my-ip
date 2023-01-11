# what's-my-ip?

Flask web server which returns the client's IP address.

# How to run?

This API is built on top of Flask, a Python framework for building simple APIs. For the creation of this API Python3 was used.

To run it, first install Flask framework:

```
pip install Flask
```

Read more about the Flask framework <a href="https://pypi.org/project/Flask/">here</a>.

Then, run it using Python3:

```
python3 app.py
```

If you are on Windows use:

```
python app.py
```

Now, there should be an IP address printed in console. That's the IP address of the server.

The console should look like below, on the bottom you can see two IPs. The first one is available only on your machine while the second one makes the server available to all devices on your network.

```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it ina production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3333
 * Running on http://192.168.1.4:3333

```

# What does the API return?

Once the client makes a GET request to that endpoint they will their IP address returned in JSON format like this:

```
{
     "ip": "...",
     "length": ...
}
```

The length key represents the number of IPs that were returned. If the length is 1, the return type of the first key which contains the IP address will be a string. However, if the length is greater than 1 then it's return type will be an array of strings. If no IP addresses are available the returned length will be 0 and the IP address will be shown as 'unknown'.

Like this:

1. No IPs are available:

```
{
     "ip": "unknown",
     "length": 0
}
```

2. Only one IP address is available

```
{
     "ip": "xxx.xxx.xxx.xxx",
     "length": 1
}
```

3. Multiple IP addresses are available

```
{
     "ip": [
          "xxx.xxx.xxx.xxx",
          "xxx.xxx.xxx.xxx",
          "xxx.xxx.xxx.xxx",
          ...,
     ],
     "length": NUMBER_OF_AVAILABLE_IPs
}
```

# Contact

<a href="mailto:vujicandrej366@gmail.com">vujicandrej366@gmail.com</a>
