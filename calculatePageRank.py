#! /usr/bin/python3

from numpy import *

def iterator_CLI(cli,table_v):
	length = len(table_v)
	table_c = cli[0]
	table_l = cli[1]
	table_i = cli[2]
	result = [0 for i in range(0,length)]
	for i in range(0,len(table_l)-1):
		if(table_l[i+1] != table_l[i]):
			for j in range(table_l[i],table_l[i+1]):
				result[table_i[j]] += table_c[j] * table_v[i]
	return result


cli = [[1,1/2,1/2,1],[0,1,3,4],[1,0,2,0]]
table_v = [1/3,1/3,1/3]
print(iterator_CLI(cli,table_v))


def pageRank(d,e,cli,table_v):
	def converge(table_1,table_2):
		flag = False
		for i in range(0,len(table_1)):
			if((abs(table_1[i]-table_2[i])) < e ):
				flag = True
			else:
				flag = False
		return flag

	while True:
		new_table_v = iterator_CLI(cli,table_v)
		for i in range(0,len(new_table_v)):
			new_table_v[i] = new_table_v[i]*(1-d) + d/n
		if converge(new_table_v,table_v):
			break