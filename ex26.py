# Predict cancellations and dataframe processing
from datetime import datetime, timedelta
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler


class Solution(object):

    def predict_cancellations(self, user_interaction_df):
        assembler = VectorAssembler(
            inputCols=["month_interaction_count", "week_interaction_count", "day_interaction_count"],
            outputCol="features"
        )

        # apply to the dataframe:
        features_df = assembler.transform(user_interaction_df)
        features_df = features_df.withColumn("label", features_df["cancelled_within_week"])

        # create the logistic regression model:
        lr_model = LogisticRegression(maxIter=10, threshold=0.6, elasticNetParam=1, regParam=0.1)

        # train the model against the features and labels:
        trained_lr_model = lr_model.fit(features_df)

        # predict with this model (append predictions to the features dataframe):
        predictions_df = trained_lr_model.transform(features_df)
        predictions_df = predictions_df.select(["user_id", 'rawPrediction', 'probability', 'prediction'])

        return predictions_df

    def get_user_interaction_counts(self, search_interaction_df):
        latest_date_string = search_interaction_df.agg({"date": "max"}).collect()[0][0]    # extract the element that we want with collect(), here (0, 0).
        latest_date = datetime.strptime(latest_date_string, '%Y-%m-%d')

        user_month_counts = self.get_df_counts_from_date_by_user_id(search_interaction_df, latest_date, 30)
        user_week_counts = self.get_df_counts_from_date_by_user_id(search_interaction_df, latest_date, 7)
        user_day_counts = self.get_user_interaction_counts(search_interaction_df, latest_date, 1)

        user_month_counts = user_month_counts.withColumnRenamed("count", "month_interaction_count")
        user_week_counts = user_week_counts.withColumnRenamed("count", "week_interaction_count")
        user_day_counts = user_day_counts.withColumnRenamed("count", "day_interaction_count")

        # we have 3 distinct separated dataframe but we want one general dataframe (it is like a left joint in SQL):
        user_interaction_counts = user_month_counts.join(user_week_counts, ["user_id"], "left")
        user_interaction_counts = user_interaction_counts.join(user_day_counts, ["user_id"], "left")
        user_interaction_counts = user_interaction_counts.na.fill(0)

        # here user_interaction_counts dataframe could be used for some machine learning models:
        return user_interaction_counts

    def get_df_counts_from_date_by_user_id(self, df, end_date, days_delta):
        start_date = end_date - timedelta(days = days_delta)

        return df.where(df['date'].between(start_date, end_date)).groupBy("user_id").count()
