#import libraries
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import tensorflow_hub as hub
from tensorflow_hub import KerasLayer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

#import KerasLayer from TensorFlow Hub
# KerasLayer = hub.KerasLayer

#stopwords
stop_words_en = stopwords.words("english")
new_stop_words = ["didnt", 'wont', 'doesnt', 'dear', 'ive', 'really', 'youre', 'couldnt', 'cant']
stop_words_en = stop_words_en + new_stop_words
stop_words_en = list(set(stop_words_en))

#lemmatizer
lemmatizer = WordNetLemmatizer()

# Text preprocessing function
def text_preprocessing(text):
    # Case folding
    text = text.lower()

    # Non-letter removal (such as emoticons, symbols, etc)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Stopwords removal
    tokens = [word for word in tokens if word not in stop_words_en]

    # Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Combining Tokens
    text = ' '.join(tokens)

    return text

def run():

    nltk.download('stopwords')
    nltk.download('punkt_tab')
    nltk.download('wordnet')
    #import KerasLayer from TensorFlow Hub
    #KerasLayer = hub.KerasLayer
    # Load the trained model
    model = load_model('sentiment_lstm_model.h5', custom_objects={'KerasLayer': KerasLayer})

    
    st.title('Predict your sentiment analysis')
    st.write('___')

    #streamlit
    with st.form('Fill In Form'):
        st.write('Insert your review')
        review = st.text_input(label="Review Box",
                            help="Enter the review you wish to predict",
                            placeholder="Ex: amazing app!/too many ads")

        submit = st.form_submit_button('Submit')

        if submit:
            #menyiapkan review sebelum dipredict
            preprocessed_review = text_preprocessing(review)

            #mengubah review yang telah diproses menjadi tensor kemudian input ke model
            text_input = [preprocessed_review]
            text_tensor = tf.convert_to_tensor(text_input, dtype=tf.string)

            #membuat preediksi
            prediction = model.predict(text_tensor)
            result = prediction[0][0]  # Assuming the model outputs probability of positive sentiment

            #mnentukan sentimen berdasarkan probabilitas
            if result > 0.5:
                print_result = "Positive sentiment review"
            else:
                print_result = "Negative sentiment review"

            st.write(print_result)


if __name__ == "__main__":
     run()