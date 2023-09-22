from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.getOrCreate()

df_category = spark.createDataFrame([
    Row(id_category=1, name_category='category_1'),
    Row(id_category=2, name_category='category_2'),
    Row(id_category=3, name_category='category_3')
])

df_product = spark.createDataFrame([
    Row(id_category=1, id_product=1, name_product='product_1'),
    Row(id_category=2, id_product=1, name_product='product_1'),
    Row(id_category=2, id_product=2, name_product='product_2'),
    Row(id_category=None, id_product=3, name_product='product_3')
])

df_result = df_product.join(df_category, on=['id_category'], how='left')

df_category.show()
df_product.show()

df_result.select((df_result.name_product).alias('product'), (df_result.name_category).alias('category')).show()