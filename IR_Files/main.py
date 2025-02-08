# imports
import time
from parser import *
from preprocessing import *
from indexing import *
from ranking import *
from utils import *
import pytrec_eval
import json

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

# STEP 5 - Working On Trec Evaluation
# print("RETRIEVING THE MAP SCORES")
# qrel = {
#     'q1': {
#         'd1': 0,
#         'd2': 1,
#         'd3': 0,
#     },
#     'q2': {
#         'd2': 1,
#         'd3': 1,
#     },
# }

# run = {
#     'q1': {
#         'd1': 1.0,
#         'd2': 0.0,
#         'd3': 1.5,
#     },
#     'q2': {
#         'd1': 1.5,
#         'd2': 0.2,
#         'd3': 0.5,
#     }
# }

# evaluator = pytrec_eval.RelevanceEvaluator(qrel, {'map', 'ndcg'})

# print(json.dumps(evaluator.evaluate(run), indent=1))

# STEP 5 REVAMPED - Running TREC_EVAL
# Function to read qrel from file (test.tsv)
print("RUNNING TREC EVAL WOOHOO")
# Function to read qrel from file (test.tsv)
def read_qrel(file_path):
    qrel = {}
    with open(file_path, 'r') as f:
        # Skip header row if it exists
        header = f.readline()  # Read and discard the header
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                query_id, doc_id, relevance = parts
                relevance = int(relevance)  # Convert relevance to an integer
                if query_id not in qrel:
                    qrel[query_id] = {}
                qrel[query_id][doc_id] = relevance
    return qrel

# Function to read run from file (Results.txt)
def read_run(file_path):
    run = {}
    with open(file_path, 'r') as f:
        for line in f:
            # Split by any whitespace
            parts = line.strip().split()
            # Ensure we have 6 columns
            if len(parts) >= 5:
                query_id, _, doc_id, rank, score, _ = parts[:6]
                score = float(score)
                if query_id not in run:
                    run[query_id] = {}
                run[query_id][doc_id] = score
    return run

# Load qrel and run from files
qrel_file = "../scifact/qrels/test.tsv"
run_file = 'Results.txt'
qrel = read_qrel(qrel_file)
run = read_run(run_file)

# Evaluate using pytrec_eval
evaluator = pytrec_eval.RelevanceEvaluator(qrel, {'map', 'ndcg'})
results = evaluator.evaluate(run)

# Save the results to a file
output_file = 'evaluation_results.json'
with open(output_file, 'w') as f:
    json.dump(results, f, indent=1)

# Return the path to the results file
print(f"Evaluation results saved to {output_file}")