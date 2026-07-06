# Hands-On Assignment 1: API Data Fetcher

## Objective

The objective of this assignment is to understand how APIs work by creating and consuming a REST API using Python.

Instead of using a third-party API like JSONPlaceholder, a custom API was developed using Flask that serves student data stored in a JSON file.

---

## Technologies Used

- Python 3.14
- Flask
- Requests Library
- JSON

---

## Project Structure

APIDataFetcherPython/
│
├── api_server.py
├── api_client.py
├── students.json
└── README.md

---

## API Used

A custom REST API was created using the Flask framework.

### Endpoint

http://127.0.0.1:5000/students

### HTTP Method

GET

### Response Format

JSON

---

## Workflow

1. Student data is stored in `students.json`.
2. The Flask server reads the JSON file.
3. The server exposes the data through the `/students` endpoint.
4. The Python client sends a GET request using the Requests library.
5. The API response is received in JSON format.
6. The data is displayed in the console.

---

## Sample JSON Response

```json
[
  {
    "id": 1,
    "name": "Mayank Makhija",
    "course": "BCA",
    "semester": 6,
    "city": "Pune"
  }
]
```

---

## How to Run

### Step 1

Start the Flask server:

```bash
py -3.14 api_server.py
```

### Step 2

Open another terminal and run:

```bash
py -3.14 api_client.py
```

---

## Output

The client successfully retrieves student data from the custom REST API and displays it in the console.

---

## Learning Outcome

- Understanding of REST APIs
- Creating an API using Flask
- Consuming APIs using the Requests library
- Working with JSON data
- Handling HTTP GET requests

# Hands-On Assignment 1: Weather API Data Fetcher

## Objective

The objective of this assignment is to understand how to consume a REST API using Python. The application fetches real-time weather information based on geographical coordinates (latitude and longitude) and displays the results in the console.

---

## Technologies Used

- Python 3.14
- Requests Library
- Open-Meteo Weather API
- JSON

---

## API Used

**API Name:** Open-Meteo Weather API

**Official Website:**
https://open-meteo.com/

### Endpoint

https://api.open-meteo.com/v1/forecast

### HTTP Method

GET

### Parameters Used

- latitude
- longitude
- current

Example Request:

https://api.open-meteo.com/v1/forecast?latitude=18.5204&longitude=73.8567&current=temperature_2m,relative_humidity_2m,wind_speed_10m

---

## Workflow

1. The user provides the latitude and longitude of a location.
2. A GET request is sent to the Open-Meteo Weather API.
3. The API returns weather information in JSON format.
4. The program extracts the required fields.
5. The weather details are displayed in the console.

---

## Weather Information Retrieved

- Temperature (°C)
- Relative Humidity (%)
- Wind Speed (km/h)

---

## Sample Output

```
===== CURRENT WEATHER =====

Temperature : 28.4 °C
Humidity    : 74 %
Wind Speed  : 6.3 km/h
```

---

## How to Run

Install the Requests library:

```bash
py -3.14 -m pip install requests
```

Run the program:

```bash
py -3.14 weather_api.py
```

---

## Learning Outcomes

- Understanding REST APIs
- Sending HTTP GET requests
- Working with URL query parameters
- Parsing JSON responses
- Extracting and displaying real-time weather data
- Using latitude and longitude for location-based services
