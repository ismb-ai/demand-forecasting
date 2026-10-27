"""Synthetic window-alignment demonstration prepared in 2026."""
import numpy as np
from core import prepare_data

if __name__=='__main__':
    series=np.arange(12,dtype=float)
    features,targets=prepare_data(series,window_size=4,horizon=2)
    print('Synthetic consecutive observations: 0 through 11')
    print('Feature shape:',features.shape,'Target shape:',targets.shape)
    print('First:',features[0].tolist(),'->',targets[0].tolist())
    print('Last: ',features[-1].tolist(),'->',targets[-1].tolist())
