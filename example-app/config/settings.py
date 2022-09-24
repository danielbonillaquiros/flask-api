class BaseConfig:
    """Base Configuration
    """
    API_PREFIX = '/api'
    TESTING = False
    DEBUG = False


class DevConfig(BaseConfig):
    """Development Configuration
    """
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:' \
                              + '5432/flask-deploy'
    CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
    CELERY_RESULT_BACKEND = 'pyamqp://rabbit_user:rabbit_password@' \
                            + 'broker-rabbitmq//'


class ProductionConfig(BaseConfig):
    """Production Configuration
    """
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:' \
                              + '5432/flask-deploy'
    CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
    CELERY_RESULT_BACKEND = 'pyamqp://rabbit_user:rabbit_password@' \
                            + 'broker-rabbitmq//'


class TestConfig(BaseConfig):
    """Test Configuration
    """
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    # make celery execute tasks synchronously in the smae process
    CELERY_ALWAYS_EAGER = True
