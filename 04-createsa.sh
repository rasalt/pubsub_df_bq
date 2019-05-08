gcloud iam service-accounts create $pubsubsa --display-name "pubsub"
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$pubsubsa@$PROJECT_ID.iam.gserviceaccount.com --role roles/pubsub.publisher
gcloud iam service-accounts keys create ./$pubsubsa.json --iam-account $pubsubsa@$PROJECT_ID.iam.gserviceaccount.com
gcloud compute scp $pubsubsa.json $pubinstance:~/. --zone=$zone

