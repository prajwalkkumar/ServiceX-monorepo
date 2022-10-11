import yaml
import sys

if len(sys.argv)==1:
    print("Error. Please enter version to update.")
    exit(1)

CHART_YAML_PATH = "servicex/Chart.yaml"
VALUES_YAML_PATH = "servicex/values.yaml"

version = sys.argv[1]

chart_data = dict()
values_data = dict()

with open(CHART_YAML_PATH, 'r') as stream:
    try:
        chart_data = yaml.load(stream,Loader=yaml.SafeLoader)
    except yaml.YAMLError as exc:
        print(exc)

chart_data['appVersion'] = version
chart_data['version'] = version

with open(VALUES_YAML_PATH, 'r') as stream:
    try:
        values_data = yaml.load(stream,Loader=yaml.SafeLoader)
    except yaml.YAMLError as exc:
        print(exc)

values_data['app']['tag'] = version
values_data['didFinder']['rucio']['tag'] = version
values_data['didFinder']['CERNOpenData']['tag'] = version
values_data['transformer']['defaultTransformerTag'] = version
values_data['x509Secrets']['tag'] = version
values_data['codeGen']['tag'] = version


with open(CHART_YAML_PATH, 'w') as yaml_file:
    yaml_file.write(yaml.dump(chart_data, default_flow_style=False))

with open(VALUES_YAML_PATH, 'w') as yaml_file:
    yaml_file.write(yaml.dump(values_data, default_flow_style=False))