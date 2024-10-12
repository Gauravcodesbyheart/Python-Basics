with ("practice.txt" , "r") as f:
    data = f.read ( )
    new_data = data.replace("java", "python")
with ("practice.txt" , "w") as f:
    f.write (new_data)



