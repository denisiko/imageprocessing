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

For now the API only provides one resource type for an image collection with the semantic notation `simple.act` and the semantic interface type **batch** with the notation `core.b`. In accordance with the CoRE standard they can be discovered by sending following GET requests:

```console
curl http://localhost:8000/.well-known/core
curl http://localhost:8000/collections
```
This will give you the following output:

```console
</collections/images>;rt="simple.act";if="core.b"
```

For sending image data you can make a POST request to this resource link. The payload must contain values for the keys `deviceId`, `timestamp` and `imageData`. The value for `imageData` must consist of a base64 string encoding the file's binary content. `timestamp` must contain a valid ISO 8601 datetime representation. Valid payload formats are JSON and CBOR.

### JSON Example

```console
curl -d '{"deviceId":"12345", "timestamp":"2024-08-18T02:04:07Z", "imageData":"iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TpUUqglYQcchQnSz4hThqFYpQIdQKrTqYXPoFTRqSFBdHwbXg4Mdi1cHFWVcHV0EQ/ABxdnBSdJES/5cUWsR6cNyPd/ced+8AoVZimtUxBmi6bSbjMTGdWRUDrwiiF36Mo19mljEnSQm0HV/38PH1Lsqz2p/7c3SrWYsBPpF4lhmmTbxBPL1pG5z3icOsIKvE58SjJl2Q+JHrisdvnPMuCzwzbKaS88RhYjHfwkoLs4KpEU8RR1RNp3wh7bHKeYuzVqqwxj35C0NZfWWZ6zSHEMciliBBhIIKiijBRpRWnRQLSdqPtfEPun6JXAq5imDkWEAZGmTXD/4Hv7u1cpMTXlIoBnS+OM7HMBDYBepVx/k+dpz6CeB/Bq70pr9cA2Y+Sa82tcgR0LMNXFw3NWUPuNwBBp4M2ZRdyU9TyOWA9zP6pgzQdwt0rXm9NfZx+gCkqKvEDXBwCIzkKXu9zbuDrb39e6bR3w9rrHKkUDJpUAAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+gIEgMzEWA+HAEAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAh0lEQVQ4y+1TwQ3EIAyzq5sI9h8hrOQ+ckorIJzavk6qXwk4dhIBJeEuNjzAnxZzepptsbUGoNb6JZjZtHgEMp6rKId7RGBmZoazaic/Gp5VJH1W+yCDimw3U+eYYjEjPSHpdx7EFksp0UWoH+Quj3jspTM4ihdjZ0KSfryw6H8cHgDfL3kNO33Qwgk1AJAGAAAAAElFTkSuQmCC"}' -H "Content-Type: application/json" -X POST http://localhost:8000/collections/images
```

### CBOR Example

```console
curl -d 'a36864657669636549646531323334356974696d657374616d7074323032342d30382d31385430323a30343a30375a69696d6167654461746179037c6956424f5277304b47676f414141414e535568455567414141425141414141554341494141414143363470614141414268476c445131424a51304d6763484a765a6d6c735a5141414b4a46396b543149773041637856395470555571676c5951636368516e537a3468546871465970514964514b7254715958506f46545271534642644877625867344d64693163484657566348563045512f414278646e4253644a45532f35635557735236634e7950642f6365642b38416f565a696d745578426d69366253626a4d54476457525544727769694633364d6f31396d6c6a456e53516d3048562f33385048314c73717a32702f376333537257597342507046346c686d6d54627842504c317047357a3369634f73494b76453538536a4a6c32512b4a4872697364766e504d75437a777a624b615338385268596a4866776b6f4c73344b70455538525231524e703377683762484b6559757a56717177786a333543304e5a6657575a367a5348454d63696c6942426849494b69696a42527052576e52514c5364715074664550756e364a58417135696d446b5745415a476d5458442f34487637753163704d54586c496f426e532b4f4d37484d42445942657056782f6b2b64707a364365422f42713730707239634132592b5361383274636752304c4d4e584677334e575550754e77424270344d325a526479553954794f5741397a503670677a516477743072586d394e665a782b67436b714b76454458427743497a6b4b5875397a62754472623339653662523377397272484b6b55444a705541414141416c7753466c7a41414175497741414c694d42654b552f646741414141643053553146422b674945674d7a4557412b484145414141415a6445565964454e766257316c626e514151334a6c5958526c5a4342336158526f4945644a54564258675134584141414168306c4551565134792b3154775133454941797a7135734939683868724f512b636b6f72494a7a61766b367158776b34646849424a6545754e6a7a416e785a7a65707074736255476f4e62364a5a6a5a744867454d7036724b4964375247426d5a6f617a6169632f477035564a4831572b794344696d7733552b6559596a456a5053487064783745466b73703055576f482b51756a336a7370544d346968646a5a304b536672797736483863486744664c336b4e4f33335177676b31414a41474141414141456c46546b5375516d4343' -H "Content-Type: application/cbor" -X POST http://localhost:8000/collections/images
```

After successfully sending the image you will get a confirmation in the form of a response with the status `201` and the newly created image's metadata as content.

For downloading an image file make a GET request to the resource link as following:

```console
curl 'http://localhost:8000/collections/images?deviceId=12345&timestamp=2024-08-18T02%3A04%3A07Z' -o image.png
```

The GET parameters `deviceId` and `timestamp` are obligatory. `timestamp` must be properly URL-encoded. If the parameters are not provided or invalid you will get a `400` response. If they do not match an existing image you will get a `404` response.
