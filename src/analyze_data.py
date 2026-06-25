import numpy as np


def generate_summary(df):
    """
    Generate summary statistics
    for the EV dataset.
    """

    print("\n" + "=" * 40)
    print("EV DATASET SUMMARY")
    print("=" * 40)

    print(f"Total Records        : {df.shape[0]}")
    print(f"Total Columns        : {df.shape[1]}")

    print(
        f"Average EV Range     : "
        f"{np.mean(df['Electric Range']):.2f} miles"
    )

    print(
        f"Median EV Range      : "
        f"{np.median(df['Electric Range']):.2f} miles"
    )

    print(
        f"Maximum EV Range     : "
        f"{np.max(df['Electric Range']):.2f} miles"
    )

    print(
        f"Minimum EV Range     : "
        f"{np.min(df['Electric Range']):.2f} miles"
    )

    print("\nTop 10 Vehicle Manufacturers")
    print("-" * 40)

    print(
        df["Make"]
        .value_counts()
        .head(10)
    )

    print("\nTop 5 Countries by EV Adoption")
    print("-" * 40)

    print(
    df["Country"]
    .value_counts()
    .head(5)
    )
    print("=" * 40)