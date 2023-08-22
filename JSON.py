
import json
# JSON file
f = open ("test.json", "r")
fnew = open ("test_upd.json", "w")
  
# Reading from file here you should store the response payload.  example data variable 

#pass the new URL either from the file, I htink the best option is file and store in the variable (exampl I have used var) 
#then this program will create an updated json object in the end i.e. json_data_out
#json_data_out will be your new payload
#send that in the next post/put request



data = json.load(f)

print (data["content"]["urls"])

var = {}

var = {
        "url": "test.com",
        "description": "Block this site",
        "enabled": True 
      }

size=len(data["content"]["urls"])
print (" The size of the urls array", size)
data["content"]["urls"].append(var)

print (data["content"]["urls"])

f.close()

fnew.close()
# Serializing json
json_data_out = json.dumps(data, indent=4)
 
print("The new dictionary file ",json_data_out)

jsonFile = open("test_upd.json", "w")
jsonFile.write(json_data_out)
jsonFile.close()




