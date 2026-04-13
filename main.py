from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

def main():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL pipeline executed successfully")

if __name__ == "__main__":
    main()
