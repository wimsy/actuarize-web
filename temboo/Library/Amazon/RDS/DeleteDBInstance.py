# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteDBInstance
# Deletes a specified database instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteDBInstance(Choreography):

    """
    Create a new instance of the DeleteDBInstance Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/DeleteDBInstance')


    def new_input_set(self):
        return DeleteDBInstanceInputSet()

    def _make_result_set(self, result, path):
        return DeleteDBInstanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDBInstanceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteDBInstance
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteDBInstanceInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the DBInstanceIdentifier input for this choreography. ((required, string) The ID for the DB instance to delete.)
        """
        def set_DBInstanceIdentifier(self, value):
            InputSet._set_input(self, 'DBInstanceIdentifier', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteDBInstance choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteDBInstanceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteDBInstanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDBInstanceResultSet(response, path)
