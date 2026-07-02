import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

mostViews = ad_clicks.groupby(["utm_source"])\
          ["user_id"].count().reset_index()
print(mostViews)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

clicks_by_source = ad_clicks.groupby(["utm_source","is_click"]).user_id.count().reset_index()
print(clicks_by_source)


clicks_pivot = clicks_by_source.pivot(columns ="is_click",\
                                      index = "utm_source",\
                                      values = "user_id").reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])*100
print(clicks_pivot)


AandB = ad_clicks.groupby(["experimental_group"])\
          ["user_id"].count().reset_index()
print(AandB)


trueAandB = ad_clicks.groupby(["is_click","experimental_group"])\
          ["user_id"].count().reset_index()
print(trueAandB)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()

percentageA = a_clicks.groupby(["is_click","day"])\
          ["user_id"].count().reset_index()
pivotPercentA = percentageA.pivot(columns ="is_click",\
                                      index = "day",\
                                      values = "user_id").reset_index()
pivotPercentA['percent_clickedA'] = pivotPercentA[True]/(pivotPercentA[True]+pivotPercentA[False])*100
print(pivotPercentA)

percentageB = b_clicks.groupby(["is_click","day"])\
          ["user_id"].count().reset_index()
pivotPercentB = percentageB.pivot(columns ="is_click",\
                                      index = "day",\
                                      values = "user_id").reset_index()
pivotPercentB['percent_clickedB'] = pivotPercentB[True]/(pivotPercentB[True]+pivotPercentB[False])*100
print(pivotPercentB)




