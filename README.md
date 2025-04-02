# Detailed Usage Dashboards

These Dashboards were built with the primary goal of addressing cost visibility concerns from customers in $ amounts that match up to their actual spend, accounting for contract discounts and terms as well as Platforms teams needing better visibility into usage and inefficiencies. The first tab (Executive Summary) focuses on Leadership level reporting while the rest focus on reporting for the Platform team.

# Disclaimer

These dashboards are not official Databricks products. They are community-built resources provided as-is, with no dedicated ongoing support. Please review and test in your environment, as they are intended for use at your own risk

## Setup Instructions

### Pre-requisites
- **Databricks Workspace with Unity Catalog Enabled** - Almost this entire dashboard relies on System Tables that are enabled as part of Unity Catalog  
- **AI_Forecast Function Preview** - In order for the Commit Burndown Chart to work on the Executive Summary page, the AI_Forecast function preview needs to be enabled in the workspace where this dashboard is being imported into. The Databricks account team can help with enrollment into the preview
- **Permissions to Create a Table** - A notebook is provided in this repo that will create a workspace_names table in the desired Catalog/Schema (it will create them as well if they do not already exist and you have sufficient permissions). This table is required for most if not the entirety of this dashboard to function 


### Setup (Git Repo)
- **Add Repo Credentials** - In your Databricks workpace click on your user icon in the top right and click Settings then in the left hand menu click Linked Accounts
  - ![image](https://github.com/user-attachments/assets/2d4e9c38-e3b4-4199-ac53-5522a15cbe81)
  - ![image](https://github.com/user-attachments/assets/9e463cc4-009e-4acf-ab9d-ab36499b70a3)
  - Either link your Git account or add your Git token
- **Import Repo** - In Databricks > Workspace click Create > Git folder then paste the Git URL in the respective field and click Create Git Folder
  - ![image](https://github.com/user-attachments/assets/92767f56-bead-47a9-bcb7-77115913cc1a)
  - ![image](https://github.com/user-attachments/assets/602d0438-2870-4226-ba13-d9d29e71ad95)
- **Workspace_names table** - In the new Git folder, open notebook file create_workspace_names to create the workspace_names table in the desired catalog/schema, update the wn_catalog, wn_schema, and wn_table widget parameters to the desired location and execute
- **Update workspace_names parameters** - Open the Dashboard file in the Git folder, click Data on the top, then in all dashboard datasets that start with de_perf, de_usage, and u_workspace, update the wn_catalog, wn_schema, and wn_table parameters to match the location of the workspace_names table you created
- **Update contract parameters** - On the Executive Summary dashboard, update the Contract Start, Contract End, Contract Commit and Cloud Discount parameters to reflect your/your customer's current contractual agreement
- **Refresh the Dashboard and Publish!**
 

### Setup (Manual)
- **Workspace_names table** - Import notebook file create_workspace_names to create the workspace_names table in the desired catalog/schema, update the wn_catalog, wn_schema, and wn_table widget parameters to the desired location and execute
- **Import Dashboard**
  - In the desired workspace, click on Dashboards from the left hand menu
    - ![image](https://github.com/user-attachments/assets/ed38eb14-1e05-4fa3-9182-9fc91f4ff978)
  - On the top right, click on the drop down right of the "Create Dashboard" button and click import Dashboard from file
    - ![image](https://github.com/user-attachments/assets/8ddcfc28-c645-479e-b4d0-098d5b65be16)
- **Update workspace_names parameters** - In all dashboard datasets that start with de_perf, de_usage, and u_workspace, update the wn_catalog, wn_schema, and wn_table parameters to match the location of the workspace_names table you created
- **Update contract parameters** - On the Executive Summary dashboard, update the Contract Start, Contract End, Contract Commit and Cloud Discount parameters to reflect your/your customer's current contractual agreement
- **Refresh the Dashboard and Publish!**
