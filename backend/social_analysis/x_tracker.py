import requests

def simulate_twitter_api_interaction(account_handle):
    """
    Simulates interaction with the Twitter API to track account activity.

    Args:
        account_handle (str): The Twitter handle of the account to track.

    Returns:
        dict: Simulated response with engagement metrics.
    """
    # Simulated Twitter API response
    response = {
        "account": account_handle,
        "followers_count": 15000,
        "engagement_rate": 0.05,
        "suspicious_activity_detected": False,
    }

    # Simulate suspicious activity detection
    if response["engagement_rate"] < 0.01:
        response["suspicious_activity_detected"] = True

    return response

if __name__ == "__main__":
    account = "example_handle"
    result = simulate_twitter_api_interaction(account)
    print(f"Simulated Twitter API Response: {result}")
