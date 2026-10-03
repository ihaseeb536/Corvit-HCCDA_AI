import streamlit as st

st.title('Welcome to Kamran --> HCCDA-AI')
st.header("This is a header") 
st.subheader("This is a subheader")

st.markdown('#### 4th heading')

st.text(2)

st.write(2)

st.success("Registeration successful")

st.info("For more Information")

st.warning("Warning")
 
# success
st.error("Error")


if st.checkbox('Male'):
    st.text('You are male.')

if st.checkbox('Female'):
    st.text('You are female.')

status = st.radio("Select Gender: ", ('Male', 'Female'))

if status == 'Male':
    st.success('You are brave..')
else:
    st.success('You are a kind lady')

hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby)

hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])
 
# write the selected options
st.write("You selected", len(hobbies), hobbies, 'hobbies')

if st.button("Click me for no reason", type='primary'):
    st.write('Hello')

level = st.slider("Select the level", 1, 10)