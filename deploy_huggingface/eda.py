# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow_hub import KerasLayer

st.set_page_config(layout='centered',
                   page_title='Spotify')


def run():
    #image
    st.image('https://www.adweek.com/wp-content/uploads/2024/05/spotify-newfronts-video-inventory-2024.jpg?w=1200')

    # Set page title
    st.title('Spotify Sentiment Analysis')

    st.markdown('''
                
                Spotify is a digital music, podcast, and video service that gives you access to millions of songs and other content from creators all over the world.
                Spotify is available across a range of devices, including computers, phones, tablets, speakers, TVs, and cars, and you can easily transition from one to another with Spotify Connect.
                To enhance the user experience, Spotify can leverage sentiment analysis on listener feedback, such as reviews and comments on various platforms, including the Google Play Store. 

                By looking at what people like or don’t like, Spotify can figure out what’s working and what needs fixing—whether it’s a bug 
                that keeps popping up or a feature that’s getting a lot of praise. All this feedback helps Spotify keep improving, so users get a better, more personal music experience every time they open the app.

                ''')

    st.write('___')

    # EDA
    st.write('## Distribution of Ratings')
    st.write('')

    st.markdown('''
                The distribution of ratings for the Spotify app on the Google Play Store ranges from 1 to 5 stars, 
                showing a mix of user experiences, from highly satisfied users giving 5 stars to those with issues who rate it 1 star.
                ''')

    df = pd.read_csv(r'reviews.csv')


    # Menghitung jumlah rating
    rating_counts = df['Rating'].value_counts().reset_index()
    rating_counts.columns = ['Rating', 'Count']

    # Membuat bar chart
    fig = px.bar(rating_counts, x='Rating', y='Count', 
            title='Distribution of Ratings', 
            labels={'Rating': 'Rating', 'Count': 'Count'},
            color='Rating', 
            color_continuous_scale='Blues')

    st.plotly_chart(fig)

    st.write('___')

    # EDA 2 - World Cloud Negative
    st.write('## Negative Sentiment Wordcloud')
    st.write('')

    # Menghapus baris yang rating-nya bukan 1 atau 5
    df_filtered = df[df['Rating'].isin([1, 5])]
    #data negatif
    data_negatif = df_filtered[df_filtered['Rating']==1]
    #WordCloud data negatif sebelum diolah
    word_sebelum_diolah_negatif = pd.Series(" ".join(data_negatif['Review']).split())
    data_sebelum_diolah_negatif = " ".join(word_sebelum_diolah_negatif)
    wordcloud_neg = WordCloud(width=800, height=400, background_color='black').generate(data_sebelum_diolah_negatif)

    # menampilkan word cloud
    st.image(wordcloud_neg.to_array(), use_container_width=True)

    st.write('___')

    #EDA - Positive
    st.write('## Positive Sentiment Wordcloud')
    st.write('')

    #data positif
    data_positif = df_filtered[df_filtered['Rating']==5]
    word_sebelum_diolah_positif = pd.Series(" ".join(data_positif['Review']).split())
    data_sebelum_diolah_positif = " ".join(word_sebelum_diolah_positif)

    wordcloud_pos = WordCloud(width=800, height=400, background_color='black').generate(data_sebelum_diolah_positif)

    # Display the word cloud
    st.image(wordcloud_pos.to_array(), use_container_width=True)

    st.markdown('<hr style="border: 4px solid #1DB954; width: 100%;" />', unsafe_allow_html=True)


if __name__ == "__main__":
     run()