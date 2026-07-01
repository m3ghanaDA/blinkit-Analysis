def calculate_metrics(df):

    metrics = {

        "total_sales": df["Sales"].sum(),

        "avg_sales": df["Sales"].mean(),

        "items": len(df),

        "rating": df["Rating"].mean()

    }

    return metrics