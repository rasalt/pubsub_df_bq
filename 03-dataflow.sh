gcloud dataflow jobs run $dataflowjobname \
    --gcs-location gs://dataflow-templates/latest/PubSub_to_BigQuery \
    --parameters \
inputTopic=projects/$PROJECT_ID/topics/$topic,\
outputTableSpec=$PROJECT_ID:$dataset_name.$table_name
