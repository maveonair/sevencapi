# Siebenuhr Notification API

This FastAPI application is designed to send notifications to the Siebenuhr system via an MQTT message broker.

## Features

- Send notifications by passing a message to the `/notify/{message}` endpoint.
- Integrates with an MQTT broker using configurable environment variables.

## Environment Variables

The following environment variables must be configured to enable communication with the MQTT broker:

- **`BROKER`**: The hostname or IP address of the MQTT broker.
- **`PORT`**: The port number for the MQTT broker (default is `1883`).
- **`USERNAME`**: The username for MQTT authentication.
- **`PASSWORD`**: The password for MQTT authentication.

## API Endpoints

### **`GET /notify/{message}`**

#### Description:

Sends the specified message to the MQTT broker for notification purposes.

#### Parameters:

- **`message`**: (Path parameter, string, required)  
  The notification message to send.

#### Responses:

- **`200 OK`**: The message was sent successfully.
- **`500 Internal Server Error`**: This error is a generic "catch-all" response to server issues.

#### Example Request:

```bash
curl -X GET "http://127.0.0.1:8000/notify/hello" -H "accept: application/json"
```

#### Example Response (200):

```json
{
  "status": "success",
  "message": "Notification sent successfully."
}
```

#### Example Response (500):

```json
{
  "status": "error",
  "message": "timed out."
}
```

## Setup and Usage

### Running with Docker:

A prebuilt Docker image is available on Docker Hub. You can quickly deploy the API using the following steps:

1. Pull the Docker image:
   ```bash
   docker pull maveonair/sevencapi
   ```

2. Run the container with required environment variables:
   ```bash
   docker run -d --name sevencapi \
     -e BROKER="your_broker_host" \
     -e PORT=1883 \
     -e USERNAME="your_username" \
     -e PASSWORD="your_password" \
     -p 8000:8000 \
     maveonair/sevencapi
   ```

3. Access the API at `http://127.0.0.1:8000`.

### Running Locally:

1. Clone the repository:
   ```bash
   git clone git@github.com:maveonair/sevencapi.git
   cd sevencapi
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   Create a `.env` file or export the variables directly:
   ```bash
   export BROKER="your_broker_host"
   export PORT=1883
   export USERNAME="your_username"
   export PASSWORD="your_password"
   ```

4. Start the application:
   ```bash
   uvicorn main:app --reload
   ```

### Accessing the API Documentation:

Interactive API documentation is available at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## License

This project is licensed under the [MIT License](LICENSE).
