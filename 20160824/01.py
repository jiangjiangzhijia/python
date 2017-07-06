f = 'hello %s ,this is %s';
v = ('lijiang','apple')
print f%v



f = 'pi is %.10f'
from math import pi
print f%pi

from string import Template
s = Template('${g}lorious!')
print s.substitute(g='slurm')


print '%s is congming'%('lijiang')
