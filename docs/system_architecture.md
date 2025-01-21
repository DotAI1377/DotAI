# System Architecture

The AIris AI application is designed to identify potential scams and vulnerabilities in the cryptocurrency space. It is composed of multiple modules organized into a backend and frontend architecture, providing a robust and scalable solution.

---

## Overview

### 1. **Backend**
- **Technology**: Python, Flask
- **Responsibilities**:
  - Analyze smart contracts for vulnerabilities.
  - Detect website cloning activities.
  - Monitor wallet activities.
  - Perform social interaction analysis.
  - Review market and insider activities.
- **Modules**:
  - `contracts_analysis`: Smart contract analysis and vulnerability detection.
  - `website_cloning`: Detection of cloned project websites.
  - `wallet_monitoring`: Wallet activity analysis for fraudulent behavior.
  - `social_analysis`: Validation of authentic social media engagements.
  - `market_activity`: Identification of insider trading or manipulation patterns.

### 2. **Frontend**
- **Technology**: React
- **Responsibilities**:
  - Provide an interactive user interface.
  - Display analysis results in a clear and user-friendly manner.
  - Allow users to input data for analysis.
- **Components**:
  - Navbar, Footer, Home Page, Results Page
  
---

## Architecture Diagram

```
+-------------------+     +--------------------+
|   Frontend (UI)   | --> |   Backend (API)    |
|   React           |     |   Flask            |
+-------------------+     +--------------------+
          |                         |
          |                         |
   User Inputs             Contract Analysis,
          |               Wallet Monitoring,
   Displays Results       Market & Social Analysis
          |                         |
          v                         v
+------------------------------------------------+
|          Database & External APIs              |
|    Stores historical data, fetches insights    |
+------------------------------------------------+
```

---

## Data Flow

1. **User Interaction**:
   - Users input cryptocurrency project details into the frontend.
2. **Request Processing**:
   - The frontend sends requests to the backend through defined API endpoints.
3. **Analysis Execution**:
   - The backend performs analysis using AI models, transaction history, and pattern detection algorithms.
4. **Results Delivery**:
   - The backend returns analysis results to the frontend.
5. **User Display**:
   - The frontend displays the results in an organized and user-friendly interface.

---

## Technologies

### Backend
- **Framework**: Flask
- **Database**: SQLite (for development) / Scalable options for production
- **Languages**: Python

### Frontend
- **Framework**: React
- **Styling**: CSS-in-JS (Styled Components / Inline styles)
- **Routing**: React Router

---

## Future Improvements

1. Integration with blockchain data providers for real-time updates.
2. Advanced AI models for detecting newer vulnerabilities and scams.
3. Scalable cloud architecture for high user loads.
4. Role-based user authentication and access control.
