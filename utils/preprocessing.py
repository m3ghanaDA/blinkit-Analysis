import pandas as pd


def preprocess_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove leading/trailing spaces
    df.columns = df.columns.str.strip()

    # Standardize text values
    object_cols = df.select_dtypes(include="object").columns

    for col in object_cols:
        df[col] = df[col].astype(str).str.strip()

    # Standardize Item Fat Content
    df["Item Fat Content"] = df["Item Fat Content"].replace({
        "LF": "Low Fat",
        "low fat": "Low Fat",
        "reg": "Regular"
    })

    # Missing Outlet Size
    #df["Outlet Size"] = df["Outlet Size"].fillna("Unknown")

    # Missing Item Weight
    if "Item Weight" in df.columns:
        df["Item Weight"] = df["Item Weight"].fillna(df["Item Weight"].median())

    # Item Visibility cannot be zero
    if "Item Visibility" in df.columns:
        median_visibility = df.loc[df["Item Visibility"] > 0, "Item Visibility"].median()
        df["Item Visibility"] = df["Item Visibility"].replace(0, median_visibility)

    return df