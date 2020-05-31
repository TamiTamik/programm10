#class MyClass: #klass nuzhno perevesti v object
    #x = 5

#p = MyClass() #sozadli object
#print(p.x) #print 'x' iz classa 'p'
#print(type(p))

class person:
    fname = 'bold'
    lname = 'tumur'

    def hi(self):
        print('hi I am', self.fname)

p1 = person()
p2 = person()
print(p1.fname)
p1.hi()
print(p2.fname)
p2.hi()