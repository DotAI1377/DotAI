def validate_social_engagement(social_data):
    """
    Validates social media engagement data to detect signs of inauthentic activity.

    Args:
        social_data (dict): A dictionary containing social media engagement metrics.
            Expected keys: ['likes', 'comments', 'shares', 'followers', 'views']

    Returns:
        dict: Analysis results indicating authenticity of engagement.
    """
    flagged_issues = []

    # Check for high follower-to-engagement ratio
    if social_data['followers'] > 0:
        engagement_ratio = (
            social_data['likes'] + social_data['comments'] + social_data['shares']
        ) / social_data['followers']

        if engagement_ratio < 0.01:  # Less than 1% engagement
            flagged_issues.append("Low engagement-to-follower ratio")

    # Check for excessive bot-like views compared to followers
    if social_data['views'] > social_data['followers'] * 10:
        flagged_issues.append("Unusually high views relative to followers")

    # Check for unrealistic likes-to-comments ratio
    if social_data['comments'] > 0:
        likes_to_comments_ratio = social_data['likes'] / social_data['comments']

        if likes_to_comments_ratio > 100:  # Unnaturally high ratio
            flagged_issues.append("Suspicious likes-to-comments ratio")

    return {
        "authenticity_detected": len(flagged_issues) == 0,
        "issues": flagged_issues
    }
