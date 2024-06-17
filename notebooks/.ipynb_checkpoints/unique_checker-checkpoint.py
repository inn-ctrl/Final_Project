#for easy viewing of string columns, we unify the values in the function
def get_unique_values(df, columns): 
    for column in columns: 
        unique_values = df[column].unique()
        print(f'unique {column}', unique_values)
