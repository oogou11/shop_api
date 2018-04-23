
def load_to_dict(d, text=None, filename=None):
    '''
    Load the code from text into the dict d.
    ''' 
    if text:
        pass
    elif filename:
        text = open(filename).read() 
    else:
        text = ''
    code_obj = compile(text, "<config string>", 'exec')
    exec(code_obj, d) 

load_to_dict(globals(),'','config.py')

import mongoengine
for alias, attrs in MONGO.items():  
    mongoengine.register_connection(alias, **attrs)