# Azure Web App Deployment

This project deploys to Azure App Service with GitHub Actions, without Docker.

## Azure Web App settings

Create an Azure Web App using the Python 3.11 runtime on Linux.

Set this startup command in Azure App Service > Configuration > General settings:

```bash
gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app --bind=0.0.0.0:8000
```

Add these application settings in Azure App Service > Configuration > Application settings:

- `MONGO_URL`
- `AZURE_ENDPOINT`
- `AZURE_API_KEY`

## GitHub secrets

Add these repository secrets in GitHub > Settings > Secrets and variables > Actions:

- `AZURE_WEBAPP_NAME`: your Azure Web App name, for example `retail-ai-api`
- `AZURE_WEBAPP_PUBLISH_PROFILE`: the publish profile XML downloaded from the Azure Web App Overview page

After these are set, every push to `main` runs tests and deploys automatically.
