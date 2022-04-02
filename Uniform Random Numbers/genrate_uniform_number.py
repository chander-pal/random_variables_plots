
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from uniform import*
import numpy as np
U = uniform_number(1,0,11425,685,(2**31),187854,1007855)
# uniform_number(uplimit,lowlimit,mult_factor,add_factor,mod,seed,size)
sns.set_style('darkgrid')
sns.distplot(U)
# sns.ecdfplot(U)
print(np.var(U))
print(np.mean(U))