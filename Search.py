import json
read_file=open("cw_data.json",encoding="utf8")
data=json.load(read_file)
#%%
flattened=dict()
for region in data:
    for date in data[region]:
        for codes in data[region][date]:
            flattened[codes]=dict()
            flattened[codes]["time"]=data[region][date][codes]["time"]
            flattened[codes]["src"]=data[region][date][codes]["src"]
            flattened[codes]["region"]=data[region][date][codes]["region"]
            flattened[codes]["time"]=data[region][date][codes]["time"]
            flattened[codes]["domain"]=data[region][date][codes]["domain"]
            flattened[codes]["digest"]=data[region][date][codes]["digests"]["English"]["digest"]
            flattened[codes]["headline"]=data[region][date][codes]["digests"]["English"]["headline"]
