import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "all_products"

try:
    es = Elasticsearch(
        "http://localhost:9200"
    )
except ConnectionError as e:
    print("Connection Error:", e)

if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")


def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "vector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": 500
    }
    res = es.knn_search(index="movies", knn=query, source=["title", "extract", "thumbnail"]
                        )
    results = res["hits"]["hits"]

    return results


def main():
    st.title("Search Movies")

    search_query = st.text_input("Enter your search query")

    if st.button("Search"):
        if search_query:
            results = search(search_query)
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        col1, col2 = st.columns([1, 4])
                        with col1:
                            try:
                                st.image(result['_source']
                                         ['thumbnail'], width=100)
                            except Exception as e:
                                print(e)
                        with col2:
                            try:
                                st.header(f"{result['_source']['title']}")
                            except Exception as e:
                                print(e)
                            try:
                                st.write(
                                    f"Description: {result['_source']['extract']}")
                            except Exception as e:
                                print(e)
                        st.divider()


if __name__ == "__main__":
    main()
