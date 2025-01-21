import unittest
from wallet_monitoring.wallet_tracker import track_wallet_activity

class TestWalletMonitoring(unittest.TestCase):

    def test_track_wallet_activity(self):
        wallet_address = "0xTestWallet"
        transactions = [
            {"from": "0xTestWallet", "to": "0xRecipient1", "amount": 200000, "timestamp": 1633024800},
            {"from": "0xTestWallet", "to": "0xRecipient2", "amount": 500, "timestamp": 1633024810},
            {"from": "0xTestWallet", "to": "0xSuspicious1", "amount": 300, "timestamp": 1633024820},
            {"from": "0xTestWallet", "to": "0xRecipient3", "amount": 100, "timestamp": 1633024830},
            {"from": "0xTestWallet", "to": "0xRecipient4", "amount": 200, "timestamp": 1633024840},
            {"from": "0xTestWallet", "to": "0xRecipient5", "amount": 300, "timestamp": 1633024850}
        ]

        result = track_wallet_activity(wallet_address, transactions)

        self.assertTrue(result['suspicious_activity_detected'])
        self.assertEqual(len(result['details']), 3)
        self.assertEqual(result['details'][0]['issue'], "Unusually large transfer")
        self.assertEqual(result['details'][1]['issue'], "Rapid sequential transactions detected")
        self.assertEqual(result['details'][2]['issue'], "Transfer to known suspicious address")

if __name__ == "__main__":
    unittest.main()
