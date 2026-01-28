import polars as pl
import datetime as dt

df = pl.read_csv("dta/rnd_cities.csv")

print(df.head(12))
df.write_csv('cotw.csv')

#  48060 dta/worldcities.csv
#  151540 final_proj_dcda/__wq_20251105_1420/Dashboards/python/Dta/exporte/world_cities.csv