name = {
    "first name" : "Gaurav",
    "second_name" : "Singh",
    "class" : "Section",
    "section" : "B",
    "subjects" : {
        "maths" : 99,
        "English" : 88,
        "skills" : ("java" , "python" , "c" , "c++"), #it is list
        "soft skills" : ["English" , "Hindi" , "Math"],
    }
}
print(name ["subjects"] ["soft skills"])
print(name.keys())    #returns all the keys
print(name.values())  #returns all the values
print(name.items())   #returns all the pairs of keys and values
print(name.get("second_name"))     #returns the value as per the key 
print(name.update( ))