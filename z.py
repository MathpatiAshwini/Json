import json
x={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

z=json.dumps(x,sort_keys=True,indent=5)
print(z)
