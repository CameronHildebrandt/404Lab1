#!/usr/bin/env python3
import os
import json

# this script is invoked by another location - the line at the top (shebang) tells the location how to run this script

# Create an empty dictionary
env = {}

for env_key, env_value in os.environ.items():
  env[env_key] = env_value
  # print('{} -> {}'.format(env_key, env_value))

print("Content-Type: application/json")
print()

# Print dict in raw json
print(json.dumps(env))



# serve env back as json???

# Report the query params to html