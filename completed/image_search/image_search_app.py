import streamlit as st #all streamlit commands will be available through the "st" alias
import image_search_lib as glib #reference to local lib script


st.set_page_config(page_title="Image Search", layout="wide") #HTML title
st.title("Image Search") #page title


search_images_tab, find_similar_images_tab = st.tabs(["Image search", "Find similar images"])


with search_images_tab:

    search_col_1, search_col_2 = st.columns(2)

    with search_col_1:
        input_text = st.text_input("Search for:") #display a multiline text box with no label
        search_button = st.button("Search", type="primary") #display a primary button

    with search_col_2:
        if search_button: #code in this if block will be run when the button is clicked
            st.subheader("Results")
            with st.spinner("Searching..."): #show a spinner while the code in this with block runs
                response_content = glib.get_similarity_search_results(search_term=input_text)
                
                for res in response_content:
                    st.image(res, width=250)


with find_similar_images_tab:
    
    find_col_1, find_col_2 = st.columns(2)

    with find_col_1:
    
        uploaded_file = st.file_uploader("Select an image", type=['png', 'jpg'])
        
        if uploaded_file:
            uploaded_image_preview = uploaded_file.getvalue()
            st.image(uploaded_image_preview)
    
        find_button = st.button("Find", type="primary") #display a primary button

    with find_col_2:
        if find_button: #code in this if block will be run when the button is clicked
            st.subheader("Results")
            with st.spinner("Finding..."): #show a spinner while the code in this with block runs
                response_content = glib.get_similarity_search_results(search_image=uploaded_file.getvalue())
                
                for res in response_content:
                    st.image(res, width=250)
            
