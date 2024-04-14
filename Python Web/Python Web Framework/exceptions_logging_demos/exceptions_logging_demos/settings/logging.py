from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'log.txt',
            'formatter': 'simple',

        }

    },
    'formatters': {
        'simple': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        # 'django': {
        #     'handlers': ['file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
    }
}
