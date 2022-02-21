import yaml
import configparser
import json
import time
  



def  yaml_file_read(path):
    try:
        with open(path) as f:
            my_dict = yaml.safe_load(f)
            save_to_json(my_dict)
    except Exception as ex:
        return str(ex)
    return my_dict

def config_file_read(path, header_names):
    try:
        config = configparser.RawConfigParser()
        config.read(path)
        for x in header_names:
            details_dict = dict(config.items(x))
        save_to_json(details_dict)
    except Exception as ex:
        return str(ex)
    return details_dict


def save_to_json(data):
    ts = time.time()

    with open(f'{ts}.json', 'w') as fp:
        json.dump(data, fp)
    return


# print(yaml_file_read('sample.yaml'))
# print(config_file_read('config.conf', ['SECTION_NAME']))