student = {
    "name" : "Gaurav",
    "score" : {                # here nested dictioanry is created
        "chem" : 98,
        "phy"  : 97,
        "math" : 95,
    }
}
print(student["name"])
print(student ["score"]["math"])  # for printing hte value that is under the nested dictionary under score key
