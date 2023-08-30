# coding: utf-8

"""
    Speech to Text API v3.0

    Speech to Text API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Dataset(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'links': 'Links',
        'properties': 'DatasetProperties',
        'kind': 'str',
        '_self': 'str',
        'display_name': 'str',
        'description': 'str',
        'project': 'EntityReference',
        'content_url': 'str',
        'custom_properties': 'dict(str, str)',
        'locale': 'str',
        'last_action_date_time': 'datetime',
        'status': 'str',
        'created_date_time': 'datetime'
    }

    attribute_map = {
        'links': 'links',
        'properties': 'properties',
        'kind': 'kind',
        '_self': 'self',
        'display_name': 'displayName',
        'description': 'description',
        'project': 'project',
        'content_url': 'contentUrl',
        'custom_properties': 'customProperties',
        'locale': 'locale',
        'last_action_date_time': 'lastActionDateTime',
        'status': 'status',
        'created_date_time': 'createdDateTime'
    }

    def __init__(self, links=None, properties=None, kind=None, _self=None, display_name=None, description=None, project=None, content_url=None, custom_properties=None, locale=None, last_action_date_time=None, status=None, created_date_time=None, _configuration=None):  # noqa: E501
        """Dataset - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._properties = None
        self._kind = None
        self.__self = None
        self._display_name = None
        self._description = None
        self._project = None
        self._content_url = None
        self._custom_properties = None
        self._locale = None
        self._last_action_date_time = None
        self._status = None
        self._created_date_time = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if properties is not None:
            self.properties = properties
        self.kind = kind
        if _self is not None:
            self._self = _self
        self.display_name = display_name
        if description is not None:
            self.description = description
        if project is not None:
            self.project = project
        if content_url is not None:
            self.content_url = content_url
        if custom_properties is not None:
            self.custom_properties = custom_properties
        self.locale = locale
        if last_action_date_time is not None:
            self.last_action_date_time = last_action_date_time
        if status is not None:
            self.status = status
        if created_date_time is not None:
            self.created_date_time = created_date_time

    @property
    def links(self):
        """Gets the links of this Dataset.  # noqa: E501

        The links for additional actions or content related to this dataset.  # noqa: E501

        :return: The links of this Dataset.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Dataset.

        The links for additional actions or content related to this dataset.  # noqa: E501

        :param links: The links of this Dataset.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def properties(self):
        """Gets the properties of this Dataset.  # noqa: E501

        Additional configuration options when creating a new dataset and additional metadata provided by the service.  # noqa: E501

        :return: The properties of this Dataset.  # noqa: E501
        :rtype: DatasetProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Dataset.

        Additional configuration options when creating a new dataset and additional metadata provided by the service.  # noqa: E501

        :param properties: The properties of this Dataset.  # noqa: E501
        :type: DatasetProperties
        """

        self._properties = properties

    @property
    def kind(self):
        """Gets the kind of this Dataset.  # noqa: E501

        The kind of the dataset.  # noqa: E501

        :return: The kind of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Dataset.

        The kind of the dataset.  # noqa: E501

        :param kind: The kind of this Dataset.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["Language", "Acoustic", "Pronunciation", "AudioFiles"]  # noqa: E501
        if (self._configuration.client_side_validation and
                kind not in allowed_values):
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def _self(self):
        """Gets the _self of this Dataset.  # noqa: E501

        The location of this entity.  # noqa: E501

        :return: The _self of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Dataset.

        The location of this entity.  # noqa: E501

        :param _self: The _self of this Dataset.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def display_name(self):
        """Gets the display_name of this Dataset.  # noqa: E501

        The display name of the object.  # noqa: E501

        :return: The display_name of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Dataset.

        The display name of the object.  # noqa: E501

        :param display_name: The display_name of this Dataset.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Dataset.  # noqa: E501

        The description of the object.  # noqa: E501

        :return: The description of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Dataset.

        The description of the object.  # noqa: E501

        :param description: The description of this Dataset.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project(self):
        """Gets the project of this Dataset.  # noqa: E501

        The project, the dataset is associated with.  # noqa: E501

        :return: The project of this Dataset.  # noqa: E501
        :rtype: EntityReference
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Dataset.

        The project, the dataset is associated with.  # noqa: E501

        :param project: The project of this Dataset.  # noqa: E501
        :type: EntityReference
        """

        self._project = project

    @property
    def content_url(self):
        """Gets the content_url of this Dataset.  # noqa: E501

        The URL of the data for the dataset.  # noqa: E501

        :return: The content_url of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._content_url

    @content_url.setter
    def content_url(self, content_url):
        """Sets the content_url of this Dataset.

        The URL of the data for the dataset.  # noqa: E501

        :param content_url: The content_url of this Dataset.  # noqa: E501
        :type: str
        """

        self._content_url = content_url

    @property
    def custom_properties(self):
        """Gets the custom_properties of this Dataset.  # noqa: E501

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :return: The custom_properties of this Dataset.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this Dataset.

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :param custom_properties: The custom_properties of this Dataset.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def locale(self):
        """Gets the locale of this Dataset.  # noqa: E501

        The locale of the contained data.  # noqa: E501

        :return: The locale of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Dataset.

        The locale of the contained data.  # noqa: E501

        :param locale: The locale of this Dataset.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501

        self._locale = locale

    @property
    def last_action_date_time(self):
        """Gets the last_action_date_time of this Dataset.  # noqa: E501

        The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The last_action_date_time of this Dataset.  # noqa: E501
        :rtype: datetime
        """
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        """Sets the last_action_date_time of this Dataset.

        The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param last_action_date_time: The last_action_date_time of this Dataset.  # noqa: E501
        :type: datetime
        """

        self._last_action_date_time = last_action_date_time

    @property
    def status(self):
        """Gets the status of this Dataset.  # noqa: E501

        The status of the object.  # noqa: E501

        :return: The status of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Dataset.

        The status of the object.  # noqa: E501

        :param status: The status of this Dataset.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotStarted", "Running", "Succeeded", "Failed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_date_time(self):
        """Gets the created_date_time of this Dataset.  # noqa: E501

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The created_date_time of this Dataset.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this Dataset.

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param created_date_time: The created_date_time of this Dataset.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Dataset, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Dataset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dataset):
            return True

        return self.to_dict() != other.to_dict()
