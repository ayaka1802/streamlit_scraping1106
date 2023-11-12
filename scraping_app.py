
import requests
import pandas as pd
from google.oauth2.service_account import Credentials
import datetime
from gspread_dataframe import set_with_dataframe
import altair as alt


data = worksheet.get_all_values()
df_udemy = pd.DataFrame(data[1:], columns=data[0])
df_udemy = df_udemy.astype({
    'n_subscriber': int,
    'n_review': int    
})
ymin1 = df_udemy['n_subscriber'].min() - 10
ymax1 = df_udemy['n_subscriber'].max() + 10

ymin2 = df_udemy['n_review'].min() - 10
ymax2 = df_udemy['n_review'].max() + 10

base = alt.Chart(df_udemy).encode(
    alt.X('date:T', axis=alt.Axis(title=None))
)

line1 = base.mark_line(opacity=0.3, color='#57A44C').encode(
    alt.Y('n_subscriber',
          axis=alt.Axis(title='受講生数', titleColor='#57A44C'),
          scale=alt.Scale(domain=[ymin1, ymax1])
         )
)

line2 = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
    alt.Y('n_review',
          axis=alt.Axis(title='レビュー数', titleColor='#5276A7'),
          scale=alt.Scale(domain=[ymin2, ymax2])
         )
)

chart = alt.layer(line1, line2).resolve_scale(
    y = 'independent'
)