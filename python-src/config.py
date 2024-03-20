import os
from dataclasses import dataclass

@dataclass
class Config:
    mongo_url = os.environ['MONGO_URL']
    certs_path = os.environ['MONGO_CERT_PATH']
