# pulaski

A script for scraping fire data from [NOAA's Hazard Mapping System Fire and Smoke Product](https://www.ospo.noaa.gov/Products/land/hms.html#data) and returning it as geojson

# Install

```bash
$ python -m venv venv
$ pip -r requirements.txt
```

# Usage

Get most current file:

```bash
$ python3 pulaski 
```

Get file by date:

```bash
$ python3 pulaski <YYYYmmdd>
```

## To do

- add option to pretty print JSON

[![pulaski](./pulaski.jpg)](https://en.wikipedia.org/wiki/Pulaski_(tool))