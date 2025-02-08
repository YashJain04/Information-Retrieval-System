# imports
import time
from parser import *
from preprocessing import *
from indexing import *
from ranking import *
from utils import *

# file directories
dataset = "../scifact/qrels/train.tsv" # not accessed
doc_folder_path = '../scifact/corpus.jsonl'
query_file_path = '../scifact/queries.jsonl'
index_file_path = '../IR_Files/inverted_index.json'
preprocessed_docs_path = '../IR_Files/preprocessed_documents.json'
preprocessed_queries_path = '../IR_Files/preprocessed_queries.json'

# STEP 0 - Parse the document
start_time = time.time() # start the timer
print("Parsing documents")
documents = []
queries = parse_queries_from_file(query_file_path)
end_time = time.time() # end the timer
print(f"Time taken to complete STEP 0 (PARSING DOCS): {end_time - start_time:.2f} seconds")

# STEP 1 - Preprocess documents and queries
start_time = time.time() # start the timer
print("Preprocessing documents")
documents = parse_documents_from_file(doc_folder_path)
documents = preprocess_documents(documents)
print("Preprocessing queries")
queries = preprocess_queries(parse_queries_from_file(query_file_path))
end_time = time.time() # end the timer
print(f"Time taken to complete STEP 1 (PREPROCESS DOCS/QUERIES): {end_time - start_time:.2f} seconds")

# STEP 2 - Build or load inverted index
start_time = time.time() # start the timer
print("Building an inverted index.")
inverted_index = build_inverted_index(documents)
end_time = time.time() # end the timer
print(f"Time taken to complete STEP 2 (BUILD INVERTED INDEX): {end_time - start_time:.2f} seconds")


# STEP 3 - Retrieval and ranking
start_time = time.time() # start the timer
doc_lengths = calculate_document_lengths(documents)
results_file = "Results.txt"   # change to Results.json for other version formatting
beir_results = {}
print("Ranking and writing to results file")
bm25 = BM25(inverted_index, doc_lengths)
writeResults(results_file, queries, bm25, "run_name")
end_time = time.time() # end the timer
print(f"\nTime taken to complete STEP 3 (RANKING DOCUMENTS): {end_time - start_time:.2f} seconds")

# STEP 4 - Return results
print(f"Ranking results written to {results_file}")
