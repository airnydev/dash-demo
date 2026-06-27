from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path(__file__).parent / "data" / "sample_kpi_data.csv"
st.set_page_config(page_title="Revenue dashboard", layout="wide")

@st.cache_data(show_spinner="Loading 50k rows...")
def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH, parse_dates=["order_date"])

def main() -> None:
    df = load_data()
    
    with st.sidebar:
        st.title("Revenue dashboard")
        min_date = df["order_date"].min().date()
        max_date = df["order_date"].max().date()
        date_range = st.date_input(
            "Date range",
            value = (min_date , max_date),
            min_value = min_date,
            max_value = max_date,
        )

        regions = st.multiselect(
            "Regions",
            options=sorted(df["region"].unique()),
            default=sorted(df["region"].unique()),
        )
        
        products = st.multiselect(
            "Products",
            options=sorted(df["product"].unique()),
            default=sorted(df["product"].unique()),
        )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start, end = date_range
        mask = (
            (df["order_date"].dt.date >= start)
            & (df["order_date"].dt.date <= end)
            & (df["region"].isin(regions))
            & (df["product"].isin(products))
        )
        filtered = df.loc[mask]
    else:
        filtered = df

    if filtered.empty:
        st.warning("No data matches the current filters.")
        return

    # kpi_cards(filtered)
    # st.divider()

    # left, right = st.columns(2)
    # with left:
    #     revenue_over_time(filtered)
    # with right:
    #     revenue_by_region(filtered)

    # st.divider()
    # top_customers(filtered)

    # start, end = date_range
    # f = df[(df["order_date"].dt.date >= start) & (df["order_date"].dt.date <