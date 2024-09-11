
import ast
import numpy as np

newr2 = 0.3625

with open('previousscores.txt', 'r') as f:
    r2list = ast.literal_eval(f.read())


firstest = newr2 < np.min(r2list)
print(firstest)

secondtest = newr2 < np.mean(r2list) - 2 * np.std(r2list)
print(secondtest)

iqr = np.percentile(r2list, 75) - np.percentile(r2list, 25)
thirdtest = newr2 < np.percentile(r2list, 25) - 1.5 * iqr
print(thirdtest)