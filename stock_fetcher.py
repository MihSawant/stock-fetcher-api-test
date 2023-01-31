import requests
import json
import os
import time
begin = time.time()
r = requests.get('https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json')
f = open("res_py.txt", "w")
for i in r.json():
    f.write(json.dumps(i))
f.close()
end = time.time()
print(f"Finished Task: {end - begin}s")
