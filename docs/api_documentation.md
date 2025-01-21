# API Documentation

This document provides details about the API endpoints for the AIris AI application. The API enables interaction with the backend for analyzing cryptocurrency data, monitoring activities, and retrieving results.

---

## Base URL
```
https://api.airis.ai
```

---

## Endpoints

### 1. **Analyze Smart Contract**
#### POST `/contracts/analyze`
- **Description**: Analyzes a given smart contract for potential vulnerabilities.
- **Request Body** (JSON):
  ```json
  {
      "contract_code": "string"
  }
  ```
- **Response** (JSON):
  ```json
  {
      "vulnerabilities_found": 2,
      "details": [
          {"issue": "Use of selfdestruct", "description": "The selfdestruct function can be exploited to drain contract funds."},
          {"issue": "Use of tx.origin", "description": "Using tx.origin for authentication can lead to phishing attacks."}
      ]
  }
  ```

### 2. **Monitor Wallet Activity**
#### POST `/wallets/monitor`
- **Description**: Monitors a wallet's activity for suspicious transactions.
- **Request Body** (JSON):
  ```json
  {
      "wallet_address": "string",
      "transactions": [
          {"from": "string", "to": "string", "amount": "number", "timestamp": "number"}
      ]
  }
  ```
- **Response** (JSON):
  ```json
  {
      "suspicious_activity_detected": true,
      "details": [
          {"transaction": {"from": "0x123", "to": "0x456", "amount": 200000}, "issue": "Unusually large transfer"}
      ]
  }
  ```

### 3. **Validate Social Media Engagement**
#### POST `/social/validate`
- **Description**: Validates social media metrics to detect inauthentic engagement.
- **Request Body** (JSON):
  ```json
  {
      "social_data": {
          "likes": "number",
          "comments": "number",
          "shares": "number",
          "followers": "number",
          "views": "number"
      }
  }
  ```
- **Response** (JSON):
  ```json
  {
      "authenticity_detected": false,
      "issues": ["Low engagement-to-follower ratio", "Unusually high views relative to followers"]
  }
  ```

### 4. **Check Market Activity**
#### POST `/market/analyze`
- **Description**: Analyzes market activity for insider trading or manipulation.
- **Request Body** (JSON):
  ```json
  {
      "trade_data": [
          {"price": "number", "volume": "number", "timestamp": "number", "trader": "string"}
      ]
  }
  ```
- **Response** (JSON):
  ```json
  {
      "suspicious_trades_detected": true,
      "details": [
          {"trade": {"price": 100, "volume": 50000}, "issues": ["Unusually large trade volume"]}
      ]
  }
  ```

---

## Authentication
Currently, the API does not require authentication for development purposes. For production, consider implementing:
- API keys
- OAuth tokens
- Rate limiting

---

## Error Handling
- **400 Bad Request**: Invalid or missing parameters.
- **500 Internal Server Error**: Server-side issue.
- Example Error Response:
  ```json
  {
      "error": "Invalid input",
      "details": "The provided contract code is empty."
  }
  ```

---

## Rate Limiting
- Development: Unlimited requests.
- Production: TBD (e.g., 100 requests per minute per IP).

---

For additional assistance, contact the development team at [support@airis.ai](mailto:support@airis.ai).
