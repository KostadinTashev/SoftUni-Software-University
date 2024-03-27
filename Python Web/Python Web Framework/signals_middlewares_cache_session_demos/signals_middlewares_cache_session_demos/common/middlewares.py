from datetime import date
from time import sleep


def sleep_middleware(get_response):
    def middleware(request, *args, **kwargs):
        sleep(3)
        return get_response(request, *args, **kwargs)

    return middleware


def set_profile_middleware(get_response):
    def middleware(request, *args, **kwargs):
        if request.user.is_authenticated:
            request.profile = request.user.profile
        else:
            request.profile = None
        return get_response(request, *args, **kwargs)

    return middleware


def measure_execution_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = date.today()
        response = get_response(request, *args, **kwargs)
        end_time = date.today()

        print(f'Executed in {end_time - start_time} seconds')

        return response

    return middleware
