def print_params_3(**params):
    print(params.__class__.__name__)
    print(params)

def printx(**kwargs):
    if kwargs['x']:
        print(kwargs['x'])


def initdb(*params,**kwargs):
    host=None
    user=None
    passwd=None
    db=None
    if len(params)>=1:
        host=params[0]
    if len(params)>=2:
        user=params[1]
    if len(params)>=3:
        passwd=params[2]
    if len(params)>=4:
        db=params[3]

    if host is None and kwargs['host']:
        host=kwargs['host']
    if user is None and kwargs['user']:
        user=kwargs['user']
    if passwd is None and kwargs["passwd"]:
        passwd=kwargs['passwd']
    if db is None and kwargs['db']:
       db=kwargs['db']

    if host is None or user is None or passwd is None or db is None:
        raise Exception('argument occured error!')
    return [host,user,passwd,db]


def retrive_multi():
    return 2,4

def print_params(*params):
    print(params)

def print_params_2(title,*params):
    print(title)
    print(params)
def in_the_middle(x,*y,z=7):
    print(x,y,z)
def in_the_middle(x,*y,**kwargs):
    print(x,y,kwargs)


def print_params_4(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)

print_params_4(1,2,3,5,6,7,foo=1,bar=2)




in_the_middle(1,2,3,4,5,6,7,z='last')
in_the_middle(1,2,3,4,6,7)
print_params("Test")
print_params("just","a","test")
print_params_2('Params:',1,2,3)
print_params_2('Nothing')
printx
printx(x=2)
vals=initdb('localhost','xuhui','flower','employees')
print(vals)
vals=initdb(host='localhost',user='xuhui',passwd='flower',db='employees')
print(vals)


