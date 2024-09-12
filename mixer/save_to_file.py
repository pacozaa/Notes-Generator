import json
import uuid
def saveToFile(name,dataset_name,data):
  dataWithId= [
      {"content": item, "id": str(uuid.uuid4())}
      for item in data
  ]
  json_array = json.dumps(dataWithId, indent=2)
  file_name = f"""./data-json/{name}-{len(dataWithId)}-{dataset_name.replace("/", "-")}-{str(uuid.uuid4())}.json"""
  with open(file_name, "w") as f:
      f.write(json_array)