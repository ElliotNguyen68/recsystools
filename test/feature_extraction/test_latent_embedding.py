import numpy as np

from recsystools.feature_extraction import latent_embedding


def test_get_user_item_embedding_from_interaction_matrix_svd():
    n_users = 10
    n_items = 20

    rand_interaction_matrix = np.random.rand(n_users, n_items)

    (
        users_embedding,
        items_embedding,
        svd,
    ) = latent_embedding.get_user_item_embedding_from_interaction_matrix_svd(
        rand_interaction_matrix, n_components=5, n_iter=2, algorithm="arpack"
    )

    assert users_embedding.shape == (10, 5)
    assert items_embedding.shape == (20, 5)

    assert (
        users_embedding @ np.diag(svd.singular_values_) @ items_embedding.T
    ).shape == (10, 20)


def test_get_user_item_embedding_from_interaction_matrix_matrix_factorization():
    n_users = 10
    n_items = 20

    rand_interaction_matrix = np.random.rand(n_users, n_items)

    (
        users_embedding,
        items_embedding,
        nmf,
    ) = latent_embedding.get_user_item_embedding_from_interaction_matrix_matrix_factorization(
        rand_interaction_matrix, n_components=5, n_iter=2
    )

    assert users_embedding.shape == (10, 5)
    assert items_embedding.shape == (20, 5)

    assert (users_embedding @ items_embedding.T).shape == (10, 20)
