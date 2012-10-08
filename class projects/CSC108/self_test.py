'''self_test.py: basic tests for A1 twitterverse.py'''
import sys,os,re,__builtin__
from StringIO import StringIO
passed_all=True

# QUERIES
q1 =\
'''SEARCH
tomcruise
FILTER
PRESENT
sort-by username
format short
'''

q2=\
'''SEARCH
tomcruise
followed-by
FILTER
PRESENT
sort-by username
format short
'''

q3=\
'''SEARCH
tomcruise
followed-by
FILTER
location-includes oz
PRESENT
sort-by username
format short
'''

q4=\
'''SEARCH
tomcruise
followed-by
follows
FILTER
follows katieh
PRESENT
sort-by username
format long
'''
# DATA
d1=\
'''tomcruise
Tom Cruise
Los Angeles, CA
http://www.tomcruise.com
Official TomCruise.com crew tweets. We love you guys! 
Visit us at Facebook!
ENDBIO
katieh
nicolekidman
END
katieh
Katie Holmes

www.tomkat.com

ENDBIO
END
nicolekidman
Nicole Kidman
Oz

At my house celebrating Halloween! I Know Haven't been on like 
years So Sorry,Be safe And have fun tonight
ENDBIO
END
'''

d2=\
'''tomcruise
Tom Cruise
Los Angeles, CA
http://www.tomcruise.com
Official TomCruise.com crew tweets. We love you guys! 
Visit us at Facebook!
ENDBIO
katieh
nicolekidman
END
katieh
Katie Holmes

www.tomkat.com

ENDBIO
END
nicolekidman
Nicole Kidman
Oz

At my house celebrating Halloween! I Know Haven't been on like 
years So Sorry,Be safe And have fun tonight
ENDBIO
END
'''
d3=\
'''tomcruise
Tom Cruise
Los Angeles, CA
http://www.tomcruise.com
Official TomCruise.com crew tweets. We love you guys! 
Visit us at Facebook!
ENDBIO
katieh
nicolekidman
END
perezhilton
Perez Hilton
Hollywood, California
http://www.PerezH...
Perez Hilton is the creator and writer of one of the most famous websites
in the world. And he also loves music - a lot!
ENDBIO
tomcruise
katieh
nicolekidman
END
katieh
Katie Holmes

www.tomkat.com
ENDBIO
END
nicolekidman
Nicole Kidman
Oz

At my house celebrating Halloween! I Know Haven't been on like 
years So Sorry,Be safe And have fun tonight
ENDBIO
END
tomfan
Chris Calderone
Houston, Texas

Tom Cruise is the best actor in Hollywood!
ENDBIO
tomcruise
END
p
Mme Clavell
Paris, France

I love winter, snow and ice.
ENDBIO
nicolekidman
END
q
Quincy Q
Port Coquitlam, BC
http://www.something.com
ENDBIO
nicolekidman
END
a
Alex D
Abbottsford, British Columbia
www.abbotsford.ca
Love the outdoors, even 
in the rain.
ENDBIO
tomfan
END
b
Benny Lewis
Bankok

ENDBIO
tomfan
END
x
Xavier
Xerox Parc
www.xerox.com
ENDBIO
c
END
y
Yousef
Yarmouth, Nova Scotia
yarmouthonline.ca
Welcome to Yarmouth, Nova Scotia - rich in history and culture, home to year-round festivals and live entertainment, and the perfect place for your next special getaway. We look forward to meeting you!
ENDBIO
c
END
z
Zoya Zorich


ENDBIO
b
END
c
captain_crunch
The Captain
Kansas
kellogs.com
ENDBIO
END
'''
# EXPECTED OUTPUTS
out1=\
'''Data file:  self_test_data.txt
Query file:  self_test_query.txt
['tomcruise']
'''

out2=\
'''Data file:  self_test_data.txt
Query file:  self_test_query.txt
['katieh', 'nicolekidman']
'''

out3=\
'''Data file:  self_test_data.txt
Query file:  self_test_query.txt
['nicolekidman']
'''

out4=\
'''Data file:  self_test_data.txt
Query file:  self_test_query.txt
----------
perezhilton
name: Perez Hilton
location: Hollywood, California
website: http://www.PerezH...
bio:
Perez Hilton is the creator and writer of one of the most famous websites
in the world. And he also loves music - a lot!
follows: ['tomcruise', 'katieh', 'nicolekidman']
----------
tomcruise
name: Tom Cruise
location: Los Angeles, CA
website: http://www.tomcruise.com
bio:
Official TomCruise.com crew tweets. We love you guys!
Visit us at Facebook!
follows: ['katieh', 'nicolekidman']
----------
'''

def normalize(s):
    '''Change a string into a normalized form for more lenient comparison
    of expected vs observed output.'''
    
    return re.sub(r'\s+','',s)


def test_scenario(q,d,o,description):
    
    print description, ": ",
    f = open("self_test_query.txt","w")
    f.write(q)
    f.close()
    f = open("self_test_data.txt","w")
    f.write(d)
    f.close()
    old_raw_input = raw_input
    input_list = ["self_test_data.txt","self_test_query.txt"]
    def new_raw_input(prompt=""):
        print prompt,
        assert len(input_list)>0,\
            "Raw input was asked for unexpectedly. The interaction was as follows:\n"+\
            sys.stdout.getvalue()+" <<<RAW INPUT CALLED>>>"
        ret = input_list.pop(0)
        print ret
        return ret
    __builtin__.raw_input = new_raw_input
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        execfile("twitterverse.py",globals(),globals())
    finally:
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
    if normalize(output)==normalize(o):
        print "passed."
    else:
        print "failed."
    print "INTERACTION LOG"
    print output

    #check that output is as expected:
    assert normalize(output)==normalize(o),\
        "The output produced during the interaction (above) was not as expected.\n"\
        "The expected output is as follows:\n%s"%o

def fail(aerror):
    
    print "FAILURE: "+aerror.message
    print
    global passed_all
    passed_all=False
    
    
if __name__=="__main__":
    assert os.path.exists("twitterverse.py"),\
    "The file twitterverse.py was not found.\n"\
    "It should be in the directory where this script is run."
    for q,d,o,description in (q1,d1,out1,"Testing that q1 on d1 yields out1"),\
                (q2,d1,out2,"Testing that q2 on d1 yields out2"),\
                (q3,d2,out3,"Testing that q3 on d2 yields out3"),\
                (q4,d3,out4,"Testing that q4 on d3 yields out4"):
        try:
            test_scenario(q,d,o,description)
        except AssertionError, error:
            fail(error)
    #test that the twitterverse module can be imported without errors
    #(previously we ran twitterverse.py as a script)
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    def new_raw_input(prompt=""):
        assert False, "Importing the module should not prompt for input, but raw_input was called!"
    raw_input = new_raw_input
    try:
        import twitterverse 
    except AssertionError, error:
        fail(error)
    capture_stdout = sys.stdout.getvalue()
    sys.stdout = old_stdout
    try:
        assert not capture_stdout, \
            "Output was printed to the console when importing twitterverse as a module.\n"\
            "The output was:\n%s\n"\
            %capture_stdout
    except AssertionError, error:
        fail(error)
    if passed_all:
        print "PASSED SELF TEST"
    else:
        print "FAILED SELF TEST"
