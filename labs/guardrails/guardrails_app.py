import streamlit as st #all streamlit commands will be available through the "st" alias
import guardrails_lib as glib #reference to local lib script

#
st.set_page_config(page_title="Guardrails") #HTML title
st.title("Guardrails") #page title

col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("Input text", label_visibility="collapsed") #display a multiline text box with no label
    go_button = st.button("Go", type="primary") #display a primary button

if go_button: #code in this if block will be run when the button is clicked
    
    with col1:
        with st.spinner("Working..."): #show a spinner while the code in this with block runs
            response_content, guardrail_action, trace = glib.get_text_response(prompt=input_text) #call the model through the supporting library
            st.write(response_content) #display the response content
            
    with col2:
        st.write("### Guardrail action")
        st.write(guardrail_action)
        
        st.write("### Trace")
        st.write(trace)