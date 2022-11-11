import random
import matplotlib.pyplot as plt

"""
Some experiments with Shannon's Demon
"""

#claculate the end value of a double-or-half coin flip game
def coinflip_game(start_balance, flips):
    history = [start_balance]
    for i in range(flips):
        if random.random() < 0.5:
            history.append(history[i] * 2)
        else:
            history.append(history[i] / 2)
    return history
    
#print(coinflip_game(1000, 10))


def sim_coinflip_game(start_balance, flips, trials):
    results = []
    for i in range(trials):
        results.append(coinflip_game(start_balance, flips))
    return results
    

# Create a modified version of the coinflip game that only applies the double-or-half rule to half of the balance
def coinflip_game2(start_balance, flips, reserve_ratio):
    deployed = [start_balance/2]
    reserved = [start_balance/2]
    nw = [start_balance]
    
    for i in range(flips):
        if random.random() < 0.5:
            winnings = deployed[i]
        else:
            winnings = -(deployed[i]/2)
        
        nw.append(deployed[i] + winnings + reserved[i])
        deployed.append(nw[i]*(1-reserve_ratio))
        reserved.append(nw[i]*reserve_ratio)

    return deployed
    
def sim_coinflip_game2(start_balance, flips, reserve_ratio, trials):
    results = []
    for i in range(trials):
        results.append(coinflip_game2(start_balance, flips, reserve_ratio))
    return results
    
experiment1 = (sim_coinflip_game(1000, 100, 1000))
experiment2 = (sim_coinflip_game2(1000, 100, .5, 1000))

for trial in experiment1:
    plt.plot(trial, color='red', alpha=0.1)

for trial in experiment2:
    plt.plot(trial, color='green', alpha=0.1)
    
plt.yscale('log')
plt.ylim(bottom=1)
plt.axhline(y=1000, color='black', linestyle='-')
plt.show()

exp1_ends = [trial[-1] for trial in experiment1]
exp2_ends = [trial[-1] for trial in experiment2]
    
    
#round to 2 decimal places and add commas
def fmt(num):
    return "{:,}".format(round(num, 2))
    
def CAGR(start, end, steps):
    return (end/start)**(1/steps) - 1

def describe_data(data, label):
    print("Describing " + label)
    print("Mean: ", fmt(sum(data)/len(data)))
    print("Median: ", fmt(sorted(data)[len(data)//2]))
    print("Max: ", fmt(max(data)))
    print("Min: ", fmt(min(data)))
    print("Std Dev: ", fmt((sum([(x - sum(data)/len(data))**2 for x in data]) / len(data))**0.5))
    print("Variance: ", fmt((sum([(x - sum(data)/len(data))**2 for x in data]) / len(data))))
    print("")


describe_data(exp1_ends, "Experiment 1: Non-rebalanced")
describe_data(exp2_ends, "Experiment 2: realanced")