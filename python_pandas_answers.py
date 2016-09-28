import pandas as pd

def main():
    # Load the CSV file into a data frame.
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
	df = pd.read_csv("sample_dataset.csv")

    # sum of spend column
    # http: // pandas.pydata.org / pandas - docs / stable / generated / pandas.DataFrame.sum.html
	print df["spend"].sum()

    # standard deviation of pixel 1 column
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.std.html
	print df["pixel_1"].std()

    # count of unique values in the utm column
    # http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.unique.html
	print df["utm"].nunique()

	return None




if __name__ == '__main__':
	main()