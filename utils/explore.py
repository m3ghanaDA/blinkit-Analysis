def show_unique_values(df):

    for col in df.select_dtypes(include="object"):

        print("="*50)
        print(col)
        print(df[col].unique())