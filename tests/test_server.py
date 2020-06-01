# SPDX-License-Identifier: MIT

import jeepney.wrappers
import pytest

from dbus_objects.integration.jeepney.blocking import DBusServer


def test_create(server):
    pass


def test_create_error():
    with pytest.raises(jeepney.wrappers.DBusErrorResponse):
        DBusServer(bus='SESSION', name='org.freedesktop.DBus')