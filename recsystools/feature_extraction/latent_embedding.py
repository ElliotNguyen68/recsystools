from typing import List, Tuple, Optional, Union

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD


def get_user_item_embedding_from_interaction_matrix_svd(
    interaction_matrix: Union[np.ndarray, csr_matrix],
    n_components: int,
    n_iter: int,
    *args,
    **kwargs,
) -> Tuple[np.ndarray, np.ndarray,TruncatedSVD]:
    svd = TruncatedSVD(n_components=n_components, n_iter=n_iter, random_state=5,*args,**kwargs)

    U = svd.fit_transform(interaction_matrix)
    # Sigma = np.diag(svd.singular_values_)
    V = svd.components_
    
    return U,V.T,svd

    