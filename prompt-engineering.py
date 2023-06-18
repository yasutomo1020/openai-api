# LlamaIndexを使って、プロンプトエンジニアリングを行う
import os

from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# 保存先のディレクトリ
persist_dir = "./storage/"

print("create index? (y/n):")
input_str = input()
if input_str == "y":
    # save to disk
    print("create new index")
    if not os.path.exists(persist_dir):
        os.mkdir(persist_dir)
    documents = SimpleDirectoryReader("data").load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir)
    # load from disk
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    # load index
    index = load_index_from_storage(storage_context)

else:
    print("load index from disk")
    # load from disk
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    # load index
    index = load_index_from_storage(storage_context)

# プロンプトエンジニアリング


def print_response(prompt: str, index):
    query_engine = index.as_query_engine()
    print(query_engine.query(prompt))


print("input prompt:")

input_prompt = input()
print_response(input_prompt, index)
