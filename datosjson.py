import json

json_file = open('/home/devasc/labs/devnet-src/parsing/myfile.json')
ourjson = json.load(json_file)

print("Token:", ourjson["access_token"])
print("Tiempo restante antes de caducar (segundos):", ourjson["expires_in"])

json_file.close()
