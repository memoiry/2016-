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

rng = np.random.RandomState(0)

#############################################################################
# Generate sample data
zxc = pd.read_excel('/users/xuguodong/desktop/data1/result1.xls');
z = np.array(zxc.ix[:,'data'])

X = np.arange(194)[:,None]
y = z


X_plot = np.arange(0,210)[:,None]

#############################################################################
# Fit regression model
train_size = 18630
C = 3e6
gamma = 0.01
svr = SVR(kernel='rbf', C=C, gamma=gamma)
alpha = 0.23
gamma1 = 0.01
kr = KernelRidge(kernel='rbf', gamma=gamma1,alpha = alpha)

t0 = time.time()
svr.fit(X[:train_size], y[:train_size])
svr_fit = time.time() - t0

t0 = time.time()
kr.fit(X[:train_size], y[:train_size])
kr_fit = time.time() - t0

t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0

t0 = time.time()
y_kr = kr.predict(X_plot)
kr_predict = time.time() - t0

xk = np.arange(18630+1440)[:,None]
#############################################################################
# look at the results
err1 = np.abs(svr.predict(X)-z)/z
err2 = np.abs(kr.predict(X)-z)/z
x1 = X.flatten()
x2 = x1
x1 = pd.DataFrame({'x':x1,'svr error %':err1,'kr error %':err2})
x2 = pd.DataFrame({'svr predict':y_svr,'kr predict': y_kr})
x2.to_excel('/users/xuguodong/desktop/data1/solution results.xls')
x1 = pd.melt(x1, id_vars=["x"], var_name="condition")
sns.lmplot(data = x1, x = 'x', y = 'value', hue = 'condition', ci=None, scatter_kws={"s": 80},lowess = True)
sv_ind = svr.support_
plt.figure()
plt.scatter(X[:], y[:], c='k', label='data')
plt.hold('on')
plt.plot(X_plot, y_svr, c='r',
         label='SVR ')
plt.plot(X_plot, y_kr, c='g',
         label='KRR' )
plt.xlabel('data')
plt.ylabel('target')
plt.title('SVR versus Kernel Ridge')
plt.legend()
plt.show()
