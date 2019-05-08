from google.cloud import bigquery
import os

client = bigquery.Client()

dataset_name = os.environ['dataset_name']
table_name = os.environ['table_name']

dataset_id = "{}.{}".format(client.project,dataset_name)

# Construct a full Dataset object to send to the API.
dataset = bigquery.Dataset(dataset_id)

# TODO(developer): Specify the geographic location where the dataset should reside.
dataset.location = "US"

# Send the dataset to the API for creation.
# Raises google.api_core.exceptions.Conflict if the Dataset already
# exists within the project.
dataset = client.create_dataset(dataset)  # API request
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))


schema = [
    bigquery.SchemaField("segmentid", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_traffic", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_length", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_tost", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_last_updt", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_lif_lat", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_strheading", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("street", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("start_lon", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_lit_lon", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_lit_lat", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_direction", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_fromst", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("_comments", "STRING", mode="REQUIRED")
]

# TODO(developer): Set table_id to the ID of the table to create
#table_id = "your-project.your_dataset.your_table_name"
table_id = client.project + "." + dataset.dataset_id + "." + table_name

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # API request
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

