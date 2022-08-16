import streamlit as st
import pickle
import numpy as np

#model
def load_model():
    with open('model_file.p', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

predictor = data["model"]
el_job = data["el_job"]
el_seniority = data["el_seniority"]
el_state = data["el_state"]
    

# Main app engine
if __name__ == "__main__":
    # display title and description
    st.title("🔎 Data Science Jobs Salary Predictor 💸")
    st.write("Get an average estimate of Data Science job salary per State, Job Title & Seniority!")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Data Science Salary Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    job = st.selectbox(
    'What is your job title?',
    ('data analyst', 'data scientist', 'data engineer','machine learning engineer','director', 'manager'))
    st.write('You selected:', job)
    seniority = st.selectbox(
    'What is your seniority level?',
    ('Junior', 'Mid', 'Senior','Not Specified'))
    st.write('You selected:', seniority)
    state = st.selectbox(
    'Which State/Location?',
    ("Remote", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA",
     "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "MI", "MN", "MO", "NC", "ND", "NE",
      "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "TN", "TX", "UT",
       "VA", "WA", "WI"
       ))
    st.write('You selected:', state)
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your forest is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your forest is in danger</h2>
       </div>
    """
    if st.button("Predict"):
        try:
            X = np.array([[job, seniority, state]])
            X[:, 0] = el_job.transform(X[:,0])
            X[:, 1] = el_seniority.transform(X[:,1])
            X[:, 2] = el_state.transform(X[:,2])
            X = X.astype(float)

            salary = predictor.predict(X)
            st.subheader(f"The estimated salary is ${salary[0]:.2f}")

        except ValueError:
            st.subheader("No enough data covering this position/seniority 😕\n Please try with a different one 😅")