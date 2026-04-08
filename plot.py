import matplotlib.pyplot as plt

def plot_region_sales(df):
    region_sales = df.groupby("Region")["Sales_Amount"].sum()

    region_sales.plot(kind="bar")

    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)

    plt.show()


def plot_category_profit(df):
    category_profit = df.groupby("Product_Category")["Profit"].sum()

    category_profit.plot(kind="bar")

    plt.title("Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")
    plt.xticks(rotation=45)

    plt.show()


def plot_sales_trend(df):
    sales_trend = df.groupby("Sale_Date")["Sales_Amount"].sum()

    sales_trend.plot(kind="line")

    plt.title("Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.xticks(rotation=45)
    plt.show()