# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 22:58:02 2018

@author: Rahul Kiran
"""

#!/usr/bin/python

def displayPathtoPrincess(n,grid):

    if(n>=3 and n<100):            
        for i in [0,n-1]:
            for j in [0,n-1]:
                if(grid[i][j]=='p'):
                    final_i=i
                    final_j=j

    #to find the location of the you:
        if(n%2!=0):
            m=int(n/2)
            if(grid[m][m]=='m'):
                initial_i=m
                initial_j=m

        if(n%2==0):
            m=int(n/2)
            for i in [m-1,m]:
                for j in range(m+1):
                    if(grid[i][j]=='m'):
                        initial_i=i
                        initial_j=j
   
        k=initial_i
        l=initial_j

        if(final_i==0 and final_j==0):
            output=""
            output=output.join("LEFT\n"*l)
            split=output.split("\n")
            for i in split:
                if(i!=""):
                    print(i)
            output=""
            output=output.join("UP\n"*k)
            split=output.split("\n")
            for i in split:
                if(i!=""):
                    print(i)
        if(final_i==n-1 and final_j==0):
            output=""
            output=output.join("LEFT\n"*l)
            split=output.split("\n")
            for i in split:
                if(i!=""):
                    print(i)
            output=""
            output=output.join("DOWN\n"*k)
            split=output.split("\n")
            for i in split:
                if(i!=""):
                    print(i)

        if(final_i==0 and final_j==n-1):
            output=""
            output=output.join("RIGHT\n"*l)
            split=output.split("\n")
            for i in split:
                if(i!=""):
                    print(i)
            output=""
            output=output.join("UP\n"*k)
            split=output.split("\n")
            for i in split:
                if(i!=""):
                    print(i)
   

        if(final_i==n-1 and final_j==n-1):
            output=""
            output=output.join("RIGHT\n"*l)
            split=output.split("\n")
            for i in split:
                if(i!=""):
                    print(i)
            output=""
            output=output.join("DOWN\n"*k)
            split=output.split("\n")
            for i in split:
                if(i!=""):
                    print(i)


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)