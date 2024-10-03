import streamlit as st
import pandas as pd
import json

# Set the title of the Streamlit app
st.title("JSON File Uploader")

# File uploader for following JSON files
uploaded_file_following = st.file_uploader("Upload a JSON file for Following", type=["json"], key="following")

if uploaded_file_following is not None:
    try:
        json_data = json.load(uploaded_file_following)
        if "following" in json_data:
            data = json_data['following']
            df = pd.json_normalize(data)
            st.write("Here is the data from the uploaded JSON file for Following:")
            st.dataframe(df)
        else:
            st.error("The JSON file does not contain the expected 'following' key.")
    except Exception as e:
        st.error(f"An error occurred while reading the JSON file for Following: {e}")

# File uploader for followers JSON files
uploaded_file_followers = st.file_uploader("Upload a JSON file for Followers", type=["json"], key="followers")

if uploaded_file_followers is not None:
    try:
        json_data = json.load(uploaded_file_followers)
        if "followers" in json_data:
            data = json_data['followers']
            df = pd.json_normalize(data)
            st.write("Here is the data from the uploaded JSON file for Followers:")
            st.dataframe(df)
        else:
            st.error("The JSON file does not contain the expected 'followers' key.")
    except Exception as e:
        st.error(f"An error occurred while reading the JSON file for Followers: {e}")

# File uploader for likes JSON files
uploaded_file_likes = st.file_uploader("Upload a JSON file for Likes", type=["json"], key="likes")

if uploaded_file_likes is not None:
    try:
        json_data = json.load(uploaded_file_likes)
        if "likes" in json_data:
            data = json_data['likes']
            df = pd.json_normalize(data)
            st.write("Here is the data from the uploaded JSON file for Likes:")
            st.dataframe(df)
        else:
            st.error("The JSON file does not contain the expected 'likes' key.")
    except Exception as e:
        st.error(f"An error occurred while reading the JSON file for Likes: {e}")

# File uploader for tweets JSON files
uploaded_file_tweets = st.file_uploader("Upload a JSON file for Tweets", type=["json"], key="tweets")

if uploaded_file_tweets is not None:
    try:
        json_data = json.load(uploaded_file_tweets)
        if "tweets" in json_data:
            data = json_data['tweets']
            df = pd.json_normalize(data)
            st.write("Here is the data from the uploaded JSON file for Tweets:")
            st.dataframe(df)
        else:
            st.error("The JSON file does not contain the expected 'tweets' key.")
    except Exception as e:
        st.error(f"An error occurred while reading the JSON file for Tweets: {e}")

# File uploader for users JSON files
uploaded_file_users = st.file_uploader("Upload a JSON file for Users", type=["json"], key="users")

if uploaded_file_users is not None:
    try:
        json_data = json.load(uploaded_file_users)
        if "users" in json_data:
            data = json_data['users']
            df = pd.json_normalize(data)
            st.write("Here is the data from the uploaded JSON file for Users:")
            st.dataframe(df)
        else:
            st.error("The JSON file does not contain the expected 'users' key.")
    except Exception as e:
        st.error(f"An error occurred while reading the JSON file for Users: {e}")
