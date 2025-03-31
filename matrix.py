import sys
import stdio

#accept n and k as command-line arguments
n = int(sys.argv[1])
k = int(sys.argv[2])

#generate matrix
for i in range(n): #iterate through numbers in range to get i, number of rows
    for j in range(n): #iterate through numbers in range to get j, number of columns
# i and j will be equal as we are looking for an n x n matrix, that is why the range for both is the same
        if j < i:
            stdio.write("0") #if j is less than i, we print 0 to create the diagonal effect
        else:
            stdio.write(str(k)) #if j is greater than or equal to i, we print the value of k
    stdio.writeln() #creates a new line