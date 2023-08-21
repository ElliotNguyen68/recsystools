from typing import List,Tuple,Optional,Union

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.

def get_user_item_embedding_from_interaction_matrix_svd(
    interaction_matrix:Union[np.ndarray,csr_matrix],
    *args,
    **kwargs,
)->Tuple[np.ndarray,np.ndarray]:
    