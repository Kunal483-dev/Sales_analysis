# Sales Data Analysis with Pandas

A beginner-friendly Pandas project that analyzes sample sales data and creates charts.

## Files

- `sales_data.csv` — sample sales dataset
- `sales_analysis.ipynb` — analysis notebook and charts

## Run

1. Install the required packages:
   ```bash
   pip install pandas matplotlib jupyter
   ```
2. Keep the CSV and notebook in the same folder.
3. Start Jupyter and open the notebook:
   ```bash
   jupyter notebook
   ```
4. Run all cells.

## What it shows

- Total sales revenue
- Best-performing region and product
- Sales by region and product charts

## Core idea

```python
df['Sales'] = df['Units'] * df['Unit_Price']
df.groupby('Region')['Sales'].sum().plot(kind='bar')
```
