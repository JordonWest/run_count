import yaml, os, sys

file_path = f"{os.getcwd()}/data/runs.yaml"

def squidget():
    yaml_file = open(file_path)
    return (yaml.load(yaml_file, Loader=yaml.FullLoader))['runs']

def squidwrite(data):
    with open(file_path, 'w') as run_file:
        output = yaml.dump(data, file_path)

