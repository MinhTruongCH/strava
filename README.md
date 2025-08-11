# Strava Activities Pipeline on Databricks

This project connects to the Strava API, retrieves the authenticated athlete's activities, stores them securely in Databricks using Secrets, and processes them into Bronze/Silver Delta tables for analysis.

## 🚀 Features
- **OAuth2 Authentication with Strava**
- Automatic token refresh using the `refresh_token`
- Retrieval of recent activities via the [Strava API](https://developers.strava.com/docs/reference/)
- Secure storage of sensitive credentials in Databricks Secrets
- Raw ingestion into **Bronze** table
- Cleaned and transformed data into **Silver** table with proper schema
- Ready for BI dashboards and analytics

## 🗂 Project Structure
