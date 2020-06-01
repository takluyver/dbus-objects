# SPDX-License-Identifier: MIT

import pytest

from dbus_objects.integration.jeepney.blocking import DBusServer
from dbus_objects.object import DBusObject, dbus_method
from dbus_objects.types import multiple_return


class ExampleObject(DBusObject):
    def __init__(self):
        super().__init__()
        self.server_name = 'com.example.object'

    @dbus_method()
    def example_method(self) -> str:
        return 'test'

    def normal_method(self):
        pass  # pragma: no cover

    @dbus_method()
    def ping(self) -> str:
        return 'Pong!'  # pragma: no cover

    @dbus_method()
    def print(self, msg: str) -> None:
        print(msg)  # pragma: no cover

    @dbus_method()
    def multiple(self, msg: str) -> multiple_return(int, int):
        print(msg)  # pragma: no cover


@pytest.fixture(scope='session')
def obj():
    return ExampleObject()


@pytest.fixture()
def obj_methods(obj):
    return obj.get_dbus_methods()


@pytest.fixture(params=['SESSION'])
def server(request):
    server = DBusServer(request.param, 'com.example.object')

    yield server

    server.close()