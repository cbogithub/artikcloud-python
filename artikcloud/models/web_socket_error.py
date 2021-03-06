# coding: utf-8

"""
    ARTIK Cloud API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class WebSocketError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message=None, code=None, cid=None):
        """
        WebSocketError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'code': 'int',
            'cid': 'str'
        }

        self.attribute_map = {
            'message': 'message',
            'code': 'code',
            'cid': 'cid'
        }

        self._message = message
        self._code = code
        self._cid = cid

    @property
    def message(self):
        """
        Gets the message of this WebSocketError.
        Message.

        :return: The message of this WebSocketError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WebSocketError.
        Message.

        :param message: The message of this WebSocketError.
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """
        Gets the code of this WebSocketError.
        Code

        :return: The code of this WebSocketError.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this WebSocketError.
        Code

        :param code: The code of this WebSocketError.
        :type: int
        """

        self._code = code

    @property
    def cid(self):
        """
        Gets the cid of this WebSocketError.
        Confirmation ID

        :return: The cid of this WebSocketError.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """
        Sets the cid of this WebSocketError.
        Confirmation ID

        :param cid: The cid of this WebSocketError.
        :type: str
        """

        self._cid = cid

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
