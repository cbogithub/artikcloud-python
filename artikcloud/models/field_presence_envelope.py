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


class FieldPresenceEnvelope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, sdid=None, field_presence=None, start_date=None, end_date=None, interval=None, size=None, data=None):
        """
        FieldPresenceEnvelope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sdid': 'str',
            'field_presence': 'str',
            'start_date': 'int',
            'end_date': 'int',
            'interval': 'str',
            'size': 'int',
            'data': 'list[FieldPresence]'
        }

        self.attribute_map = {
            'sdid': 'sdid',
            'field_presence': 'fieldPresence',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'interval': 'interval',
            'size': 'size',
            'data': 'data'
        }

        self._sdid = sdid
        self._field_presence = field_presence
        self._start_date = start_date
        self._end_date = end_date
        self._interval = interval
        self._size = size
        self._data = data

    @property
    def sdid(self):
        """
        Gets the sdid of this FieldPresenceEnvelope.


        :return: The sdid of this FieldPresenceEnvelope.
        :rtype: str
        """
        return self._sdid

    @sdid.setter
    def sdid(self, sdid):
        """
        Sets the sdid of this FieldPresenceEnvelope.


        :param sdid: The sdid of this FieldPresenceEnvelope.
        :type: str
        """

        self._sdid = sdid

    @property
    def field_presence(self):
        """
        Gets the field_presence of this FieldPresenceEnvelope.


        :return: The field_presence of this FieldPresenceEnvelope.
        :rtype: str
        """
        return self._field_presence

    @field_presence.setter
    def field_presence(self, field_presence):
        """
        Sets the field_presence of this FieldPresenceEnvelope.


        :param field_presence: The field_presence of this FieldPresenceEnvelope.
        :type: str
        """

        self._field_presence = field_presence

    @property
    def start_date(self):
        """
        Gets the start_date of this FieldPresenceEnvelope.


        :return: The start_date of this FieldPresenceEnvelope.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this FieldPresenceEnvelope.


        :param start_date: The start_date of this FieldPresenceEnvelope.
        :type: int
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this FieldPresenceEnvelope.


        :return: The end_date of this FieldPresenceEnvelope.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this FieldPresenceEnvelope.


        :param end_date: The end_date of this FieldPresenceEnvelope.
        :type: int
        """

        self._end_date = end_date

    @property
    def interval(self):
        """
        Gets the interval of this FieldPresenceEnvelope.


        :return: The interval of this FieldPresenceEnvelope.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this FieldPresenceEnvelope.


        :param interval: The interval of this FieldPresenceEnvelope.
        :type: str
        """

        self._interval = interval

    @property
    def size(self):
        """
        Gets the size of this FieldPresenceEnvelope.


        :return: The size of this FieldPresenceEnvelope.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this FieldPresenceEnvelope.


        :param size: The size of this FieldPresenceEnvelope.
        :type: int
        """

        self._size = size

    @property
    def data(self):
        """
        Gets the data of this FieldPresenceEnvelope.


        :return: The data of this FieldPresenceEnvelope.
        :rtype: list[FieldPresence]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this FieldPresenceEnvelope.


        :param data: The data of this FieldPresenceEnvelope.
        :type: list[FieldPresence]
        """

        self._data = data

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
