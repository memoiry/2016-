"""
=============================================
Comparison of kernel ridge regression and SVR
=============================================

Both kernel ridge regression (KRR) and SVR learn a non-linear function by
employing the kernel trick, i.e., they learn a linear function in the space
induced by the respective kernel which corresponds to a non-linear function in
the original space. They differ in the loss functions (ridge versus
epsilon-insensitive loss). In contrast to SVR, fitting a KRR can be done in
closed-form and is typically faster for medium-sized datasets. On the other
hand, the learned model is non-sparse and thus slower than SVR at
prediction-time.

This example illustrates both methods on an artificial dataset, which
consists of a sinusoidal target function and strong noise added to every fifth
datapoint. The first figure compares the learned model of KRR and SVR when both
complexity/regularization and bandwidth of the RBF kernel are optimized using
grid-search. The learned functions are very similar; however, fitting KRR is
approx. seven times faster than fitting SVR (both with grid-search). However,
prediction of 100000 target values is more than tree times faster with SVR
since it has learned a sparse model using only approx. 1/3 of the 100 training
datapoints as support vectors.

The next figure compares the time for fitting and prediction of KRR and SVR for
different sizes of the training set. Fitting KRR is faster than SVR for medium-
sized training sets (less than 1000 samples); however, for larger training sets
SVR scales better. With regard to prediction time, SVR is faster than
KRR for all sizes of the training set because of the learned sparse
solution. Note that the degree of sparsity and thus the prediction time depends
on the parameters epsilon and C of the SVR.
"""

# Authors: Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
# License: BSD 3 clause


from __future__ import division
import time

import numpy as np

from sklearn.svm import SVR
from sklearn.grid_search import GridSearchCV
from sklearn.learning_curve import learning_curve
from sklearn.kernel_ridge import KernelRidge
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(style="ticks")
rng = np.random.RandomState(0)

#############################################################################
# Generate sample data
zxc = pd.read_excel('/users/xuguodong/desktop/123.xls');
z = np.array(zxc.ix[:,'df'])

X = np.arange(18630)[:,None]
y = z


X_plot = np.arange(18630,18630+1440)[:,None]

#############################################################################
# Fit regression model
train_size = 24*4*7
C = 10e4
gamma = 10
svr = SVR(kernel='rbf', C=C, gamma=gamma)

t0 = time.time()
svr.fit(X[-train_size:], y[-train_size:])
svr_fit = time.time() - t0

t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0

print y_svr

xk = np.arange(18630+1440)[:,None]
#############################################################################
# look at the results
plt.scatter(X[:], y[:], c='k', label='data')
plt.hold('on')
plt.plot(X_plot, y_svr, c='r',
         label='SVR ')
plt.xlabel('data')
plt.ylabel('target')
plt.title('SVR versus Kernel Ridge')
plt.legend()

# Visualize training and prediction time

plt.show()
