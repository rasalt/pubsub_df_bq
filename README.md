This code example shows how setup a streaming job (chicago traffic real time dataset)
send it to pubsub and direct it to Bigquery with a Dataflow job

Steps to run this code.
-------------------------


Prerequisites:

 1- Edit the environment file to have your project id etc
    vi env.sh 
 
Source this environment file

 2- source env.sh 

 3- On code shell: Run script to create the Bigquery dataset and tables
    python ./01-bqcreate.py

 4- On code shell: Run script to create pubsub topic 
    python ./02-createpubsub.py

 5- On cloud shell run the shell script to setup the dataflow pipeline
    ./03-dataflow.sh

 6-Create a GCE instance

  Install packages 

  sudo apt install python python-dev python3 python3-dev
  sudo pip install google-cloud-pubsub
  sudo pip install pandas
  sudo pip install sodapy

7- Go back to Cloud shell and run the script to create service accounts.
   This script copies the service account key to the instance created.

   ./createsa.sh

8- SSH to the GCE instance in step 6 
   
  Clone the same repo her on this instance
  Add a line like this
 
  export GOOGLE_APPLICATION_CREDENTIALS="Service account key created in step 7" and the right path 

  Edit the ~/.bash_alias file and add a line thus 
  source env.sh
  
  Edit the cronpublish.sh file.  
  Add a line to cron scheduler

  crontab -e 

  * * * *  * <path to cronpublish.py> 
   
  sudo service cron reload

9- Continue to the cloud console go to BigQuery and explore the database
 
