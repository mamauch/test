import optparse

def fib(n, prin):
    a,b = 0,1
    for i in range(n):
        a,b = b , a+b
        if prin:
            print(a)

    return a

def main():
    parser = optparse.OptionParser('usage %prog' +\
                                   '-n <fib number> -o <output file> -a (print all)', version= "prog 1.0")
    parser.add_option('-n',dest='num',type = 'int', \
                      help = 'specify the nth fibonacci number to output ')
    parser.add_option('-o' , dest = 'out', type ='string', \
                      help= 'specify an outputfile (optional)')
    
