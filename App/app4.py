import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import datetime

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")
st.title("🌍 Air Quality Dashboard")
st.markdown("## 📍 Geospatial Temporal Data Analysis")


# =========================
# Load Static Dataset
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("air_quality_india.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()


# =========================
# Sidebar Filters
# =========================
cities = df["city"].unique().tolist()
selected_city = st.sidebar.selectbox("Select City", cities)

pollutants = [col for col in df.columns if col not in ["date", "city", "latitude", "longitude"]]
selected_pollutant = st.sidebar.selectbox("Select Pollutant", pollutants)

today = df["date"].max().date()
default_start = today - datetime.timedelta(days=30)
start_date = st.sidebar.date_input("Start Date", default_start)
end_date = st.sidebar.date_input("End Date", today)

if start_date >= end_date:
    st.error("End date must be after start date.")
    st.stop()

# =========================
# Filter Data
# =========================
mask = (
    (df["city"] == selected_city) &
    (df["date"].dt.date >= start_date) &
    (df["date"].dt.date <= end_date)
)
filtered_df = df.loc[mask].copy()  #loc: it allows to simulatneously choose both row and column.

if filtered_df.empty:
    st.warning(f"No {selected_pollutant} data found for {selected_city} in selected date range.")
    st.stop()

# =========================
# Time Series Plot
# =========================
st.subheader(f"📈 {selected_pollutant} Levels Over Time – {selected_city}")

fig_line = px.line(
    filtered_df,
    x="date",
    y=selected_pollutant,
    title=f"{selected_pollutant} Trend",
    markers=True
)
st.plotly_chart(fig_line, use_container_width=True)

# =========================
# Map Plot
# =========================
st.subheader("🗺️ Geospatial Distribution of Measurements")

fig_map = px.scatter_mapbox(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color=selected_pollutant,
    size=selected_pollutant,
    color_continuous_scale="OrRd",
    mapbox_style="open-street-map",
    zoom=8,
    height=400
)
st.plotly_chart(fig_map, use_container_width=True)

# =========================
# Forecast
# =========================
st.subheader("🤖 Forecasting with Linear Regression")

filtered_df["timestamp"] = filtered_df["date"].astype('int64') // 10**9
X = filtered_df[["timestamp"]]
y = filtered_df[selected_pollutant]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
# rmse = mean_squared_error(y_test, y_pred, squared=False)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
st.markdown(f"**RMSE**: `{rmse:.2f}` units") # RMSE: How far are our predictions from the real values, on average.

# Forecast future days
future_days = st.slider("Forecast Days", 1, 7, 3)
last_ts = filtered_df["timestamp"].max()
future_timestamps = [last_ts + 86400 * i for i in range(1, future_days + 1)]
future_df = pd.DataFrame({"timestamp": future_timestamps})
future_df[f"Predicted_{selected_pollutant}"] = model.predict(future_df[["timestamp"]])
future_df["Date"] = pd.to_datetime(future_df["timestamp"], unit="s")

st.dataframe(future_df[["Date", f"Predicted_{selected_pollutant}"]])

fig_forecast = px.line(
    future_df,
    x="Date",
    y=f"Predicted_{selected_pollutant}",
    title=f"Forecasted {selected_pollutant} Levels"
)
st.plotly_chart(fig_forecast, use_container_width=True)

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Static Air Quality Dataset | Project by **Sanchit G. Barne**")
