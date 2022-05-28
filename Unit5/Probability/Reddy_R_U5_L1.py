from pomegranate import *
# Part A
Offer = DiscreteDistribution({'g':0.9, 'no-g':0.1}) # Creates independent nodes
# Creates dependent nodes
Tester = ConditionalProbabilityTable([
['g', 'positive', 0.5],
['g', 'negative', 0.5],
['no-g', 'positive', 0.05],
['no-g', 'negative', 0.95]], [Offer])
Tester2 = ConditionalProbabilityTable([
['g', 'positive', 0.75],
['g', 'negative', 0.25],
['no-g', 'positive', 0.25],
['no-g', 'negative', 0.75]], [Offer])
s_offer = State(Offer, 'graduate')
s_tester_1 = State(Tester, 'tester_1') # Creates nodes and states
s_tester_2 = State(Tester2, 'tester_2')
model = BayesianNetwork('graduate')
model.add_states(s_offer, s_tester_1, s_tester_2) # Creates the connections
model.add_transition(s_offer, s_tester_1)
model.add_transition(s_offer, s_tester_2)
model.bake() # finalize the topology of the model
print ('The number of nodes:', model.node_count())
print ('The number of elges:', model.edge_count())
# P(o2 | g, ~o1)
print("Part A")
print (model.predict_proba({'graduate':'g', "tester_1":"negative"})[2].parameters)
# P(g | o1, o2)
print (model.predict_proba({'tester_1':'positive', "tester_2":"positive"})[0].parameters)
# P(g | ~o1, o1)
print (model.predict_proba({'tester_1':'negative', "tester_2":"positive"})[0].parameters)
# P(g | ~o1, ~o2)
print (model.predict_proba({'tester_1':'negative', "tester_2":"negative"})[0].parameters)
# P(o2 | o1)
print (model.predict_proba({'tester_1':'positive'})[2].parameters)

# Part B
sunny = DiscreteDistribution({'s':0.7, 'no-s':0.3}) # Creates two independent nodes
rainy = DiscreteDistribution({'r':0.01, 'no-r':0.99})
happy = ConditionalProbabilityTable([
['s', 'r', 'h', 1],
['no-s', 'r', 'h', 0.9],
['s', 'no-r', 'h', 0.7],
['no-s', 'no-r', 'h', 0.1]], [sunny, rainy]) # Creates the dependent nodes
s_sunny = State(sunny, 'sunny')
s_rainy = State(rainy, 'rainy')
s_happy_1 = State(happy, 'happy')
model = BayesianNetwork('sunny')
model.add_states(s_sunny, s_rainy, s_happy_1) # Add nodes and connections
model.add_transition(s_sunny, s_happy_1)
model.add_transition(s_rainy, s_happy_1)
model.bake() # finalize the topology of the model
print ('The number of nodes:', model.node_count())
print ('The number of edges:', model.edge_count())
print("Part B")
# P(r | s)
print (model.predict_proba({'sunny':'s'})[1].parameters)
# P(r | h , s)
print (model.predict_proba({'happy':'h', "sunny":"s"})[1].parameters)
# P(r | h)
print (model.predict_proba({'happy':'h'})[1].parameters)
# P(r | h, ~ s)
print (model.predict_proba({'happy':'h', "sunny":"no-s"})[1].parameters)
