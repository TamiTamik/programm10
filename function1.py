def create():
    owog,ner,dun = input('owog ner dun: ').split()   # mozhno cherez zapyatuyu
    f = open('dun.txt', 'a')
    f.write('\n' + owog + ' ' + ner + ' ' + dun)   #pisat' cherez '+'
    f.close()
    print('\n','dungiin medeeleld amjilttai nemlee')

def remove():
    owog, ner = input('owog, ner: ').split()
    f = open('dun.txt', 'r')
    data = f.readlines()
    f.close()
    for item in data:
        line = item.split()   #kazhduyu stroku zasplitili
        if line[0] == owog and line[1] == ner:
            data.remove(item)
    txt = ''.join(data)   #vistraivaet kazhdiy index v stolbik
    f = open('dun.txt','w')
    f.write(txt)
    f.close()
    print('\n','dungiin medeellees amjilttai haslaa')

def showMenu():
    print('\n\n\n','-'*30,'\ndungiin burtgeliin programm\n','-'*30)
    print('1. dungiin medeelel harah')
    print('2. dungiin medeelel burtgeh')
    print('3. dungiin medeelel ustgah')
    print('4. dungiin medeelel zasah')
    print('5. programmaas garah\n','-'*30)

def show():
    f = open('dun.txt', 'r')
    data = f.readlines()
    f.close()
    for item in data:
        line = item.split()   #kazhduyu stroku zasplitili
    txt = ''.join(data)
    print('dungiin medeelel:','\n')
    print(txt)

def change():
    owog, ner = input('owog, ner: ').split()
    f = open('dun.txt', 'r')
    data = f.readlines()
    f.close()
    for item in data:
        line = item.split()   #kazhduyu stroku zasplitili
        if line[0] == owog and line[1] == ner:
            f = open('dun.txt','r+')
            a = input("dun zasnuu: ")
            f.write(item.replace(line[2], a))
    f.close()
    print('\n','dungiin medeelel amjilttai zaslaa')
