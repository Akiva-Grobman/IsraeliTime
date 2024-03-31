from pymongo import MongoClient
from pymongo.server_api import ServerApi
from config import Config



def _get_mongo_client() -> MongoClient:
    return MongoClient(Config.mongo_url,
                        tls=True,
                        # tlsCertificateKeyFile='certs/X509-cert-4343229093406906630.pem',
                        tlsCertificateKeyFile=Config.certs_path,
                        server_api=ServerApi('1'))


_MONGO_CLIENT: MongoClient = _get_mongo_client()


def get_dbs():
    return _MONGO_CLIENT.list_database_names()
