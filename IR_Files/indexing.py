def build_inverted_index(documents):
    """
    Build an inverted index from the preprocessed documents
    """
    inverted_index = {}
    for doc in documents:
        doc_id = doc['DOCNO']
        text_tokens = doc['TEXT']
        for token in text_tokens:
            if token not in inverted_index:
                inverted_index[token] = {}
            inverted_index[token][doc_id] = inverted_index[token].get(doc_id, 0) + 1
    return inverted_index

def calculate_document_lengths(documents):
    """
    Calculate the length of each document based on the number of terms
    """
    doc_lengths = {}
    for doc in documents:
        doc_id = doc['DOCNO']
        text_tokens = doc['TEXT']
        doc_length = len(text_tokens)
        doc_lengths[doc_id] = doc_length
    return doc_lengths

# ==============================================
# below is for when it's being run only on heads

def build_inverted_index_head_only(documents):
    """
    Build an inverted index from the preprocessed documents
    """
    inverted_index = {}
    for doc in documents:
        doc_id = doc['DOCNO']
        text_tokens = doc['HEAD']
        for token in text_tokens:
            if token not in inverted_index:
                inverted_index[token] = {}
            inverted_index[token][doc_id] = inverted_index[token].get(doc_id, 0) + 1
    return inverted_index

def calculate_document_lengths_head_only(documents):
    """
    Calculate the length of each document based on the number of terms
    """
    doc_lengths = {}
    for doc in documents:
        doc_id = doc['DOCNO']
        text_tokens = doc['HEAD']
        doc_length = len(text_tokens)
        doc_lengths[doc_id] = doc_length
    return doc_lengths