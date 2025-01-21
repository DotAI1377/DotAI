import os

class Config:
    """
    Base configuration class for the application.
    """
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    DEBUG = os.getenv("DEBUG", False)
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///app.db")

class DevelopmentConfig(Config):
    """
    Configuration class for development environment.
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    Configuration class for production environment.
    """
    DEBUG = False

class TestingConfig(Config):
    """
    Configuration class for testing environment.
    """
    TESTING = True
    DATABASE_URI = "sqlite:///:memory:"

# Config selector
def get_config(env):
    """
    Returns the appropriate configuration class based on the environment.

    Args:
        env (str): The environment name (e.g., 'development', 'production', 'testing').

    Returns:
        Config: The corresponding configuration class.
    """
    env = env.lower()
    if env == "development":
        return DevelopmentConfig
    elif env == "production":
        return ProductionConfig
    elif env == "testing":
        return TestingConfig
    else:
        return Config
