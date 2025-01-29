# Import necessary libraries
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained VGG16 model
@st.cache_resource
def load_model():
    model = VGG16(weights="imagenet", include_top=False, pooling="avg")
    return model

# Preprocess the uploaded image
def preprocess_image(uploaded_image):
    img = Image.open(uploaded_image).resize((224, 224))  # Resize for VGG16 input
    img_array = img_to_array(img)  # Convert to array
    img_array = img_array.reshape((1, 224, 224, 3))  # Add batch dimension
    img_array = preprocess_input(img_array)  # Normalize pixel values
    return img_array

# Extract features from the image
def extract_features(image_array, model):
    features = model.predict(image_array).flatten()
    return features

# Load the precomputed features from the CSV
@st.cache_data
def load_features():
    df = pd.read_csv("image_features.csv")
    df["features"] = df["features"].apply(eval)  # Convert string to list
    return df

# Calculate cosine similarity
def find_similar_images(query_features, feature_data, top_n=5):
    features_array = np.array(feature_data["features"].tolist())
    similarities = cosine_similarity([query_features], features_array)[0]
    feature_data["similarity"] = similarities
    return feature_data.sort_values(by="similarity", ascending=False).head(top_n)

# Main Streamlit app
def main():
    # Load the pre-trained model and feature data
    model = load_model()
    feature_data = load_features()

    st.title("Image Similarity Finder")

    # Sidebar instructions
    st.sidebar.header("Instructions")
    st.sidebar.markdown("1. Upload an image.\n2. Click 'Find Similar Images' button.\n3. View results below.")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Perform image similarity search
        if st.button("Find Similar Images"):
            st.write("Searching for similar images...")
            # Preprocess and extract features from the uploaded image
            image_array = preprocess_image(uploaded_image)
            query_features = extract_features(image_array, model)

            # Find the top 5 similar images
            similar_images = find_similar_images(query_features, feature_data, top_n=5)

            # Display the results
            st.write("### Similar Images:")
            for _, row in similar_images.iterrows():
                st.image(row["image_url"], caption=f"Similarity: {row['similarity']:.2f}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
