# -*- coding: utf-8 -*-

###############################################################################
#
# CreateNewsletter
# Create a new newsletter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateNewsletter(Choreography):

    """
    Create a new instance of the CreateNewsletter Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Newsletter/CreateNewsletter')


    def new_input_set(self):
        return CreateNewsletterInputSet()

    def _make_result_set(self, result, path):
        return CreateNewsletterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateNewsletterChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateNewsletter
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateNewsletterInputSet(InputSet):
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
        Set the value of the HTML input for this choreography. ((required, string) The html portion of the newsletter.)
        """
        def set_HTML(self, value):
            InputSet._set_input(self, 'HTML', value)

        """
        Set the value of the Identity input for this choreography. ((required, string) The Identiy that will be used for the newsletter to be created.  This must be an existing Identity.)
        """
        def set_Identity(self, value):
            InputSet._set_input(self, 'Identity', value)

        """
        Set the value of the Name input for this choreography. ((required, string) The name of the new newsletter.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Subject input for this choreography. ((required, string) The subject for the new newsletter.)
        """
        def set_Subject(self, value):
            InputSet._set_input(self, 'Subject', value)

        """
        Set the value of the Text input for this choreography. ((required, string) The text portion of the newsletter.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the CreateNewsletter choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateNewsletterResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateNewsletterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateNewsletterResultSet(response, path)
