import streamlit as st
import pandas as pd
from search import load_data, search_articles

# Page settings
st.set_page_config(
    page_title="WikiInfo",
    page_icon="🌍",
    layout="wide"
)

# Title
st.title("🌍 WikiInfo")
st.subheader("Explore Wikipedia using structured Wikimedia data")

st.divider()


# Load dataset
@st.cache_data
def get_data():
    return load_data()


df = get_data()


# Search box
query = st.text_input(
    "🔎 Search for a Wikipedia article",
    placeholder="Try: Cataract, India, River..."
)


# Search button
if st.button("Search", type="primary"):

    if not query.strip():
        st.warning("Please enter something to search.")

    else:
        results = search_articles(df, query, limit=10)

        if results.empty:
            st.error("No articles found.")

        else:
            st.success(f"Found {len(results)} result(s)")

            for _, article in results.iterrows():

                st.markdown(f"## 📖 {article['name']}")

                # Description
                description = article["description"]

                if pd.notna(description):
                    st.write(description)

                # Abstract
                abstract = article["abstract"]

                if pd.notna(abstract) and str(abstract).strip():
                    st.markdown("### 📝 Summary")
                    st.write(abstract)

                # Image
                image = article["image"]

                if pd.notna(image) and str(image).strip():
                    try:
                        st.image(image, width=300)
                    except:
                        pass

                # Wikipedia link
                url = article["url"]

                if pd.notna(url) and str(url).strip():
                    st.markdown(
                        f"🔗 [Open Wikipedia article]({url})"
                    )

                st.divider()