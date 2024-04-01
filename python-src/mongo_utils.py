from pymongo import MongoClient
from pymongo.server_api import ServerApi
from config import Config
from bson.json_util import dumps
from json import loads



def _get_mongo_client() -> MongoClient:
    return MongoClient(Config.mongo_url,
                        tls=True,
                        # tlsCertificateKeyFile='certs/X509-cert-4343229093406906630.pem',
                        tlsCertificateKeyFile=Config.certs_path,
                        server_api=ServerApi('1'))


_MONGO_CLIENT: MongoClient = _get_mongo_client()


def add_student_to_db(student):
    student_collection = _MONGO_CLIENT['israel_time']['students']
    student_collection.insert_one(student)


def get_students_from_db():
    student_collection = _MONGO_CLIENT['israel_time']['students']
    return loads(dumps(student_collection.find({})))



def get_dbs():
    return _MONGO_CLIENT.list_database_names()
