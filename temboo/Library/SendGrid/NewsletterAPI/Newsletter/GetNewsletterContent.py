# -*- coding: utf-8 -*-

###############################################################################
#
# GetNewsletterContent
# Retrieve contents of a specified newsletter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetNewsletterContent(Choreography):

    """
    Create a new instance of the GetNewsletterContent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Newsletter/GetNewsletterContent')


    def new_input_set(self):
        return GetNewsletterContentInputSet()

    def _make_result_set(self, result, path):
        return GetNewsletterContentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewsletterContentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetNewsletterContent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetNewsletterContentInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from SendGrid.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APIUser input for this choreography. ((required, string) The username registered with SendGrid.)
        """
        def set_APIUser(self, value):
            InputSet._set_input(self, 'APIUser', value)

        """
        Set the value of the Name input for this choreography. ((required, string) The name of the newsletter to be retrieved. It must be an existing newsletter.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the GetNewsletterContent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetNewsletterContentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetNewsletterContentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNewsletterContentResultSet(response, path)
