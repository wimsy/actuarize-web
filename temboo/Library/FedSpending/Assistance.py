# -*- coding: utf-8 -*-

###############################################################################
#
# Assistance
# Allows access to the information in the Federal Assisatance Award Data System (FAADS) database, which reports all financial assistance made by federal agencies.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Assistance(Choreography):

    """
    Create a new instance of the Assistance Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FedSpending/Assistance')


    def new_input_set(self):
        return AssistanceInputSet()

    def _make_result_set(self, result, path):
        return AssistanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AssistanceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Assistance
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AssistanceInputSet(InputSet):
        """
        Set the value of the AgencyCode input for this choreography. ((conditional, string) The 4-character code for a specific governmental agency providing assistance.)
        """
        def set_AgencyCode(self, value):
            InputSet._set_input(self, 'AgencyCode', value)

        """
        Set the value of the AssistanceType input for this choreography. ((conditional, string) The type of assistance provided. Valid values are: d = Direct Payments (specified and unrestricted), g = Grants and Cooperative Agreements, i = Insurance, l = Loans (direct and guaranteed), o = Other.)
        """
        def set_AssistanceType(self, value):
            InputSet._set_input(self, 'AssistanceType', value)

        """
        Set the value of the CFDAProgram input for this choreography. ((conditional, string) An ID for the governmental program.)
        """
        def set_CFDAProgram(self, value):
            InputSet._set_input(self, 'CFDAProgram', value)

        """
        Set the value of the Detail input for this choreography. ((optional, string) Controls the level of detail of the output. Acceptable values: -1 (summary), 0 (low), 1 (medium), 2 (high), and 3 (extensive). Defaults to -1. See docs for more information.)
        """
        def set_Detail(self, value):
            InputSet._set_input(self, 'Detail', value)

        """
        Set the value of the FederalID input for this choreography. ((conditional, string) A Federal ID for the award.)
        """
        def set_FederalID(self, value):
            InputSet._set_input(self, 'FederalID', value)

        """
        Set the value of the FirstYearRange input for this choreography. ((conditional, integer) Specifies the first year in a range of years from 2000-2006; if used, must be used with LastYearRange and without FiscalYear.)
        """
        def set_FirstYearRange(self, value):
            InputSet._set_input(self, 'FirstYearRange', value)

        """
        Set the value of the FiscalYear input for this choreography. ((conditional, integer) Specifies a single year from 2000-2006; defaults to all years.)
        """
        def set_FiscalYear(self, value):
            InputSet._set_input(self, 'FiscalYear', value)

        """
        Set the value of the LastYearRange input for this choreography. ((conditional, integer) Specifies the last year in a range of years from 2000-2006; if used, must be used with FirstYearRange and without FiscalYear.)
        """
        def set_LastYearRange(self, value):
            InputSet._set_input(self, 'LastYearRange', value)

        """
        Set the value of the MajAgency input for this choreography. ((conditional, string) The 2-character code for a major governmental agency providing assistance.)
        """
        def set_MajAgency(self, value):
            InputSet._set_input(self, 'MajAgency', value)

        """
        Set the value of the MaxRecords input for this choreography. ((optional, integer) Allows you to set the maximum number of records retrieved. Defaults to 100.)
        """
        def set_MaxRecords(self, value):
            InputSet._set_input(self, 'MaxRecords', value)

        """
        Set the value of the PrincipalPlaceCC input for this choreography. ((conditional, string) The city or county of the place of performance.)
        """
        def set_PrincipalPlaceCC(self, value):
            InputSet._set_input(self, 'PrincipalPlaceCC', value)

        """
        Set the value of the PrincipalPlaceStateCode input for this choreography. ((conditional, string) The FIPS state code for the state of the place of performance.)
        """
        def set_PrincipalPlaceStateCode(self, value):
            InputSet._set_input(self, 'PrincipalPlaceStateCode', value)

        """
        Set the value of the RecipientCityName input for this choreography. ((conditional, string) The city in the address of a recipient.)
        """
        def set_RecipientCityName(self, value):
            InputSet._set_input(self, 'RecipientCityName', value)

        """
        Set the value of the RecipientCountyName input for this choreography. ((conditional, string) The county in which a recipient is located.)
        """
        def set_RecipientCountyName(self, value):
            InputSet._set_input(self, 'RecipientCountyName', value)

        """
        Set the value of the RecipientDistrict input for this choreography. ((conditional, string) The Congressional District in which the recipient is located, formatted with four characters.)
        """
        def set_RecipientDistrict(self, value):
            InputSet._set_input(self, 'RecipientDistrict', value)

        """
        Set the value of the RecipientName input for this choreography. ((conditional, string) The name of a recipient of assistance.)
        """
        def set_RecipientName(self, value):
            InputSet._set_input(self, 'RecipientName', value)

        """
        Set the value of the RecipientStateCode input for this choreography. ((conditional, string) The FIPS state code for the state in the address of a recipient.)
        """
        def set_RecipientStateCode(self, value):
            InputSet._set_input(self, 'RecipientStateCode', value)

        """
        Set the value of the RecipientType input for this choreography. ((conditional, string) The type of recipient. Valid values are: f = For Profits, g = Government,h = Higher Education, i = Individuals,n = Nonprofits, o = Other.)
        """
        def set_RecipientType(self, value):
            InputSet._set_input(self, 'RecipientType', value)

        """
        Set the value of the RecipientZip input for this choreography. ((conditional, integer) The ZIP code in the address of a recipient.)
        """
        def set_RecipientZip(self, value):
            InputSet._set_input(self, 'RecipientZip', value)

        """
        Set the value of the SortBy input for this choreography. ((optional, string) Determines how records are sorted. Valid values: r (contractor/recipient name), f (dollars of awards),g (major contracting agency), p (CFDA Program), d (date of award). Defaults to f.)
        """
        def set_SortBy(self, value):
            InputSet._set_input(self, 'SortBy', value)

        """
        Set the value of the TextSearch input for this choreography. ((conditional, string) A free text search on a description of the project.)
        """
        def set_TextSearch(self, value):
            InputSet._set_input(self, 'TextSearch', value)


"""
A ResultSet with methods tailored to the values returned by the Assistance choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AssistanceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FedSpending.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AssistanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AssistanceResultSet(response, path)
