import matplotlib.pyplot as plt
import seaborn as sns

#Histogram of Electric Range
def plot_electric_range(df):

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df['Electric Range'],
        bins=30,
        kde=True
    )

    plt.title("Distribution of Electric Range")
    plt.xlabel("Electric Range (Miles)")
    plt.ylabel("Number of Vehicles")

    plt.tight_layout()

    plt.savefig(
        "outputs/electric_range_histogram.png",
        bbox_inches="tight"
    )

    plt.close()

#Make Distribution Bar Plot
def plot_make_distribution(df):

    plt.figure(figsize=(10, 8))

    top_makes = (
    df["Make"]
    .value_counts()
    .head(15)
    .index
    )

    sns.countplot(
    data=df,
    y="Make",
    order=top_makes
   )

    plt.title("Number of Vehicles by Make")

    plt.tight_layout()

    plt.savefig(
        "outputs/vehicle_make_distribution.png",
        bbox_inches="tight"
    )

    plt.close()

#Scatter Plot of Electric Range vs Base MSRP
def plot_range_vs_msrp(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
    x='Electric Range',
    y='Base MSRP',
    data=df.sample(5000),
    alpha=0.5
   )

    plt.title("Electric Range vs Base MSRP")

    plt.tight_layout()
    
    plt.savefig(
        "outputs/range_vs_msrp.png",
        bbox_inches="tight"
    )

    plt.close()

#Correlation Heatmap of Numeric Features
def plot_heatmap(df):

    corr_matrix = (
        df.select_dtypes(
            include='number'
        )
        .corr()
    )

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="viridis",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")

    plt.tight_layout()
    
    plt.savefig(
        "outputs/correlation_heatmap.png",
        bbox_inches="tight"
    )

    plt.close()

def plot_top_countries(df):

    plt.figure(figsize=(10,6))

    (
        df["Country"]
        .value_counts()
        .head(10)
        .plot(kind="bar")
    )

    plt.title("Top 10 Countries by EV Adoption")
    plt.xlabel("Country")
    plt.ylabel("Number of EVs")

    plt.tight_layout()

    plt.savefig(
        "outputs/top_countries.png",
        bbox_inches="tight"
    )

    plt.close()