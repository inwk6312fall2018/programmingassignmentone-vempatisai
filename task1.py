def task1():
	fin=open("running-config.cfg") 
	list1= []                
	for line in fin:
		line=line.strip()       
		line=line.split()            
		if(line[0] ==  "interface"): 
			list1.append(line[1])  
	print(list1)
task1()
