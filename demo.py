from pkg_resources import iter_entry_points, working_set, Environment, add_activation_listener
from pprint import pprint
for i, entry_point in enumerate(iter_entry_points(group='img.plugin', name=None), 1):
    name = entry_point.name
    module = entry_point.module_name
    f = entry_point.load()
    print('---------- entry point %d ----------' % i)
    print('entry point name:   %s' % name)
    print('entry point module: %s' % module)
    print('entry point object: %r' % f)
    print('the object is a function, run it: %r' % f())

print('================')

plgs = working_set.find_plugins(Environment())
pprint(plgs)
