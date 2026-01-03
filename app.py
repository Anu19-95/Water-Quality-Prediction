import pandas as pd
import joblib
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- Load model & dataset --------------------
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

df = pd.read_csv("PB_All_2000_2021_named.csv", sep=";")

# Parse date + year
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['year'] = df['date'].dt.year

pollutants = ['O2','NO3','NO2','SO4','PO4','CL']

# Lookup tables
id_to_name = dict(zip(df['id'], df['site_name']))
name_to_id = dict(zip(df['site_name'], df['id']))

# -------------------- UI Title --------------------
st.title("Water Quality — Lake & River Pollution Predictor")

st.write("Search by **Lake / River Name** to view and predict pollutant levels.")

# -------------------- Search Box --------------------
search_text = st.text_input("Search Lake / River", "")

if search_text.strip():
    results = [n for n in df['site_name'].unique()
               if search_text.lower() in n.lower()]
else:
    results = sorted(df['site_name'].unique())

selected_site = st.selectbox("Select Monitoring Location", results)

station_id = name_to_id.get(selected_site, None)

st.write(f"**Selected Station:** {selected_site}")
st.write(f"**Station ID:** {station_id}")

# -------------------- Prediction --------------------
st.subheader("Pollutant Level Prediction")

year_input = st.number_input(
    "Enter Year for Prediction",
    min_value=2000,
    max_value=2100,
    value=2025
)

if st.button("Predict"):
    if station_id is None:
        st.error("Station ID missing — cannot predict.")
    else:
        input_df = pd.DataFrame({
            'year':[year_input],
            'id':[station_id]
        })

        # One-hot encode to match model
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0

        input_encoded = input_encoded[model_cols]

        predicted = model.predict(input_encoded)[0]

        st.subheader(f"Predicted pollutant levels for\n**{selected_site}** in **{year_input}**")

        pred_df = pd.DataFrame({
            "Pollutant": pollutants,
            "Value": predicted
        })

        st.dataframe(pred_df)

        # Bar Chart
        fig, ax = plt.subplots()
        sns.barplot(x="Pollutant", y="Value", data=pred_df, ax=ax)
        ax.set_ylabel("Concentration")
        st.pyplot(fig)

# -------------------- Statistics Panel --------------------
st.sidebar.header("Basic Statistics")

param = st.sidebar.selectbox("Choose Parameter", pollutants)

if param:
    sub_df = df[df['site_name'] == selected_site]

    st.sidebar.write("Mean:", round(sub_df[param].mean(),2))
    st.sidebar.write("Median:", round(sub_df[param].median(),2))
    st.sidebar.write("Std Dev:", round(sub_df[param].std(),2))
    st.sidebar.write("Min:", sub_df[param].min())
    st.sidebar.write("Max:", sub_df[param].max())

# -------------------- Visualizations --------------------
st.sidebar.header("Visualizations")

option = st.sidebar.selectbox(
    "Choose Chart",
    ["Histogram","Boxplot","Line Chart","Scatter Plot","Pie Chart"]
)

site_df = df[df['site_name'] == selected_site]

if option == "Histogram":
    fig, ax = plt.subplots()
    site_df[param].hist(bins=30, color="skyblue", ax=ax)
    ax.set_title(f"Histogram of {param} — {selected_site}")
    st.pyplot(fig)

elif option == "Boxplot":
    fig, ax = plt.subplots()
    sns.boxplot(x=site_df[param], ax=ax)
    ax.set_title(f"Boxplot of {param} — {selected_site}")
    st.pyplot(fig)

elif option == "Line Chart":
    fig, ax = plt.subplots()
    site_df.groupby("year")[param].mean().plot(ax=ax)
    ax.set_title(f"{param} Trend Over Years — {selected_site}")
    st.pyplot(fig)

elif option == "Scatter Plot":
    other_param = st.sidebar.selectbox(
        "Compare with",
        [p for p in pollutants if p != param]
    )
    fig, ax = plt.subplots()
    ax.scatter(site_df[param], site_df[other_param], alpha=0.5)
    ax.set_xlabel(param)
    ax.set_ylabel(other_param)
    ax.set_title(f"{param} vs {other_param} — {selected_site}")
    st.pyplot(fig)

elif option == "Pie Chart":
    fig, ax = plt.subplots()
    df_group = site_df.groupby("year")[param].mean().head(5)
    ax.pie(df_group, labels=df_group.index, autopct="%.1f%%", startangle=90)
    ax.set_title(f"{param} Share (First 5 Years) — {selected_site}")
    st.pyplot(fig)