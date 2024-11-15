import logging

import paho.mqtt.client as mqtt
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.responses import PlainTextResponse, JSONResponse


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    broker: str
    port: int = 1883
    username: str
    password: str


settings = Settings()

notification_topic = "aha/Siebenuhr-057070/siebenuhr-057070-notification/cmd_t"

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(settings.username, settings.password)

app = FastAPI(redoc_url=None)


@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Why did the clock get kicked out of the party? It kept tocking too much! 🕒"


@app.get("/notify/{message}")
async def send_message(message: str):
    try:
        mqtt_client.connect(settings.broker, settings.port)
        mqtt_client.publish(notification_topic, message)
        mqtt_client.disconnect()

        return {"status": "success", "message": "message sent successfully."}
    except Exception as e:
        logging.error(e)

        return JSONResponse(
            status_code=500, content={"status": "error", "message": str(e)}
        )
