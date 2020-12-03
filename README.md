# MAIS202 FALL 2020 FINAL PROEJCT: Fake News Detector

## Abstract
This is the McGill MAIS202's Final Project. The goal in this project is to give a "true" or "fake" classification on any news. The proposed and implemented algorithm is the classical Naive Bayes Algorithm. In addition, I have implemented extensive natural language pre-processing, methods such as "stop-words removal" and "lemmatisation" were used to improve the classification accuracy. After Grid-searching on the Multinomial Algorithm and by implementing the best parameters, a test accuracy of 97% was acheived. 
## Repository Structure
The repository contains 2 folders and 2 file:
.
- Delivearbles
  - Deliverable1
    - Data Selection Proposal.pdf
  - Deliverable2
    - Deliverable2.ipynb
    - Delivearble2.pdf
  - Deliverable3
    - Deliverable3.ipynb
    - Deliverable3.pdf
  - Deliverable4
    - Deliverable4.ipynb
  - dataset
    - Fake.csv
    - True.csv
- FinalProject
  - __pycache__
  - env
  - templates
    - fake.html
    - real.html
    - take_input.html
  - app.py
  - predictor.py
  - requirements.txt
## Dataset
https://www.uvic.ca/engineering/ece/isot/datasets/fake-news/index.php

## Usage
The webapp runs locally from terminal or command line. 
To run the webapp, follow the following steps:
1. Clone the sub-directory **FinalProject** 
2. Go to (https://drive.google.com/file/d/17SGESVVtq10bkWkT7gkrNNvTCZj3rvO5/view?usp=sharing) download **my_pipeline.joblib** and place **my_pipeline.joblib** directly under the directory FinalProject. This step is due to the large size of the joblib file.
3. Navigate to the **Final Project** directory and use command `source env/bin/activate` to activate the virtual enviroment
4. Use command `pip install -r requirements.txt` to install all the neccasary import packages
5. Use command `python app.py` to initiate the webapp. This step could take 2-5 minutes due to the complexity of the predicotor model.

Note: The webapp is hosted at [http://127.0.0.1:5000/]

## Sample output:
