import pandas as pd

def clean_data(df):
    
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows where important values are missing
    df = df.dropna(subset=["Product", "Region", "Sales"])

    # Make sure Sales is numeric
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

    # Remove rows where Sales could not be converted
    df = df.dropna(subset=["Sales"])

    return df