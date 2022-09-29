# Copyright 2022 University of Waterloo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def handle_error_response(resp):
    """Handle Alma API exceptions."""
    codes = {
        -1: AlmaApiError,
        -402119: GeneralError,
        -40166410: InvalidParameterWithValidOptionsError,
        -40166419: NoValidOptionsParameterError,
        -401873: NoFilterWithPolModeError,
    }
    error = resp.json().get('error', {})
    message = error.get('message')
    code = error.get('code', -1)
    data = error.get('data', {})
    raise codes[code](message=message, code=code, data=data, response=resp)


class AlmaApiError(Exception):
    """An Alma API exception."""

    response = None
    data = {}
    code = -1
    message = "An unknown error occurred"

    def __init__(self, message=None, code=None, data={}, response=None):
        """Init method."""
        self.response = response
        if message:
            self.message = message
        if code:
            self.code = code
        if data:
            self.data = data

    def __str__(self):
        """Create string representation."""
        if self.code:
            return '{}: {}'.format(self.code, self.message)
        return self.message


class GeneralError(AlmaApiError):
    """Handle an Alma API GeneralError exception."""

    pass


class InvalidParameterWithValidOptionsError(AlmaApiError):
    """Handle an Alma API InvalidParameterWithValidOptionsError exception."""

    pass


class NoValidOptionsParameterError(AlmaApiError):
    """Handle an Alma API NoValidOptionsParameterError exception."""

    pass


class NoFilterWithPolModeError(AlmaApiError):
    """Handle an Alma API NoFilterWithPolModeError exception."""

    pass
