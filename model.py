import streamlit as st
import pandas as pd 
import pickle
import ast 
import numpy as np

def run():
  st.header('Welcome to Model Section')

  with open('pipeline.pkl', 'rb') as file_1:
    model = pickle.load(file_1)

  with open('all_process.pkl', 'rb') as file_2:
    final_preprocess = pickle.load(file_2)


  st.header('Predict customer credit card risk!!')

  checking_status = st.selectbox(label=" checking_status ",options=['no checking','<0','0<=X<200','>=200'], index = 1 )
  credit_history = st.selectbox(label=" credit_history ",options=['delayed previously' ,'existing paid' ,'no credits/all paid' ,'all paid',
                  'critical/other existing credit'] , index = 4)
  purpose = st.selectbox(label=" purpose ",options=[ 'used car', 'domestic appliance', 'repairs' ,'furniture/equipment' ,'new car',
                  'radio/tv', 'retraining', 'education', 'business' ,'other'] , index = 4)
  savings_status = st.selectbox(label=" savings_status ",options=[ 'no known savings','<100','100<=X<500','500<=X<1000', '>=1000' ], index = 1 )
  employment = st.selectbox(label=" employment ",options=[ 'unemployed','<1','1<=X<4','4<=X<7','>=7'    ], index = 0 )
  personal_status = st.selectbox(label=" personal_status ",options=[ 'male single', 'female div/dep/mar', 'male div/sep' ,'male mar/wid'], index = 0)
  other_parties = st.selectbox(label=" other_parties ",options=[ 'guarantor','co applicant','none'] , index = 2)
  property_magnitude = st.selectbox(label=" property_magnitude ",options=[ 'real estate','no known property','car','life insurance'])
  other_payment_plans = st.selectbox(label=" other_payment_plans ",options=['stores','none','bank'], index = 1)
  housing = st.selectbox(label=" housing ",options=['rent','for free','own'], index = 1)
  job = st.selectbox(label=" job ",options=['skilled','high qualif/self emp/mgmt', 'unemp/unskilled non res',
          'unskilled resident'])
  own_telephone = st.selectbox(label=" own_telephone ",options= ['yes','none'], index = 1 )
  foreign_worker = st.selectbox(label=" foreign_worker ",options= ['yes','no'] )
  duration = st.slider('duration',4,72 )
  credit_amount = st.slider('credit_amount',250,18424 )
  installment_commitment = st.selectbox(label=" installment_commitment ",options=[ 1,2,3,4] )
  residence_since = st.selectbox(label=" residence_since ",options= [1,2,3,4 ])
  age = st.slider('age',19,75 )
  existing_credits = st.selectbox(label=" existing_credits ",options=[ 1,2,3,4] )
  num_dependents = st.selectbox(label=" num_dependents ",options=[1,2] )


  data_inf = pd.DataFrame({
      'checking_status' : checking_status,
      'credit_history': credit_history,
      'purpose': purpose,
      'savings_status': savings_status,
      'employment' : employment,
      'personal_status': personal_status,
      'other_parties': other_parties,
      'property_magnitude': property_magnitude,
      'other_payment_plans': other_payment_plans,
      'housing': housing,
      'job': job,
      'own_telephone': own_telephone,
      'foreign_worker': foreign_worker,
      'duration': duration,
      'credit_amount': credit_amount,
      'installment_commitment': installment_commitment,
      'residence_since': residence_since,
      'age': age,
      'existing_credits': existing_credits,
      'num_dependents': num_dependents
      }, index =[0])

  st.table(data_inf)

  if st.button(label='predict'):
      # Prediksi Inference-Set
      y_pred_inf = model.predict(data_inf)

      # Menampilkan hasil berdasarkan nilai y_pred_inf
      if y_pred_inf == 1:
          st.write("Hasil: Good")
      else:
          st.write("Hasil: Bad")
          y_segment = final_preprocess.predict(data_inf)
          if y_segment == 1:
            st.write("Kelompok: 0")
            st.write("Ciri-Ciri: 0 diisi oleh anak muda yang sering memakai kartu kredit untuk membeli barang mewah / mahal dimana rata-rata sudah memiliki rumah dan menggunakan tenor yang cepat untuk membayar cicilan kartu kredit")
            st.write("Solusi: Memberikan tenor yang lebih panjang agar bisa memperlancar cicilan , menurunkan limit kartu kredit karena mayoritas cluster 1 membeli barang mahal untuk menghidari gagal bayar")
          else :
            st.write("Kelompok: 1")
            st.write("Ciri-Ciri: 1 disi oleh orang tua yang tinggal bersama anaknya dimana mengisi mengunakan kartu kredit dalam julah kreditnya tinggi dan menggunakan tenor yang lama untuk membayar kartu kredit")
            st.write("Solusi: Memberikan tenor yang lebih pendek agar bisa mengurangi beban bunga, melakukan update data untuk mengerahui sumber dana jika sudah tidak bekerja bisa mengisi sumber dana dari pihak ketiga / anak agar bisa mengetahui pengahasilan per bulan untuk mengatur cara pembayaran berdasarkan penghasilan. Jika memungkinkan memberikan suku bunga yang lebih rendah")