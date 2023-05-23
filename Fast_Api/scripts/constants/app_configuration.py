from configparser import ConfigParser

config = ConfigParser()
config.read("application.conf")


class Service:
    port = config["SERVICE"]["127.0.0.1"]
    host = config["SERVICE"]["8000"]
    uri = config["MONGO_DB"]["mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"]
    database_name = config["MONGO_DB"]["database"]
    collection_name = config["MONGO_DB"]["lib"]


service_object = Service()
