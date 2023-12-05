import streamlit as st
import pyspark

def main():
   st.title('Sales Information')
   st.markdown('Chose the tab to view the information')
   # nút chọn xem toàn bộ data
   if st.sidebar.button('View all data'):
      st.subheader('All data')
      S3_ENDPOINT = "http://192.168.227.128:9000/"
      AWS_BUCKET_NAME = "salesdata"
      # This cell may take some time to run the first time, as it must download the necessary spark jars
      conf = pyspark.SparkConf().setMaster("local")
      conf.set("spark.jars.packages", 'org.apache.hadoop:hadoop-aws:3.3.1,io.delta:delta-spark_2.12:3.0.0')\
         .set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")\
         .set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")\
         .set("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")\
         .set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")\
         .set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')\
         .set('spark.hadoop.fs.s3a.endpoint', S3_ENDPOINT)\
         .set('spark.hadoop.fs.s3a.access.key', "minioadmin")\
         .set('spark.hadoop.fs.s3a.secret.key', "minioadmin")\
         .set('spark.hadoop.fs.s3a.path.style.access', "true")\
            #.set("spark.jars.packages","io.delta:delta-sharing-spark_2.12:0.6.4")\
      sc = pyspark.SparkContext(conf=conf)
      spark = pyspark.sql.SparkSession(sc)
      df_order=spark.read.format("delta").option("header","true").load("s3a://salesdata/gold/TotalPay_By_Order")
      df_user=spark.read.format("delta").option("header","true").load("s3a://salesdata/gold/TotalPay_By_User")
      df_item=spark.read.format("delta").option("header","true").load("s3a://salesdata/gold/TotalSold_and_TotalAmount_By_Item")
      st.markdown('## Table : TotalPay_By_Order')
      st.dataframe(df_order)
      st.markdown('## Table : TotalPay_By_User')
      st.dataframe(df_user)
      st.markdown('## Table : TotalSold_and_TotalAmount_By_Item')
      st.dataframe(df_item)
      
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass