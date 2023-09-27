
import os
from py_apollo_cli.client import ApolloClient


meta_server = {
	"LOCAL": "http://your_domain.com",
	"DEV": "http://your_domain.com",
	"FAT": "http://172.16.80.59:31760",
	"UAT": "http://172.16.0.157:30682",
	"PRO": "http://172.16.1.173:31639",
}

default_client: ApolloClient

def start(app_id: str, env: str = ''):
    if app_id == "":
        raise Exception("no app_id specified!")
    
    env = env.upper().strip()
    cluster = "default"    
    if env == "" or env == "LOCAL":
        config_url = meta_server["DEV"]    
    elif env == "FAT" or env == "DEV" or env == "DEVELOPMENT":
        config_url = meta_server["FAT"]
    elif env == "UAT" or env == "TEST":
        config_url = meta_server["UAT"]
    elif env == "PRO" or env == "PROD" or env == "PRODUCTION":
        config_url = meta_server["PRO"]                        
    else:
        raise Exception(f"invalid env: {env}")   

    print(f"apollo start, app_id:{app_id}, env:{env}, config_url:{config_url}") 
    global default_client  
    default_client = ApolloClient(app_id=app_id, cluster=cluster, config_url=config_url)

def get_config() -> ApolloClient:
    if not default_client:
        start(os.getenv("app_id"), os.getenv("env", ''))
    return default_client        



def init():
    start(os.getenv("APP_ID"), os.getenv("ENV", ''))


init()


