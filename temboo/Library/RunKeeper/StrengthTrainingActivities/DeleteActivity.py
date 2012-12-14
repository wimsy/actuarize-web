# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteActivity
# Removes an individual strength training activity from a user’s feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteActivity(Choreography):

    """
    Create a new instance of the DeleteActivity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/StrengthTrainingActivities/DeleteActivity')


    def new_input_set(self):
        return DeleteActivityInputSet()

    def _make_result_set(self, result, path):
        return DeleteActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteActivityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteActivity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteActivityInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ActivityID input for this choreography. ((required, integer) This can be the individual id of the activity, or you can pass the full uri for the activity as returned from RetrieveActivities response (i.e. /strengthTrainingActivities/125927913).)
        """
        def set_ActivityID(self, value):
            InputSet._set_input(self, 'ActivityID', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteActivity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteActivityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) Contains the string "true" when an activity is deleted successfully.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteActivityResultSet(response, path)
