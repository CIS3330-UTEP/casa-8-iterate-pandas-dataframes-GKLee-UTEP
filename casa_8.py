import pandas as pd
file = './big-mac-full-index.csv'
df = pd.read_csv(file)

# define a function to apply:
def print_row(row):
    print('')
print(df)

print("Iterrating using irerrows")
for index, row in df.iterrows():
    print(f'Index: {index}, Date: {row['date']}, Country: {row['name']}, Local Price: {row['local_price']}')

def adjusted_price(row):
    conversion_rate = 1.2
    return row['local_price'] * conversion_rate

df['adjusted_price'] = df.apply(adjusted_price, axis=1)

print("\nDataFrame after Apply():")
print(df[['name', 'local_price', 'adjusted_price']])