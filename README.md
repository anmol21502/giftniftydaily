# GIFT NIFTY Market API

A simple Flask API that scrapes the latest GIFT NIFTY value from MoneyControl using Selenium.

## Endpoint

`GET /getGiftNifty`

### Example Response

```json
{
  "status": "success",
  "market": "GIFT NIFTY",
  "value": "22450.00"
}
```

## Deployment

This app is ready to deploy on [Render.com](https://render.com).

1. Push this repo to GitHub.
2. Create a **new Web Service** on Render.
3. Connect your GitHub repo.
4. Render will detect `render.yaml` and auto-deploy.

✅ Done!
