# imageprocessing
Django project for REST API which manages sending, retrieving and processing of images.

The API follows the **RFC6690** standard for Constrained RESTful Environments (CoRE) and is designed to receive, compress and then save image data into a database for performant file downloads by the API's clients. Supported payload formats are JSON as well as CBOR (Concise Binary Object Representation).

## Prerequisites

- Up-to-date Python version (3.12 is recommended)
- PIP installation
- Virtual environment for setting up Python dependencies (optional)

## Setup

1. Navigate into the project root (where `manage.py` and `requirements.txt` are located)
2. Install Python dependencies on your environment by running `pip install -r requirements.txt`
3. Run `python manage.py runserver` to start up the development server

The application should now run on your environment. The default port for Django applications is `8000`.

For convenience an empty database setup is already included inside the SQLite file `db.sqlite3` on project root level. If you encounter database problems consider removing the file and running `python manage.py migrate` afterwards.

## Usage

For now the API only provides one resource type **image-db** with the semantic interface type **collection**. In accordance with the CoRE standard they can be discovered by sending following GET requests:

```console
curl http://localhost:8000/.well-known/core
curl http://localhost:8000/collections
```
This will give you the following output:

```console
</collections/images>;rt="image-db";if="collection"
```
