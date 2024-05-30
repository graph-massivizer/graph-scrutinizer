# BETA TESTING
- Download the following files: 
  - [Citation network - tiny](https://drive.google.com/file/d/1FpaARB7sCDHd_L5mSMgESjkbI9kzveto/view?usp=sharing)
  - [Citation network - small](https://drive.google.com/file/d/1NrN4YTX8Qy1sJbtP9BBnCCyUrGNQKOe0/view?usp=sharing)
- Make sure Docker is installed on your machine
- In the directory: persistence-layer, execute: `docker-compose up`
- In the directory: consumer, execute: `python consumer-betweenness-centrality.py`
  - Make sure the Python environment for the consumer has Redis installed (pip install redis)
- In the directory: rest-api, execute:
```
export PYTHONPATH=$PWD
python app/main.py
```
  - Make sure the required dependencies are installed! Please take a look at the README.md for details.

- Open the following URL: http://localhost:8000/docs
 - Go to the following endpoint: `POST /scrutinizer/requests/betweenness-centrality`
 - Issue the POST request and validate the response was successful
- Provide feedback on the beta-testing questionnaire
