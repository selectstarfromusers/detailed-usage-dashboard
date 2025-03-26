# Detailed Usage Dashboards

These Dashboards were built with the primary goal of addressing cost visibility concerns from customers in $ amounts that match up to their actual spend, accounting for contract discounts and terms as well as Platforms teams needing better visibility into usage and inefficiencies. The first tab (Executive Summary) focuses on Leadership level reporting while the rest focus on reporting for the Platform team.

# Disclaimer

These dashboards are not official Databricks products. They are community-built resources provided as-is, with no dedicated ongoing support. Please review and test in your environment, as they are intended for use at your own risk

## Setup Instructions

### Pre-requisites
- **AI_Forecast Function Preview** - In order for the Commit Burndown Chart to work on the Executive Summary page, the AI_Forecast function preview needs to be enabled in the workspace where this dashboard is being imported into. The Databricks account team can help with enrollment into the preview  

### Setup (Git Repo)  
- Coming Soon  

### Setup (Manual)
- **Workspace_names table** - Copy the code from create_workspace_names.dbquery.ipynb to create the workspace_names table in the desired catalog/schema, update the wn_catalog, wn_schema, and wn_table parameters to the desired location and execute
- **Import Dashboard**
  - In the desired workspace, click on Dashboards from the left hand menu
    - ![image](https://github.com/user-attachments/assets/cb867c6f-649c-44de-8c38-ab9ed7479441)
  - On the top right, click on the drop down right of the "Create Dashboard" button and click import Dashboard from file
    - ![image](https://github.com/user-attachments/assets/4a988a43-acef-40eb-b806-3b3b1b7ff120)
- **Update workspace_names parameters** - In all dashboard datasets that start with de_perf, de_usage, and u_workspace, update the wn_catalog, wn_schema, and wn_table parameters to match the location of the workspace_names table you created
- **Update contract parameters** - On the Executive Summary dashboard, update the Contract Start, Contract End, Contract Commit and Cloud Discount parameters to reflect your/your customer's current contractual agreement
- **Refresh the Dashboard!**
