import os
import pathlib
from dotenv import load_dotenv


ROOT_DIR = pathlib.Path(__file__).parent
ENV_PATH = os.path.join(ROOT_DIR, ".env")

load_dotenv(ENV_PATH)


DATABASE = {
    "NAME": os.getenv("MONGO_DB_NAME"),
    "URL": os.getenv("MONGO_CONNECTION_URL"),
}
