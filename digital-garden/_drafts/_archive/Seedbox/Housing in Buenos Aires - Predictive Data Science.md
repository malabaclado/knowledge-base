---
tags:
alias:
creation-date: Saturday 17th June 2023
---

In this project, you're working for a client who wants to create a model that can predict the price of apartments in the city of Buenos Aires — with a focus on apartments that cost less than $400,000 USD.

[[Subsetting data in pandas using masks]]


# Data preparation

## Import

**Subsetting data**
This allows you to apply multiple filters on the dataframe. For example:
```python
## Subset properties in "Capital Federal"
mask_cpt=df['place_with_parent_names'].str.contains('Capital Federal')

## Subset to "apartments"
mask_apt=df['property_type'] == 'apartment'

## Subset to properties where "price_approx_usd" <400000
mask_cost=df['price_aprox_usd'] <400000

## Applying the masks:
df[mask_cpt & mask_apt & mask_cost]
```

## Explore
## Split

# Build Model
## Baseline
## Iterate
## Evaluate




---
See also: [[WorldQuant - Applied Data Science Lab]]