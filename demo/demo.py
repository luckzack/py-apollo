#!/usr/bin/env python

#import os
import sys
sys.path.append("../py_apollo_cli")

#os.environ["app_id"] = "studio_stage"

import apollo
apollo.start("studio_stage", "local")
client = apollo.get_config()

val = client.get_value("logger.config", default_val="{}")
print(val)