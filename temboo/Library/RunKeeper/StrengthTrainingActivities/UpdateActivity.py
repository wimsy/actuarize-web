# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateActivity
# Updates a past strength training activity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateActivity(Choreography):

    """
    Create a new instance of the UpdateActivity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/StrengthTrainingActivities/UpdateActivity')


    def new_input_set(self):
        return UpdateActivityInputSet()

    def _make_result_set(self, result, path):
        return UpdateActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateActivityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateActivity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateActivityInputSet(InputSet):
        """
        Set the value of the Activity input for this choreography. ((required, json) A JSON string containing the key/value pairs for the activity to update. See documentation for formatting examples.)
        """
        def set_Activity(self, value):
            InputSet._set_input(self, 'Activity', value)

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
A ResultSet with methods tailored to the values returned by the UpdateActivity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateActivityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from RunKeeper.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateActivityResultSet(response, path)
