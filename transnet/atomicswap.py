from transnet.exceptions import ContractDoesNotExistsException
from transnet.instance import shared_transnet_instance


class AtomicSwap(dict):
    def __init__(
            self,
            data,
            transnet_instance=None
    ):
        self.transnet = transnet_instance or shared_transnet_instance()
        super(AtomicSwap, self).__init__(data)
        self.refresh()

    def refresh(self):
        """ Refresh the data from the API server
        """
        swap_data = self.transnet.rpc.get_atomicswap_contract(self['owner'], self['participant'], self['secret_hash'])
        if not swap_data:
            raise ContractDoesNotExistsException(self['owner'], self['participant'], self['secret_hash'])
        super(AtomicSwap, self).__init__(swap_data, transnet_instance=self.transnet)
