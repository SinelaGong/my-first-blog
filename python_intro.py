


def hi(name):
    if name == 'Sinela':
        print('Hi Sinela!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi("Sinela")

def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
    
