from typing import List, Tuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf_feature_extraction(
    training_list_text: List[str], *args, **kwards
) -> Tuple[TfidfVectorizer, np.ndarray]:
    """Using TFIDF to generate text vector

    Args:
        training_list_text (List[str]): Input documents for fiting tfidf

    Returns:
        Tuple[TfidfVectorizer,np.ndarray]:
            TfidfVectorizer : fited tfidf vectorizer
            np.ndarray : transformed training documents

    """
    tfidf_vectorizer = TfidfVectorizer(*args, **kwards)

    tfidf_vectorizer.fit(training_list_text)
    transformed_input = tfidf_vectorizer.transform(training_list_text)

    return tfidf_vectorizer, transformed_input
