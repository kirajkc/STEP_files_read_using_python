from steputils import p21

FNAME = r'C:\Users\Karan\Downloads\STEP\step_files\TRIQBRIQ_300_Balken_1.STEP'
# Read an existing file from file system:
try:
    stepfile = p21.readfile(FNAME)
    
except IOError as e:
    print(str(e))
else:
    print(f'File {FNAME} is a valid STEP-file')
    data_iterable = stepfile.__iter__()
    for instances in data_iterable:
        
        # .ref ---->>>> instance reference eg: #10
        # .entity ---->>>> entity info like name, position, color,etc
                #.name ---->>>> name of entity
                #.params ----->>> properties of entity
        # .entities --->>> list of mulitple entity (in case of comple entity instance)
        
        if type(instances) == p21.SimpleEntityInstance:
            #simple instances entity
            print(instances.ref,instances.entity.name,instances.entity.params)
        else:
            #complex entity instances
            print(instances.ref,instances.entities)
            for complex_entity in instances.entities:
                print(complex_entity.name,complex_entity.params)
