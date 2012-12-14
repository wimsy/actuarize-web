# -*- coding: utf-8 -*-

###############################################################################
#
# GetLowestOfferListingsForSKU
# Returns the lowest price offer listings for specific products by item condition. This method uses a MarketplaceId and SellerSKU values to uniquely identify products.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLowestOfferListingsForSKU(Choreography):

    """
    Create a new instance of the GetLowestOfferListingsForSKU Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Products/GetLowestOfferListingsForSKU')


    def new_input_set(self):
        return GetLowestOfferListingsForSKUInputSet()

    def _make_result_set(self, result, path):
        return GetLowestOfferListingsForSKUResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLowestOfferListingsForSKUChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLowestOfferListingsForSKU
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLowestOfferListingsForSKUInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSMarketplaceId input for this choreography. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        def set_AWSMarketplaceId(self, value):
            InputSet._set_input(self, 'AWSMarketplaceId', value)

        """
        Set the value of the AWSMerchantId input for this choreography. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        def set_AWSMerchantId(self, value):
            InputSet._set_input(self, 'AWSMerchantId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the Endpoint input for this choreography. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the ExcludeMe input for this choreography. ((optional, boolean) Excludes your own offer listings from the offer listings that are returned. Set to "true" to exclude your own offer listings from the results. Defaults to "false".)
        """
        def set_ExcludeMe(self, value):
            InputSet._set_input(self, 'ExcludeMe', value)

        """
        Set the value of the ItemCondition input for this choreography. ((optional, string) Filters the offer listings to be considered based on item condition. Valid values: New, Used, Collectible, Refurbished, Club.)
        """
        def set_ItemCondition(self, value):
            InputSet._set_input(self, 'ItemCondition', value)

        """
        Set the value of the SellerSKU input for this choreography. ((required, string) A comma-separated list of up to 20 SellerSKU values used to identify products in the given marketplace.)
        """
        def set_SellerSKU(self, value):
            InputSet._set_input(self, 'SellerSKU', value)


"""
A ResultSet with methods tailored to the values returned by the GetLowestOfferListingsForSKU choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLowestOfferListingsForSKUResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLowestOfferListingsForSKUChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLowestOfferListingsForSKUResultSet(response, path)
