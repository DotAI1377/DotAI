import unittest
from contracts_analysis.transaction_analyzer import analyze_transactions
from contracts_analysis.vulnerability_scanner import scan_for_vulnerabilities

class TestContractsAnalysis(unittest.TestCase):

    def test_analyze_transactions(self):
        transactions = [
            {"amount": 15000, "from_address": "0xScamAddress1", "to_address": "0xSafeAddress", "timestamp": 1633024800},
            {"amount": 500, "from_address": "0xSafeAddress", "to_address": "0xSafeAddress", "timestamp": 1633024900}
        ]

        result = analyze_transactions(transactions)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['risk_factors'][0], "Large transaction amount")
        self.assertEqual(result[1]['risk_factors'][0], "Sender and receiver addresses are identical")

    def test_scan_for_vulnerabilities(self):
        contract_code = """
        pragma solidity ^0.8.0;
        contract Test {
            function destroy() public {
                selfdestruct(payable(msg.sender));
            }
            function authenticate() public {
                if (tx.origin == msg.sender) {
                    // insecure auth
                }
            }
        }
        """

        result = scan_for_vulnerabilities(contract_code)

        self.assertEqual(result['vulnerabilities_found'], 2)
        self.assertEqual(result['details'][0]['issue'], "Use of selfdestruct")
        self.assertEqual(result['details'][1]['issue'], "Use of tx.origin")

if __name__ == "__main__":
    unittest.main()
