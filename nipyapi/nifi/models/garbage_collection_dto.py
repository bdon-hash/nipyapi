# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.9.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GarbageCollectionDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'collection_count': 'int',
        'collection_time': 'str',
        'collection_millis': 'int'
    }

    attribute_map = {
        'name': 'name',
        'collection_count': 'collectionCount',
        'collection_time': 'collectionTime',
        'collection_millis': 'collectionMillis'
    }

    def __init__(self, name=None, collection_count=None, collection_time=None, collection_millis=None):
        """
        GarbageCollectionDTO - a model defined in Swagger
        """

        self._name = None
        self._collection_count = None
        self._collection_time = None
        self._collection_millis = None

        if name is not None:
          self.name = name
        if collection_count is not None:
          self.collection_count = collection_count
        if collection_time is not None:
          self.collection_time = collection_time
        if collection_millis is not None:
          self.collection_millis = collection_millis

    @property
    def name(self):
        """
        Gets the name of this GarbageCollectionDTO.
        The name of the garbage collector.

        :return: The name of this GarbageCollectionDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GarbageCollectionDTO.
        The name of the garbage collector.

        :param name: The name of this GarbageCollectionDTO.
        :type: str
        """

        self._name = name

    @property
    def collection_count(self):
        """
        Gets the collection_count of this GarbageCollectionDTO.
        The number of times garbage collection has run.

        :return: The collection_count of this GarbageCollectionDTO.
        :rtype: int
        """
        return self._collection_count

    @collection_count.setter
    def collection_count(self, collection_count):
        """
        Sets the collection_count of this GarbageCollectionDTO.
        The number of times garbage collection has run.

        :param collection_count: The collection_count of this GarbageCollectionDTO.
        :type: int
        """

        self._collection_count = collection_count

    @property
    def collection_time(self):
        """
        Gets the collection_time of this GarbageCollectionDTO.
        The total amount of time spent garbage collecting.

        :return: The collection_time of this GarbageCollectionDTO.
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """
        Sets the collection_time of this GarbageCollectionDTO.
        The total amount of time spent garbage collecting.

        :param collection_time: The collection_time of this GarbageCollectionDTO.
        :type: str
        """

        self._collection_time = collection_time

    @property
    def collection_millis(self):
        """
        Gets the collection_millis of this GarbageCollectionDTO.
        The total number of milliseconds spent garbage collecting.

        :return: The collection_millis of this GarbageCollectionDTO.
        :rtype: int
        """
        return self._collection_millis

    @collection_millis.setter
    def collection_millis(self, collection_millis):
        """
        Sets the collection_millis of this GarbageCollectionDTO.
        The total number of milliseconds spent garbage collecting.

        :param collection_millis: The collection_millis of this GarbageCollectionDTO.
        :type: int
        """

        self._collection_millis = collection_millis

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
        if not isinstance(other, GarbageCollectionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
