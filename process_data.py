import pandas as pd
import glob
import os

def main():
    print("Starting data processing...")
    # Define the path to the data
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'data')
    output_file = os.path.join(base_dir, 'formatted_output.csv')

    # Find all CSV files in the data directory
    all_files = glob.glob(os.path.join(data_dir, "*.csv"))
    if not all_files:
        print(f"No CSV files found in {data_dir}")
        return

    print(f"Found {len(all_files)} CSV files to process.")

    df_list = []
    for file in all_files:
        df = pd.read_csv(file)
        df_list.append(df)

    # Combine all datasets
    df_combined = pd.concat(df_list, ignore_index=True)

    print("Filtering and transforming data...")
    # 1. Filter product to 'pink morsel' (case insensitive to be safe, though the raw data is lowercase)
    df_combined = df_combined[df_combined['product'].str.lower() == 'pink morsel']

    # 2. Clean 'price' column (remove '$' and convert to float)
    df_combined['price'] = df_combined['price'].str.replace('$', '', regex=False).astype(float)

    # 3. Calculate 'sales'
    df_combined['sales'] = df_combined['price'] * df_combined['quantity']

    # 4. Select required fields: Sales, Date, Region
    # The requirement specifically mentions Title case (Sales, Date, Region) or just those 3 specific fields.
    final_df = df_combined[['sales', 'date', 'region']].copy()
    final_df.columns = ['Sales', 'Date', 'Region']

    # Write to output file
    final_df.to_csv(output_file, index=False)

    print(f"Data processing complete. output saved to {output_file}")

if __name__ == "__main__":
    main()
