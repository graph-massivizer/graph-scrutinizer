# BETA TESTING
- Download the following file: https://drive.google.com/file/d/1FpaARB7sCDHd_L5mSMgESjkbI9kzveto/view?usp=sharing
- Make sure Docker is installed on your machine
- In the directory: persistence-layer, execute: docker-compose up
- In the directory: consumer, execute: python consumer-betweenness-centrality.py
  - Make sure the python environment for the consumer has redis installed (pip install redis)
- In the directory: rest-api, execute: 
export PYTHONPATH=$PWD
python app/main.py
  - Make sure the required dependencies are installed! Check the README.md for details.

- Open the following URL: http://localhost:8000/docs
 - Go to the following endpoint: POST /scrutinizer/requests/betweenness-centrality
 - Issue the POST request and validate the response was successful
- Provide feedback at the beta-testing questionnaire
