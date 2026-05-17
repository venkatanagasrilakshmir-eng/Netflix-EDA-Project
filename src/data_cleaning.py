import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def clean_data(df):

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    df['director'].fillna('Unknown', inplace=True)
    df['cast'].fillna('Unknown', inplace=True)
    df['country'].fillna('Unknown', inplace=True)
    df['rating'].fillna('Not Rated', inplace=True)

    # Convert date_added to datetime
    df['date_added'] = pd.to_datetime(df['date_added'])

    return df


if __name__ == "__main__":
    df = load_data("../data/netflix_titles.csv")
    df = clean_data(df)

    print(df.head())
    print("\nData Cleaned Successfully")
