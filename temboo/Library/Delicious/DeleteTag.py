# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteTag
# Deletes a specified tag.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteTag(Choreography):

    """
    Create a new instance of the DeleteTag Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/DeleteTag')


    def new_input_set(self):
        return DeleteTagInputSet()

    def _make_result_set(self, result, path):
        return DeleteTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteTagChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteTag
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteTagInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Tag input for this choreography. ((required, string) The tag to delete.)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)

        """
        Set the value of the Username input for this choreography. ((required, string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteTag choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteTagResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteTagResultSet(response, path)