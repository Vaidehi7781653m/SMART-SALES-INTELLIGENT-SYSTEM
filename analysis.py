def total_sales(df):
    return df["Sales"].sum()


def average_sales(df):
    return df["Sales"].mean()


def sales_by_product(df):
    return (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def sales_by_region(df):
    return (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def sales_by_category(df):
    return (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def best_selling_product(df):
    product_sales = sales_by_product(df)
    return product_sales.idxmax()


def best_region(df):
    region_sales = sales_by_region(df)
    return region_sales.idxmax()


def best_category(df):
    category_sales = sales_by_category(df)
    return category_sales.idxmax()


def lowest_performing_product(df):
    product_sales = sales_by_product(df)
    return product_sales.idxmin()