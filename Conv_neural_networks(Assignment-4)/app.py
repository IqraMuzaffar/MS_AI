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

# Custom Styling for UI
st.markdown(
    """
    <style>
    .big-font { font-size:30px !important; font-weight: bold; color: #333366;}
    .small-font { font-size:15px !important; color: #555;}
    .uploaded-img { border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2);}
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Streamlit app
def main():
    # Load the pre-trained model and feature data
    model = load_model()
    feature_data = load_features()

    # Page Title
    st.markdown('<p class="big-font">🔍 Image Similarity Finder for Accessories</p>', unsafe_allow_html=True)
    st.write("Upload an image of **accessories** such as perfumes, clothes, watches, etc., and find similar images.")

    # Sidebar Instructions
    st.sidebar.header("📌 Instructions")
    st.sidebar.info("1. Upload an image of an accessory (e.g., **perfume, clothing, shoes, watch**). \n"
                    "2. Click **Find Similar Images** button. \n"
                    "3. View the most similar images below.")

    # Upload image
    uploaded_image = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        # Display the uploaded image
        st.image(uploaded_image, caption="📷 Uploaded Image", use_column_width=True, output_format="auto")

        # Perform image similarity search
        if st.button("🔎 Find Similar Images", use_container_width=True):
            with st.spinner("🔄 Searching for similar images..."):
                # Preprocess and extract features from the uploaded image
                image_array = preprocess_image(uploaded_image)
                query_features = extract_features(image_array, model)

                # Find the top 5 similar images
                similar_images = find_similar_images(query_features, feature_data, top_n=5)

            # Display the results in a grid layout
            st.markdown("<p class='big-font'>🖼️ Similar Images</p>", unsafe_allow_html=True)

            # Create two columns for better layout
            col1, col2 = st.columns(2)
            for idx, (_, row) in enumerate(similar_images.iterrows()):
                if idx % 2 == 0:
                    with col1:
                        st.image(row["image_url"], caption=f"🔹 Similarity: {row['similarity']:.2f}", use_column_width=True)
                else:
                    with col2:
                        st.image(row["image_url"], caption=f"🔹 Similarity: {row['similarity']:.2f}", use_column_width=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
