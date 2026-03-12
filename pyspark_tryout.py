from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import row_number, col

# Initialize Spark Session (if not already running)
spark = SparkSession.builder.appName("WindowPartitionSample").getOrCreate()

# Create a sample DataFrame
data = [
    ("Bob", "HR", 1200),
    ("Frank", "HR", 1100),
    ("Alice", "HR", 1000),
    ("David", "IT", 1700),
    ("Eve", "IT", 1600),
    ("Cathy", "IT", 1500)
]
columns = ["Name", "Department", "Salary"]
df = spark.createDataFrame(data, columns)
df.show()

# Define the window specification
# Partition by "Department" and order by "Salary" in descending order
window_spec = Window.partitionBy("Department").orderBy(col("Salary").desc())

# Apply the window function to add a new column "rank"
df_ranked = df.withColumn(
    "department_rank", 
    row_number().over(window_spec)
)

# Show the result
df_ranked.show()
