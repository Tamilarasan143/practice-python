name = "tamil" #global

#dose not change the value because of scope 
def update_name():
    name = "tamilarasan" # local
    print(name)
def update_global_name():
    global name
    name = "tmilarasan elumalai"
    print(name)
print(name)
update_name()
update_global_name()

#output
#tamil
#tamilarasan
#tamilarasan elumalai