import streamlit as st
import numpy as np
from main import predict

# 39 real feature names
feature_names = [
    'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
    'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
    'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount',
    'log_amount', 'hour', 'transaction_rate', 'V1_x_logAmt', 'V2_x_logAmt',
    'V3_x_logAmt', 'V4_x_logAmt', 'V10_x_logAmt', 'V14_x_logAmt'
]


def main():
    st.title("Credit Card Fraud Detection App")

    st.write("Enter the transaction details below:")

    input_data = []
    for feature in feature_names:
        value = st.number_input(f"{feature}", format="%.6f")
        input_data.append(value)

    if st.button("Predict"):
        # Convert input to numpy array and reshape for prediction
        input_array = np.array([input_data])
        prediction = predict(input_array)

        # Show result
        if prediction[0] == 1:
            st.error("⚠️ This transaction is predicted to be **Fraudulent**.")
        else:
            st.success("✅ This transaction is predicted to be **Not Fraudulent**.")


if __name__ == '__main__':
    main()
