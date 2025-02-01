# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:00:39 2025

@author: VOIB's PC
"""

import pickle
import streamlit as st


fault_detection = pickle.load(open("fault_bina_model.sav", 'rb'))

def main():
    
    
    
    st.title('Fault prediction in three phase')
    Ia = st.text_input('Enter the current for phase 1')
    Ib = st.text_input('Enter the current for phase 2')
    Ic = st.text_input('Enter the current for phase 3')
    Va = st.text_input('Enter the voltage for phase 1')
    Vb = st.text_input('Enter the voltage for phase 2')
    Vc = st.text_input('Enter the voltage for phase 3')


    #code for prediction

    fault_diagnosis = ''
    fault_answer = None


    if st.button('Check for fault'):
        
        fault_answer = fault_detection.predict([[Ia, Ib, Ic, Va, Vb, Vc]])
        
        
        if (fault_answer == 1):
            fault_diagnosis = 'There is a fault'
            
        else:
            fault_diagnosis = 'There is no fault'
        
        
        
    
        
        
        
                
    st.success(fault_diagnosis)
    
    
if __name__ == '__main__':
    main()
    



            
            
            
            
