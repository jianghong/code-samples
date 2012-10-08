class JimsException(Exception):
    pass

def this_fails():
    #raise NameError, "Sorry, never met them."
    x = 1 / 0
    print "This statement is never reached."

def this_too():
    raise JimsException('hi there')

if __name__ == "__main__":
    try:
        this_fails()
    except ZeroDivisionError, e:
        print "oops",
        print e
        print dir(e)
    
    #this_too()
    
    try:
        f = open('notthere')
        s = f.readline()
        print 3 / 0
        i = int(s.strip())
    except Exception:
        print "You're a completely general idiot."
    except IOError:
        print "Input/Output error"
    except ValueError:
        print "Could not convert data to an integer"
    except:
        print "You're an idiot."
    
    print i
