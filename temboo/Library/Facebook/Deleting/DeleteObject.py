# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteObject
# Deletes objects in the graph with a given id or path.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteObject(Choreography):

    """
    Create a new instance of the DeleteObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Deleting/DeleteObject')


    def new_input_set(self):
        return DeleteObjectInputSet()

    def _make_result_set(self, result, path):
        return DeleteObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteObjectInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ObjectID input for this choreography. ((required, string) The id or path to an object to delete.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteObjectResultSet(response, path)
