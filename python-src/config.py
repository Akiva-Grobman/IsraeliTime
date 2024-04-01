import os
from dataclasses import dataclass

@dataclass
class Config:
    mongo_url = os.environ.get('MONGO_URL', 'mongodb+srv://israelitime.of5zepk.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=IsraeliTime')
    certs_path = os.environ.get('MONGO_CERT_PATH', '/home/ubuntu/.keys/mongo.pem')
    student_token = 'T0RZeE1qQTNNVGd4TXpRd05UUTVPVGc1TFRJd01ERXpORFkwTURjeU9EQTNNelUyTXpNd05qSTFOREEyT1RjME16UXdMakEwT0RBek9EZ3dORFUyT1Rjek5UazFNREF3T0RnM09Ua3lORFExTkRZM01EQXlOekEzTlRJMk5qY3VjajVm'
