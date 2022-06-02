import sys; args = sys.argv[1:]
infile = open(args[0], 'r')
import math, random

# t_funct is symbol of transfer functions: 'T1', 'T2', 'T3', or 'T4'
# input is a list of input (summation) values of the current layer
# returns a list of output values of the current layer
def transfer(t_funct, input):
   if t_funct == 'T3': return [1 / (1 + math.e**-x) for x in input]
   elif t_funct == 'T4': return [-1+2/(1+math.e**-x) for x in input]
   elif t_funct == 'T2': return [x if x > 0 else 0 for x in input]
   else: return [x for x in input]

# returns a list of dot_product result. the len of the list == stage
# dot_product([x1, x2, x3], [w11, w21, w31, w12, w22, w32], 2) => [x1*w11 + x2*w21 + x3*w31, x1*w12, x2*w22, x3*w32] 
def dot_product(input, weights, stage):
   return [sum([input[x]*weights[x+s*len(input)] for x in range(len(input))]) for s in range(stage)]

# Complete the whole forward feeding for one input(training) set
# return updated x_vals and error of the one forward feeding
def ff(ts, xv, weights, t_funct):
   for i in range(len(weights)-1):
        xv[i+1] = dot_product(xv[i], weights[i], len(xv[i+1]))
        xv[i+1] = transfer(t_funct, xv[i+1])
   xv[len(xv)-1] = [xv[len(xv)-2][i]*weights[len(weights)-1][i] for i in range(len(xv[len(xv)-2]))]
   err = sum([(ts[-1-i] - xv[-1][i])**2 for i in range(len(xv[-1]))]) / 2
   return xv, err

# Complete the back propagation with one training set and corresponding x_vals and weights
# update E_vals (ev) and negative_grad, and then return those two lists
def bp(ts, xv, weights, ev, negative_grad, output):   
   ev[-1] = [ts[-1-i] - xv[-1][i] for i in range(output)]
   for i in range(len(ev)-2, 0, -1):
    for j in range(len(ev[i])):
        ev[i][j] = 0
        for k in range(0,len(weights[i])//len(ev[i])):
            ev[i][j] += ev[i+1][k]*weights[i][k*len(ev[i])+j]
        ev[i][j]*=xv[i][j]*(1-xv[i][j])
   for i in range(0,len(negative_grad)):
    for j in range(len(negative_grad[i])):
        negative_grad[i][j] = ev[i+1][j%len(ev[i+1])]*xv[i][j%len(ev[i])]
   return ev, negative_grad

# update all weights and return the new weights
# Challenge: one line solution is possible
def update_weights(ts,weights, negative_grad, alpha, t_funct):
#    xv = []
#    xv.append(ts)
   temp = []
   for i in range(len(weights)):
        newW = []
        for j in range(len(weights[i])):
#             newW.append(xv[i][j%len(xv[i])]*alpha*negative_grad[i][j]+weights[i][j])
            newW.append(alpha*negative_grad[i][j]+weights[i][j])
        temp.append(newW)
#         xv.append(dot_product(xv[i], newW, len(xv[i]) - 1))
#         xv[i+1] = transfer(t_funct, xv[i+1])
#    xv.append([xv[len(xv)-1][i]*temp[len(temp)-1][i] for i in range(len(xv[len(xv)-1]))])
#    err = sum([(ts[-1-i] - xv[-1][i])**2 for i in range(len(xv[-1]))]) / 2
#    print(xv)
#    print(temp)
   return temp

def main():
   t_funct = 'T3' # we default the transfer(activation) function as 1 / (1 + math.e**(-x))
   ''' work on training_set and layer_count '''
   training_set = []  # list of lists
   output_set = []
   outputAmount = 0
   for line in infile.readlines():
    if outputAmount ==0: outputAmount = len((line.split("=>"))[-1].strip().split(" "))
    temp2 = []
    for i in line.split(" "):
        if i!="=>":
            temp2.append(i.strip())
    training_set.append(temp2)
    output_set.append(outputAmount)
   training_set = [[float(j) for j in i] for i in training_set]
#    print (training_set) #[[1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [-1.0, -1.0, 1.0], [0.0, 0.0, 0.0]]
   layer_counts = [i for i in range(len(training_set[0])-outputAmount+1, outputAmount-1, -1)] # set the number of layers
#    layer_counts = [len(training_set[0])-outputAmount+1] + layer_counts
#    print(layer_counts, outputAmount)
   layer_counts.append(outputAmount)
#    print ('layer counts', layer_counts) # This is the first output. [3, 2, 1, 1] with teh given x_gate.txt

   # build NN: x nodes and weights 
   x_vals = [[temp[0:len(temp)-outputAmount]] for temp in training_set] # x_vals starts with first input values
#    print (x_vals) # [[[1.0, -1.0]], [[-1.0, 1.0]], [[1.0, 1.0]], [[-1.0, -1.0]], [[0.0, 0.0]]]
   # make the x value structure of the NN by putting bias and initial value 0s.
   for i in range(len(training_set)):
      for j in range(len(layer_counts)):
         if j == 0: x_vals[i][j].append(1.0)
         else: x_vals[i].append([0 for temp in range(layer_counts[j])])
#    print (x_vals) # [[[1.0, -1.0, 1.0], [0, 0], [0], [0]], [[-1.0, 1.0, 1.0], [0, 0], [0], [0]], ...
   # by using the layer counts, set initial weights [3, 2, 1, 1] => 3*2 + 2*1 + 1*1: Total 6, 2, and 1 weights are needed
   weights = [[random.uniform(-2.0, 2.0) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
#    weights = [[1.35, -1.34, -1.66, -0.55, -0.9, -0.58], [-1.08, -0.7], [-0.6]]   #Example 2
#    print ("w",weights)    #[[2.0274715389784507e-05, -3.9375970265443985, 2.4827119599531016, 0.00014994269071843774, -3.6634876683142332, -1.9655046461270405]
                        #[-3.7349985848630634, 3.5846029322774617]
                        #[2.98900741942973]]

   # build the structure of BP NN: E nodes and negative_gradients 
   E_vals = [[*i] for i in x_vals]  #copy elements from x_vals, E_vals has the same structures with x_vals
   negative_grad = [[*i] for i in weights]  #copy elements from weights, negative gradients has the same structures with weights
   errors = [10]*len(training_set)  # Whenever FF is done once, error will be updated. Start with 10 (a big num)
   count = 1  # count how many times you trained the network, this can be used for index calc or for decision making of 'restart'
   oalpha = 1
   countMax = 1
   alpha = 10
   err = 100
   max = 5000
   # calculate the initail error sum. After each forward feeding (# of training sets), calculate the error and store at error list
   
   while err > 1:
    weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
    for k in range(len(training_set)):
#       print(training_set[k], x_vals[k])
      x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
    err = sum(errors)
       
#    print(err)
   while err > 0.0099 and count < max:
    temp = [[0 for j in range(len(negative_grad[i]))] for i in range(len(negative_grad))]
    for k in range(len(training_set)):
      x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
      E_vals[k], negative_grad = bp(training_set[k], x_vals[k], weights, E_vals[k], negative_grad, output_set[k])
      weights = update_weights(E_vals[k], weights, negative_grad, alpha, t_funct)
    count+=1
    err = sum(errors)
#     print(count, err)
#     if err < 0.25:
#         alpha = 0.5
    if(count%250==0 and alpha>0.25):
        alpha = alpha*0.5
#     print(alpha)
    if (err > .0099 and count == max) or err > 1:
        weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
        count = 0
        alpha  = 1
#    print("w",err)
   ''' 
         check error sum and change alpha or reset weights if it's needed
      update E_vals and negative_grad by calling bp()
      update weights
      count++
   '''
   # print final weights of the working NN
   print ('layer counts', layer_counts)
   for w in weights: print (w)
if __name__ == '__main__': main()
# Ram Reddy, 5, 2023