from django.core.exceptions import PermissionDenied
from time import sleep
from datetime import datetime, timedelta


class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        banned_ips = [
            '127.0.0.2'
        ]

        ip = request.META.get('REMOTE_ADDR')
        if ip in banned_ips:
            raise PermissionDenied

        response = self.get_response(request)
        return response


class DelayMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0
        self.n_request = 3
        self.delay = 2

    def __call__(self, request):
        self.counter += 1
        print(f'Запрос № {self.counter}')
        if self.counter == self.n_request:
            print(f'Ждем {self.delay} секунды')
            sleep(self.delay)
            self.counter = 0

        response = self.get_response(request)

        return response


class PeriodMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.time = 5
        self.requests = 3
        self.ips = dict()

    def __call__(self, request):
        now = datetime.now()
        curr_ip = request.META.get('REMOTE_ADDR')
        if self.ips.get(curr_ip):
            if len(self.ips[curr_ip]) == self.requests:
                self.ips[curr_ip].pop(0)

            self.ips[curr_ip].append(now)
            if self.ips[curr_ip][-1] - self.ips[curr_ip][0] < timedelta(seconds=self.time):
                raise PermissionDenied
        else:
            self.ips[curr_ip] = [now]

        response = self.get_response(request)

        return response
