import unittest
from social_analysis.social_validator import validate_social_engagement

class TestSocialAnalysis(unittest.TestCase):

    def test_validate_social_engagement(self):
        social_data = {
            "likes": 500,
            "comments": 5,
            "shares": 10,
            "followers": 10000,
            "views": 150000
        }

        result = validate_social_engagement(social_data)

        self.assertFalse(result['authenticity_detected'])
        self.assertEqual(len(result['issues']), 2)
        self.assertIn("Low engagement-to-follower ratio", result['issues'])
        self.assertIn("Unusually high views relative to followers", result['issues'])

if __name__ == "__main__":
    unittest.main()
