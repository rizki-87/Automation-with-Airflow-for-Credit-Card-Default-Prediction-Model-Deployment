# Automation with Airflow for Credit Card Default Prediction Model Deployment
In this repository, we have implemented an end-to-end automation process using Apache Airflow for deploying a predictive model focused on determining the likelihood of credit card holders defaulting on their payments. This project encompasses several essential steps, from data collection and preprocessing to model development, deployment, and monitoring.

## Table of Contents
  1. About the Project
  2. Getting Started
  3. How the Model Works
  4. Setting Up and Configuring Airflow
  5. How to Run
  6. Contact and Contribution

## About the Project
This project aims to predict whether a credit card holder will default based on several features such as credit history, monthly income, number of dependents, and more. By leveraging Apache Airflow, we can automate the process of training, evaluating, and deploying this model with ease.

  This project was created by:

    - Rizki Pria Aditama as a Data Engineer
    - Kenneth Vincentius as a Data Analyst
    - Harari Netanya Theon as a Data Scientist
    - Rais Yufli Xavierullah as a Data Scientist

## How the Model Works
The model is trained using a dataset containing the history of credit card holders. Some of the features used include:

  * credit_history
  * purpose
  * personal_status
  * other_parties
  * property_magnitude
  * other_payment_plans
  * housing
  * foreign_worker
  * checking_status 
  * savings_status 
  * employment
  * age              
  * duration         
  * credit_amount 

This model utilizes the Naive Bayes algorithm and has achieved an accuracy of 81% on the test dataset.

## Setting Up and Configuring Airflow
Ensure you've installed Apache Airflow. 
Copy the DAG file (Final_Project_G1_DAG.py.py) to your Airflow DAGs folder.
Adjust the configurations in the airflow.cfg file as needed.

## How to Run
- Start Apache Airflow with the command:
  <img src:"https://cdn.discordapp.com/attachments/1161568624461484136/1166287877500575784/image.png 
  ex=6549f13a&is=65377c3a&hm=8bb14c3292ef38e863fec6adc568021b4c5bfafa6e4db1f735b737fb641adb54&" width="500" height="300">
