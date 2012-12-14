# -*- coding: utf-8 -*-

###############################################################################
#
# GetComments
# Returns comments for a specified journal entry.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetComments(Choreography):

    """
    Create a new instance of the GetComments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/JournalEntries/GetComments')


    def new_input_set(self):
        return GetCommentsInputSet()

    def _make_result_set(self, result, path):
        return GetCommentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCommentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetComments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCommentsInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the JournalID input for this choreography. ((required, integer) The ID number of the journal entry for which you want comments.)
        """
        def set_JournalID(self, value):
            InputSet._set_input(self, 'JournalID', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page position of results to return. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetComments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCommentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCommentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCommentsResultSet(response, path)
