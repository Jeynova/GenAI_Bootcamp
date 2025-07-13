import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Mini EDA + LLM", layout="wide")

st.title("EDA + LLM")
st.write("Charge un CSV, explore les données, et pose des questions au LLM.")

# Upload
uploaded_file = st.file_uploader("Charge un fichier CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Fichier chargé avec succès !")
    st.write(df.head())

    # Colonnes numériques
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    if not num_cols:
        st.warning("Pas de colonnes numériques détectées.")
        st.stop()

    # Statistiques de base
    st.subheader("Statistiques descriptives")
    st.write(df.describe())

    # Corrélation
    st.subheader("Matrice de corrélation")
    corr = df[num_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Distribution
    st.subheader("Distribution d'une variable")
    var = st.selectbox("Choisis une variable", num_cols)
    fig2, ax2 = plt.subplots()
    sns.histplot(df[var], kde=True, ax=ax2)
    st.pyplot(fig2)

    # Outliers
    st.subheader("Outliers")
    fig3, ax3 = plt.subplots()
    sns.boxplot(data=df[num_cols], orient="h", ax=ax3)
    st.pyplot(fig3)

    # PCA + KMeans
    st.subheader("PCA + Clustering")
    try:
        scaler = StandardScaler()
        scaled = scaler.fit_transform(df[num_cols])
        pca = PCA(n_components=2)
        reduced = pca.fit_transform(scaled)

        k = st.slider("Nombre de clusters", 2, 10, 3)
        kmeans = KMeans(n_clusters=k, random_state=0)
        labels = kmeans.fit_predict(reduced)

        cluster_df = pd.DataFrame(reduced, columns=["PC1", "PC2"])
        cluster_df["Cluster"] = labels

        fig4, ax4 = plt.subplots()
        sns.scatterplot(data=cluster_df, x="PC1", y="PC2", hue="Cluster", palette="Set2", ax=ax4)
        st.pyplot(fig4)
    except Exception as e:
        st.error(f"Erreur clustering : {e}")

    # LLM Local
    st.subheader("Assistant IA")

    question = st.text_area("Pose une question sur les données")
    if st.button("Interroger le LLM"):
        try:
            prompt = f"""Tu es un expert en analyse de données. Réponds en français à cette question sur ce jeu de données :
Données :
{df.head(10).to_csv(index=False)}
Question :
{question}
"""

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama3", "prompt": prompt, "stream": False},
                timeout=60
            )
            if response.status_code == 200:
                result = response.json()
                st.markdown("**Réponse du LLM :**")
                st.write(result.get("response", "Pas de réponse."))
            else:
                st.error(f"Erreur LLM : {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Erreur de connexion à Ollama : {e}")
else:
    st.info("Charge un fichier CSV pour commencer.")
