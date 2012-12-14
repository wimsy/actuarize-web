# -*- coding: utf-8 -*-

###############################################################################
#
# PublishLink
# Publishes a link on a given profile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PublishLink(Choreography):

    """
    Create a new instance of the PublishLink Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/PublishLink')


    def new_input_set(self):
        return PublishLinkInputSet()

    def _make_result_set(self, result, path):
        return PublishLinkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PublishLinkChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PublishLink
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PublishLinkInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Caption input for this choreography. ((optional, string) A caption for the link being published.)
        """
        def set_Caption(self, value):
            InputSet._set_input(self, 'Caption', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) A description of the link being published.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the Link input for this choreography. ((required, string) The link to publish.)
        """
        def set_Link(self, value):
            InputSet._set_input(self, 'Link', value)

        """
        Set the value of the Message input for this choreography. ((optional, string) A message about the link.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the Name input for this choreography. ((optional, string) The name of the link.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Picture input for this choreography. ((optional, string) A URL to the thumbnail image to use for the link post.)
        """
        def set_Picture(self, value):
            InputSet._set_input(self, 'Picture', value)

        """
        Set the value of the ProfileID input for this choreography. ((optional, string) The id of the profile that the link will be published to. Defaults to "me" indicating the authenticated user.)
        """
        def set_ProfileID(self, value):
            InputSet._set_input(self, 'ProfileID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the PublishLink choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PublishLinkResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PublishLinkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PublishLinkResultSet(response, path)
