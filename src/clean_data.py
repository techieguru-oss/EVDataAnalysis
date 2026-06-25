def clean_dataset(df):

    print("Cleaning dataset...")

    duplicates_before = df.duplicated().sum()

    df['Electric Range'] = df['Electric Range'].fillna(
        df['Electric Range'].median()
    )

    df['Base MSRP'] = df['Base MSRP'].fillna(
        df['Base MSRP'].median()
    )

    df['Legislative District'] = (
        df['Legislative District']
        .fillna("Unknown")
        .astype(str)
    )

    df.drop_duplicates(inplace=True)

    if duplicates_before == 0:
        print("No duplicate rows found.")
    else:
        print(f"Duplicates removed: {duplicates_before}")

    return df