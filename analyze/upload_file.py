import requests
from io import BytesIO


def create_vector_store(client, name="default_store"):
    vector_store = client.vector_stores.create(name=name)
    print(
        f'Vector store {name} was created successfully')
    return vector_store


def add_file_to_vector_store(client, vector_store, file):
    print(f'==> Adding {file.name}to vector store with id {vector_store.name}')
    client.vector_stores.files.create(
        vector_store_id=vector_store.id, file_id=file.id)


def upload_file(client, path, file_name):
    file_path = path + file_name
    with open(file_path, "rb") as file_content:
        result = client.files.create(
            file=file_content,
            purpose="assistants"
        )
    return result


# -> Methods
def check_method_1_file_limit(file_names):
    if len(file_names) > 5:
        print("You have exceeded the limit of 5 files")
        return False
    else:
        return True


def method1(client, path, file_names):
    file_ups = []
    vector_store_list = []
    vector_store = create_vector_store(client)
    vector_store_list.append(vector_store)
    for file_name in file_names:
        file_up = upload_file(client, path, file_name)
        file_ups.append(file_up)
        add_file_to_vector_store(client, vector_store, file_up)
    return vector_store_list


def method2(client, path, file_names):
    x = 1
    vector_store_list = []
    for file_name in file_names:
        vector_store = create_vector_store(client, name=f"store_{x}")
        x += 1
        file_up = upload_file(client, path, file_name)
        add_file_to_vector_store(client, vector_store, file_up)
        vector_store_list.append(vector_store)
    return vector_store_list

# def check_files_in_vector_store(client, vector_store_id):
#     result = client.vector_stores.files.list(
#         vector_store_id=vector_store_id)
    # pp(
    #     f"Files in vector store {vector_store_id} are {result} - Total # {len(result)}")
    # print(result)


if __name__ == "__main__":
    pass
