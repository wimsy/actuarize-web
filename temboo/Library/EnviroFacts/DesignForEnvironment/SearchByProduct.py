# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByProduct
# Searches for products in the EPA Design for the Environment database.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByProduct(Choreography):

    """
    Create a new instance of the SearchByProduct Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/DesignForEnvironment/SearchByProduct')


    def new_input_set(self):
        return SearchByProductInputSet()

    def _make_result_set(self, result, path):
        return SearchByProductResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByProductChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByProduct
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByProductInputSet(InputSet):
        """
        Set the value of the CompanyKeyword input for this choreography. ((conditional, string) A keyword in the name of the company to search for. If a specific ProductName or ProductID is specified, this input is ignored.)
        """
        def set_CompanyKeyword(self, value):
            InputSet._set_input(self, 'CompanyKeyword', value)

        """
        Set the value of the Operator input for this choreography. ((optional, string) Default output is "CONTAINING" and does not require an operator, but users can enter "<", " >", "!=", "BEGINNING", "=" for more customized searches.)
        """
        def set_Operator(self, value):
            InputSet._set_input(self, 'Operator', value)

        """
        Set the value of the ProductID input for this choreography. ((conditional, integer) A number representing the unique identifier for a product in the EnviroFacts database.)
        """
        def set_ProductID(self, value):
            InputSet._set_input(self, 'ProductID', value)

        """
        Set the value of the ProductKeyword input for this choreography. ((conditional, string) A keyword in the name of the product to search for. If a specific ProductID is specified, this input is ignored.)
        """
        def set_ProductKeyword(self, value):
            InputSet._set_input(self, 'ProductKeyword', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((conditional, string) Response can be returned in JSON or XML. Defaults to XML.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the RowEnd input for this choreography. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        def set_RowEnd(self, value):
            InputSet._set_input(self, 'RowEnd', value)

        """
        Set the value of the RowStart input for this choreography. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        def set_RowStart(self, value):
            InputSet._set_input(self, 'RowStart', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByProduct choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByProductResultSet(ResultSet):
        """
        Retrieve the value for the "Count" output from this choreography execution. (The total number of records returned for any given search.)
        """
        def get_Count(self):
            return self._output.get('Count', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByProductChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByProductResultSet(response, path)
