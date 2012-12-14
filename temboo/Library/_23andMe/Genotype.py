# -*- coding: utf-8 -*-

###############################################################################
#
# Genotype
# For each of the user's profiles, retrieves the base-pairs for given locations.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Genotype(Choreography):

    """
    Create a new instance of the Genotype Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/23andMe/Genotype')


    def new_input_set(self):
        return GenotypeInputSet()

    def _make_result_set(self, result, path):
        return GenotypeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GenotypeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Genotype
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GenotypeInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after completing the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Locations input for this choreography. ((required, string) A space delimited list of SNPs (i.e. rs3094315 rs3737728).)
        """
        def set_Locations(self, value):
            InputSet._set_input(self, 'Locations', value)


"""
A ResultSet with methods tailored to the values returned by the Genotype choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GenotypeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from 23AndMe.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GenotypeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GenotypeResultSet(response, path)
