# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveActivites
# Returns a feed of a user's fitness activities.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveActivites(Choreography):

    """
    Create a new instance of the RetrieveActivites Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/FitnessActivities/RetrieveActivites')


    def new_input_set(self):
        return RetrieveActivitesInputSet()

    def _make_result_set(self, result, path):
        return RetrieveActivitesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveActivitesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveActivites
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveActivitesInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the PageSize input for this choreography. ((optional, integer) The number entries to return per page. Defaults to 25.)
        """
        def set_PageSize(self, value):
            InputSet._set_input(self, 'PageSize', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page of entries to return. This parameter is used in combination with the PageSize input to page through results. Defaults to 0 (the first page).)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveActivites choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveActivitesResultSet(ResultSet):
        """
        Retrieve the value for the "Next" output from this choreography execution. ((integer) The next page of entries that is available. This value can be passed into the Page input while paging through entries.)
        """
        def get_Next(self):
            return self._output.get('Next', None)
        """
        Retrieve the value for the "Previous" output from this choreography execution. ((integer) The previous page of entries that is available. This value can be passed into the Page input while paging through entries.)
        """
        def get_Previous(self):
            return self._output.get('Previous', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from RunKeeper.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveActivitesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveActivitesResultSet(response, path)
