import yaml, os, sys


file_path = f"{os.getcwd()}/data/dev.yaml" if os.environ['FLASK_ENV'] == 'development' else f"{os.getcwd()}/data/runs.yaml"

def squidget():
    yaml_file = open(file_path)
    return (yaml.load(yaml_file, Loader=yaml.FullLoader))

def squidwrite(data):
    yaml_file = open(file_path, "w")
    yaml.dump(data, yaml_file, default_flow_style=False)

