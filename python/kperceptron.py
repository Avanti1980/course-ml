import numpy as np

rng = np.random.RandomState(1234567)
np.random.seed(1234567)


class KPerceptron(object):
    """
    X: nd*nx
    y: (nx,)
    """

    def __init__(self, kerntype='poly', kerngamma=1, kerncoef0=1, kerndegree=2,
                 batch_size=100, ybias=0):
        self.kernfunc = getattr(self, '_kern_'+kerntype)
        self.kerngamma = kerngamma
        self.kerncoef0 = kerncoef0
        self.kerndegree = kerndegree
        self.batch_size = batch_size
        self.ybias = ybias

    def _kern_lin(self, xij):
        return np.dot(self.SV[self.svindex], xij)

    def _kern_poly(self, xij):
        dp = np.dot(self.SV[self.svindex], xij)
        return (self.kerngamma*dp+self.kerncoef0)**self.kerndegree

    def _kern_rbf(self, xij):
        """
        sv:  ns x nd
        xij: nd x nk
        """
        sv = self.SV[self.svindex]
        x_sq = (xij**2).sum(axis=0)  # (nk,)
        sv_sq = (sv**2).sum(axis=1)  # (ns,)
        return np.exp(-2*self.kerngamma * (x_sq + (-2*np.dot(sv, xij) + sv_sq.reshape(sv_sq.shape[0], 1))))

    def __getYHat(self, xij, beta):
        if self.svindex.any():
            a = np.dot(beta[:, self.svindex], self.kernfunc(xij.T))
            return a.argmax(0)+1
        else:
            return np.ones(xij.shape[0], dtype=np.int)

    def __batch_fit(self, batch_indexes, Xtrn, ytrn):
        Xbatch, ybatch = Xtrn[batch_indexes, :], ytrn[batch_indexes]
        z = self.__getYHat(Xbatch, self.beta)
        updates = (z != ybatch)
        self.beta2 += self.beta
        if updates.any():
            uInd = batch_indexes[updates]
            self.svindex[uInd] = True
            self.beta[ybatch[updates]-1, uInd] += 1
            self.beta[z[updates]-1, uInd] += -1
            self.beta2 += self.beta

    def partial_fit(self, Xtrn, ytrn, classes=None):
        ytrn = ytrn + self.ybias
        if not hasattr(self, 'SV'):
            assert (np.unique(ytrn) == np.arange(1, ytrn.max()+1)).all()
            nx, nd, nc = Xtrn.shape[0], Xtrn.shape[1], ytrn.max()
            self.nx, self.nc = nx, nc
            self.beta = np.zeros((nc, nx), dtype=np.int)
            self.beta2 = np.zeros((nc, nx), dtype=np.int)
            self.svindex = np.zeros(nx, dtype=np.bool)
            self.SV = Xtrn
            assert self.SV.shape == (nx, nd)
        indexes = np.random.permutation(self.nx)
        for i in np.arange(0, self.nx, self.batch_size):
            self.__batch_fit(indexes[i:min(i+self.batch_size, self.nx)], Xtrn, ytrn)

    def predict(self, X):
        return self.__getYHat(X, self.beta2) - self.ybias

    def score(self, X, y):
        y = y+self.ybias
        z = self.__getYHat(X, self.beta2)
        return np.sum(z == y)/float(y.size)
