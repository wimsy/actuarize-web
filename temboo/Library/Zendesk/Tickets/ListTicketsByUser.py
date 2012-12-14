# -*- coding: utf-8 -*-

###############################################################################
#
# ListTicketsByUser
# 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListTicketsByUser(Choreography):

    """
    Create a new instance of the ListTicketsByUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Tickets/ListTicketsByUser')


    def new_input_set(self):
        return ListTicketsByUserInputSet()

    def _make_result_set(self, result, path):
        return ListTicketsByUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListTicketsByUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListTicketsByUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListTicketsByUserInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email to authenticate the Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Password input for this choreography. ((required, password) The password matching the email to authenticate the Zendesk account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Server input for this choreography. ((required, string) The server URL associated with your Zendesk account. In many cases this looks like: temboo.zendesk.com but may also be customized: support.temboo.com)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the UserID input for this choreography. ((required, integer) The ID number of the user.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)

        """
        Set the value of the UserType input for this choreography. ((optional, string) Specify "requested" to find tickets that the given user requested and "ccd" to find tickets on which a given user was CC'd. Defaults to searching for tickets that the user requested.)
        """
        def set_UserType(self, value):
            InputSet._set_input(self, 'UserType', value)


"""
A ResultSet with methods tailored to the values returned by the ListTicketsByUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListTicketsByUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListTicketsByUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListTicketsByUserResultSet(response, path)
