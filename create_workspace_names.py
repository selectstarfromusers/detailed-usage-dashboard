# Databricks notebook source
# DBTITLE 1,Get widget values
# Get widget values
wn_catalog = dbutils.widgets.get("wn_catalog")
wn_schema = dbutils.widgets.get("wn_schema")
wn_table = dbutils.widgets.get("wn_table")

# COMMAND ----------

# DBTITLE 1,Create catalog if not exists
create_catalog_sql = f"CREATE CATALOG IF NOT EXISTS {wn_catalog}"
spark.sql(create_catalog_sql)

# COMMAND ----------

# DBTITLE 1,Create schema if not exists
create_schema_sql = f"CREATE SCHEMA IF NOT EXISTS {wn_catalog}.{wn_schema}"
spark.sql(create_schema_sql)

# COMMAND ----------

# DBTITLE 1,Create table if not exists
full_table_name = f"{wn_catalog}.{wn_schema}.{wn_table}"
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS {full_table_name} (
  workspace_name STRING,
  workspace_id STRING
)
USING delta
"""
spark.sql(create_table_sql)

# COMMAND ----------

# DBTITLE 1,Query the table
df = spark.table(full_table_name)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC The table is empty, but when you populate it with workspace ids and the corresponding workspace names the dashboards will update.