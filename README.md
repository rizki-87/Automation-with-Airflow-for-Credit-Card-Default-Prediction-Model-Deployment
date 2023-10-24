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

    airflow webserver

- Open the Apache Airflow web interface in your browser.
- Activate the DAG named [DAG Name] and run it.

## Contact and Contribution
If you have questions or would like to contribute to this project, please contact Rizki Pria Aditama at rizki.aditama87@gmail.com or create a Pull Request.
