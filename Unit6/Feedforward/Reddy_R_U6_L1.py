import sys; args = sys.argv[1:]
file = open(args[0], 'r')
import math

def transfer(t_funct, input):
   if t_funct == "T1":
       return input
   elif t_funct == "T2":
       if input>0:
            return input
       else:
            return 0
   elif t_funct == "T3":
       return 1/(1+pow((math.e), -1*input)) 
   elif t_funct == "T4":
       return -1 + (2/(1+pow((math.e), -1*input)))

def dot_product(input, weights, stage):
   outputs = []
   for j in range(0,stage):
       sum = 0
       useWeights = weights[int(j*(len(weights)/stage)):int((j+1)*(len(weights)/stage))]
       if len(useWeights) > 0:
           for i in range(0,len(useWeights)):
                sum+=float(useWeights[i])*input[i]
           outputs.append(sum)
   return outputs
        
def evaluate(file, input_vals, t_funct):
   lines = file.readlines()
   lineCount = len(lines)
   outputs = []
   for line in lines:
       line = line.split(" ")
       if "\n" in line[len(line)-1]:
           line[len(line)-1] = line[len(line)-1][:-1]
       lineCount-=1
       newInputAmount = len(line)//len(input_vals)
       if(lineCount != 0):
           new_inputs = dot_product(input_vals, line, newInputAmount)
           input_vals.clear()
           input_vals = new_inputs
           for val in range(0,len(new_inputs)):
               input_vals[val] = transfer(t_funct, new_inputs[val])
       else:
        for i in range(0,len(line)):
            input_vals[i] = input_vals[i]*float(line[i])
   return input_vals
     
def main():
   inputs, t_funct, transfer_found = [], 'T1', False
   for arg in args[1:]:
      if not transfer_found:
         t_funct, transfer_found = arg, True
      else:
         inputs.append(float(arg))
   li =(evaluate(file, inputs, t_funct)) #ff
   for x in li:
      print (x, end=' ') # final outputs
if __name__ == '__main__': main()
# Ram Reddy, Period 5, 2023