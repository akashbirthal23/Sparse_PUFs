import numpy as np
def HT( v, k ):
    t = np.zeros_like( v )
    if k < 1:
        return t
    else:
        ind = np.argsort( abs( v ) )[ -k: ]
        t[ ind ] = v[ ind ]
        return t
def my_fit( X_trn, y_trn ):

    w = np . zeros_like ( X_trn [0])
    v = np . ones_like ( X_trn [0])
    t =0.3 # step length
    lamda =0.01 # regularization constant
    for j in range (100) :
        for i in range (1600) :
            sgt = lamda * v +(1/1600 * X_trn [ i ]) * ( np . dot ( X_trn [ i ] , w . T ) - y_trn [ i ] )
            w = w - t * sgt
        w = HT (w , 512) # our model sparsity is 512
        t = t /1.02
    return w

