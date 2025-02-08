import time
from parser import *
from preprocessing import *
from indexing import *
from ranking import *
from utils import *

dataset = "../scifact/qrels/train.tsv"  # Change to dataset being used
doc_folder_path = '../scifact/corpus.jsonl'
query_file_path = '../scifact/queries.jsonl'
index_file_path = '../IR_Files/inverted_index.json'
preprocessed_docs_path = '../IR_Files/preprocessed_documents.json'
preprocessed_queries_path = '../IR_Files/preprocessed_queries.json'

start_time = time.time()

print("Parsing documents")
documents = []
queries = parse_queries_from_file(query_file_path)

# Preprocess documents and queries - step 1
print("Preprocessing documents")
documents = parse_documents_from_file(doc_folder_path)
documents = preprocess_documents(documents)

print("Preprocessing queries")
queries = preprocess_queries(parse_queries_from_file(query_file_path))

start_time = time.time()

# Build or load inverted index - step 2
print("Building an inverted index.")
inverted_index = build_inverted_index(documents)
end_time = time.time()
print(f"Time taken to build inverted index: {end_time - start_time:.2f} seconds")

doc_lengths = calculate_document_lengths(documents)

results_file = "Results.txt"   #Change to Results.txt for TREC formatting
start_time = time.time()
beir_results = {}

print("Ranking and writing to results file")
start_time = time.time()

bm25 = BM25(inverted_index, doc_lengths)    #Uncomment these 2 lines
writeResults(results_file, queries, bm25)   #To use the baseline BM25

end_time = time.time()
print(f"\nTime taken to rank documents: {end_time - start_time:.2f} seconds")
print(f"Ranking results written to {results_file}")
