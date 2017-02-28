import os, time, re

def flowtable(switch):
    shell = "ovs-ofctl dump-flows " + switch
    print shell
    output = os.popen(shell).read()
    print output
    print output.count("actions")
    fl = open(switch+'1.txt','a')
    fl.write(str(output.count("actions")) + "\n")
    fl.close()

if __name__ == '__main__':
	while True:
		flowtable('s1')
		flowtable('s2')
		flowtable('s3')
		flowtable('s4')
		flowtable('s5')
		print "inters"
		time.sleep(2)
		

		
        

