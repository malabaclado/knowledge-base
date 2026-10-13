---
tags:
alias:
creation-date: Saturday 17th June 2023
---

```python
import plotly.express as px
fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat=df['lat'],
    lon=df['lon'],
    center={"lat": 19.43, "lon": -99.13},  # Map will be centered on Mexico City
    width=600,  # Width of map
    height=600,  # Height of map
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)

fig.update_layout(mapbox_style="open-street-map")

fig.show()
```