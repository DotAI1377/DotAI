def track_wallet_activity(wallet_address, transactions):
    """
    Monitors wallet activity to detect suspicious behavior.

    Args:
        wallet_address (str): The wallet address to monitor.
        transactions (list): A list of transaction dictionaries associated with the wallet.

    Returns:
        dict: Analysis results including suspicious activity flags.
    """
    suspicious_activity = []

    for tx in transactions:
        if tx.get("from") == wallet_address or tx.get("to") == wallet_address:
            # Check for unusually large transfers
            if tx.get("amount", 0) > 100000:  # Example threshold
                suspicious_activity.append({
                    "transaction": tx,
                    "issue": "Unusually large transfer"
                })

            # Check for rapid sequential transactions
            if tx.get("timestamp") and is_rapid_sequence(tx, transactions):
                suspicious_activity.append({
                    "transaction": tx,
                    "issue": "Rapid sequential transactions detected"
                })

            # Check for transfers to flagged addresses
            if tx.get("to") in known_suspicious_addresses():
                suspicious_activity.append({
                    "transaction": tx,
                    "issue": "Transfer to known suspicious address"
                })

    return {
        "wallet_address": wallet_address,
        "suspicious_activity_detected": len(suspicious_activity) > 0,
        "details": suspicious_activity
    }

def is_rapid_sequence(transaction, all_transactions):
    """
    Determines if a transaction is part of rapid sequential activity.

    Args:
        transaction (dict): The transaction to check.
        all_transactions (list): A list of all transactions for context.

    Returns:
        bool: True if the transaction is part of rapid sequential activity, False otherwise.
    """
    timestamp = transaction.get("timestamp")
    sequence_count = sum(
        1 for tx in all_transactions
        if abs(tx.get("timestamp", 0) - timestamp) <= 60  # 60 seconds threshold
    )
    return sequence_count > 5  # Example threshold for rapid transactions

def known_suspicious_addresses():
    """
    Returns a set of known suspicious wallet addresses.

    Returns:
        set: A set of flagged wallet addresses.
    """
    return {"0xSuspicious1", "0xSuspicious2"}
