import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SECRET_KEY = os.getenv("SECRET_KEY", "DemoSecretKey123456")
    AI_API_KEY = os.getenv("AI_API_KEY", "demo_huggingface_api_key_12345")
    DATABASE_URL = os.getenv("DATABASE_URL", "https://demo-firebase-db.firebaseio.com")
    BLOCKCHAIN_RPC_URL = os.getenv("BLOCKCHAIN_RPC_URL", "https://demo-eth-rpc-url")
    CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "0xDEMO123ABC456DEF7890")
    AI_MAX_INSIGHTS = int(os.getenv("AI_MAX_INSIGHTS", 5))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
