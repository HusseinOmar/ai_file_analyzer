import requests
from io import BytesIO
# from get_files import get_files

# path, file_names = get_files()


def create_vector_store(client, name="default_store"):
    vector_store = client.vector_stores.create(name=name)
    print(
        f'Vector store {name} was created successfully')
    return vector_store


def add_file_to_vector_store(client, vector_store, file):
    print(f'==> Adding {file.id} to vector store with id {vector_store.name}')
    client.vector_stores.files.create(
        vector_store_id=vector_store.id, file_id=file.id)


def upload_file(client, path, file_name):
    if path[-1] != "/":
        path += "/"
    file_path = path + file_name
    with open(file_path, "rb") as file_content:
        file = client.files.create(
            file=file_content,
            purpose="assistants"
        )
    return file


def build_store(client, path, file_names):
    x = 1
    build_store = []
    for file_name in file_names:
        build = {}
        vector_store = create_vector_store(client, name=f"store_{x}")
        x += 1
        file_up = upload_file(client, path, file_name)
        add_file_to_vector_store(client, vector_store, file_up)
        build['store'] = vector_store
        build['file'] = file_up
        build_store.append(build)
    return build_store
