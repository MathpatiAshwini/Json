import json

z={
    "Name": "Abhishek",
    "Designation":"CEO of navgurukul",
    "Gender":"male",
    "Age":"29"
}

x=json.dumps(z ,indent=5,sort_keys=True) 
print(x)
