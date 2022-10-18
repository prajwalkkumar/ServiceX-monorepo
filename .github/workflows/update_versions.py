import sys
import ruamel.yaml

def update_version_in_servicex_chart_yaml(version):
    servicex_chart_yaml_file = "servicex/Chart.yaml"
    with open(servicex_chart_yaml_file, 'r') as stream:
        try:
            servicex_chart_data = ruamel.yaml.load(stream, Loader=ruamel.yaml.RoundTripLoader)
        except ruamel.yaml.YAMLError as exc:
            print("ERR: loading Yaml file")
            raise Exception(exc)

    servicex_chart_data['appVersion'] = version
    servicex_chart_data['version'] = version

    with open(servicex_chart_yaml_file, 'w') as yaml_file:
        yaml_file.write(ruamel.yaml.dump(servicex_chart_data, Dumper=ruamel.yaml.RoundTripDumper))

def update_version_in_servicex_values_yaml(version):
    servicex_values_yaml_file = "servicex/values.yaml"
    with open(servicex_values_yaml_file, 'r') as stream:
        try:
            servicex_values_data = ruamel.yaml.load(stream, Loader=ruamel.yaml.RoundTripLoader)
        except ruamel.yaml.YAMLError as exc:
            print("ERR: loading Yaml file")
            raise Exception(exc)

    servicex_values_data['app']['tag'] = version
    servicex_values_data['didFinder']['rucio']['tag'] = version
    servicex_values_data['didFinder']['CERNOpenData']['tag'] = version
    servicex_values_data['transformer']['defaultTransformerTag'] = version
    servicex_values_data['x509Secrets']['tag'] = version
    servicex_values_data['codeGen']['tag'] = version

    with open(servicex_values_yaml_file, 'w') as yaml_file:
        yaml_file.write(ruamel.yaml.dump(servicex_values_data,  Dumper=ruamel.yaml.RoundTripDumper))



def update_version_in_flux_river_uproot_values_yaml(version):
    flux_river_uproot_values_file = "../flux_river_configs/servicex-int-uproot/values.yaml"
    with open(flux_river_uproot_values_file, 'r') as stream:
        try:
            flux_river_uproot_data = ruamel.yaml.load(stream, Loader=ruamel.yaml.RoundTripLoader)
        except ruamel.yaml.YAMLError as exc:
            print(exc)

    flux_river_uproot_data['spec']['chart']['spec']['version'] = version
    with open(flux_river_uproot_values_file, 'w') as yaml_file:
        yaml_file.write(ruamel.yaml.dump(flux_river_uproot_data, Dumper=ruamel.yaml.RoundTripDumper))


def update_version_in_flux_river_xaod_values_yaml(version):
    flux_river_xaod_values_file = "../flux_river_configs/servicex-int-xaod/values.yaml"

    with open(flux_river_xaod_values_file, 'r') as stream:
        try:
            flux_river_xaod_data = ruamel.yaml.load(stream, Loader=ruamel.yaml.RoundTripLoader)
        except ruamel.yaml.YAMLError as exc:
            print(exc)

    flux_river_xaod_data['spec']['chart']['spec']['version'] = version

    with open(flux_river_xaod_values_file, 'w') as yaml_file:
        yaml_file.write(ruamel.yaml.dump(flux_river_xaod_data, Dumper=ruamel.yaml.RoundTripDumper))


if __name__ == '__main__':

    if len(sys.argv) == 1:
        raise Exception("ERR: Please enter version to update.")

    version = sys.argv[1]
    update_version_in_servicex_chart_yaml(version)
    update_version_in_servicex_values_yaml(version)
    update_version_in_flux_river_uproot_values_yaml(version)
    update_version_in_flux_river_xaod_values_yaml(version)



