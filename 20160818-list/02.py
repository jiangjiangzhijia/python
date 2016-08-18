#1
#tag = '<a href="http://www.python.org">Python web site</a>'
#print tag[9:30]
#print tag[:3]
#print tag[:]
#2

#numbers = [1,2,3,4,5,6,7,8,9,10]
#print numbers[0:10:-2]
#3
#print [1,2,3]+[4,5,6]
print [1,2,3]+['hello']
if(1==2):print 'a'
else : print 'b' 

#sequence = [None]*10
#print sequence
#a = input('what is your name:')
#print a

sententce = raw_input("Sententce: ")
scren_width = 40
text_width = len(sententce)
box_width    = text_width+8
left_margin = (scren_width+box_width) // 2

print 
print ' ' * left_margin + '+' + '-'*box_width + '+'
print ' ' * (left_margin+4) + '|' + ' ' * text_width + '|'
print ' ' * (left_margin+4) + '|' + sententce + '|'
print ' ' * (left_margin+4) + '|' + ' '*text_width + '|'
print ' ' * left_margin + '+' + '-'*box_width + '+'


