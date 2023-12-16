from re import I


def store(data,*full_names):
    for full_name in full_names:
        names=full_name.split()
        if len(names) == 2:
            names.insert(1,'')
        labels='first','middle','last'
        for label,name in zip(labels,names):
            people=lookup(data,label,name)
            if people:
                people.append(full_name)
            else:
                data[label][name]=[full_name]



def init(d):
    d['first']={}
    d['middle']={}
    d['last']={}
def lookup(data,label,name):
    if data[label][name] is None:
        data[label][name]=[]
        
    return data[label][name]
    
l=dict()
init(l)


store(l,'Luke Skywalker','Anakin Skywalker')
lookup(l,'last','Skywalker')
print(l)
