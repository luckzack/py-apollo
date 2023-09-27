from py_apollo_cli import apollo

apollo.start(app_id="studio_stage", env="local")
client = apollo.get_config()

val = client.get_value("logger.config", default_val="{}")
print(val)