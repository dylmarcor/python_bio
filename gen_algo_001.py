# This is a Genetic Algorithm from scratch from the website
# machinelearningmastery.com

# initial population of random bitstring
pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
