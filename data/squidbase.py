import yaml, os, sys, json


file_path = f"{os.getcwd()}/data/dev.json" if os.environ['FLASK_ENV'] == 'development' else f"{os.getcwd()}/data/runs.json"

def squidget():
    json_file = open(file_path)
    return json.load(json_file)

def squidwrite(data):
#    yaml_file = open(file_path, "w")
#    yaml.dump(data, yaml_file, default_flow_style=False)
    with open(file_path, 'w') as f:
        json.dump(data, f)

