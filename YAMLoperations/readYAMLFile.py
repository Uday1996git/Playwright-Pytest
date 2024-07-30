import yaml


with open("../PlayWrightDemo/Configs/appConfig.yaml", "r") as file:
    service = yaml.safe_load(file)

print(service['URL'])
