# Fix for "Data must be 1-dimensional, got ndarray of shape (5, 1)" Error

## Problem
The error occurs in this line:
```python
sns.lineplot(x=df['order_year'], y=df.groupby(['order_year'])[['sales']].sum())
```

The issue is that:
- `df['order_year']` returns a 1D Series with all original rows (matching entire df length)
- `df.groupby(['order_year'])[['sales']].sum()` returns a 2D DataFrame with shape (5, 1)
  - These have mismatched lengths and dimensions
  - seaborn expects 1D data

## Solution
Use the already-calculated `vendas_ano` variable which is a properly aggregated DataFrame, then extract the 1D Series from it:

```python
plt.figure(figsize=(10,6))
sns.lineplot(x=vendas_ano.index, y=vendas_ano['sales'])
```

This works because:
- `vendas_ano.index` provides the x-axis values (order_year: 2015-2019) - 1D
- `vendas_ano['sales']` extracts just the sales column as a 1D Series - shape (5,)
- Both are aligned and properly 1D for seaborn to process

## Verification
```python
vendas_ano['sales'].shape  # (5,) - proper 1D series
vendas_ano.shape           # (5, 1) - 2D dataframe (this is what was being passed before)
```
