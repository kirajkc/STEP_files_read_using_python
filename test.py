from steputils import p21

FNAME = 'exapmle.STEP'
# Read an existing file from file system:
try:
    stepfile = p21.readfile(FNAME)
    
except IOError as e:
    print(str(e))
else:
    print(f'File {FNAME} is a valid STEP-file')
    #Reading Header section
    print('-----Header---------')
    header_ = stepfile.header.entities
    for header_entity in header_:
        print(header_entity, stepfile.header.__getitem__(header_entity))
    
    #Reading Data Section
    print('----------Data-------------')
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
                
    '''
    # In case of multiple data section
    
    data_iter = stepfile.data
    for data_section in data_iter:
        data_iterable = data_section.__iter__()
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
    '''
