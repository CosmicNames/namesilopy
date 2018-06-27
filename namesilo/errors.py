class NameSiloError(Exception):
    """Base class for NameSilo errors."""
    pass


class HTTPSNotUsed(NameSiloError):
    """Raised if request is made without HTTPS."""
    pass


class NoVersionSpecified(NameSiloError):
    """Raised if no version is specified in the request."""
    pass


class InvalidAPIVersion(NameSiloError):
    """Raised if the ApI version specified is invalid."""
    pass


class NoTypeSpecified(NameSiloError):
    """Raised if no type is specified in request."""
    pass


class InvalidAPIType(NameSiloError):
    """Raised if API type is invalid."""
    pass


class NoOperationSpecified(NameSiloError):
    """Raised if no operation is specified in request."""
    pass


class MissingAPIParameters(NameSiloError):
    """Raised if there are missing parameters for the specified operation."""
    pass


class InvalidAPIOperation(NameSiloError):
    """Raised if the API operaiton is invalid."""
    pass


class MissingOperationParameters(NameSiloError):
    """Raised if parameters are missing from the API operation."""
    pass


class NoAPIKeySpecified(NameSiloError):
    """Raised if no API key is specified for request."""
    pass


class InvalidAPIKey(NameSiloError):
    """Raised if the API key is invalid."""
    pass


class InvalidUser(NameSiloError):
    """Raised if user associatedwith API key is invalid."""
    pass


class APINotAvailableToSubAccounts(NameSiloError):
    pass


class InvalidIPAddress(NameSiloError):
    pass


class InvalidDomainSyntax(NameSiloError):
    pass


class CentralRegistryNotResponding(NameSiloError):
    pass


class InvalidSandboxAccount(NameSiloError):
    pass


class CreditCardProfileDoesNotExist(NameSiloError):
    pass


class UnverifiedCreditCardProfile(NameSiloError):
    pass


class InsufficientAccountFunds(NameSiloError):
    pass


class ApIKeyNotPassedasGet(NameSiloError):
    pass


class DomainNotActive(NameSiloError):
    pass


class InteralSystemError(NameSiloError):
    pass


class DomainAlreadyAutoRenew(NameSiloError):
    pass


class DomainAlreadyNotAutoReview(NameSiloError):
    pass


class DomainAlreadyLocked(NameSiloError):
    pass


class DomainAlreadyUnlocked(NameSiloError):
    pass


class NameserverUpdateError(NameSiloError):
    pass


class DomainAlreadyPrivate(NameSiloError):
    pass


class DomainAlreadyNotPrivate(NameSiloError):
    pass


class ProcessingError(NameSiloError):
    pass


class DomainAlreadyActive(NameSiloError):
    pass


class InvalidNumberOfYears(NameSiloError):
    pass


class DomainRenewalError(NameSiloError):
    pass


class DomainTransferError(NameSiloError):
    pass


class DomainTransferDoesNotExist(NameSiloError):
    pass


class InvalidDomainName(NameSiloError):
    pass


class DNSModificationError(NameSiloError):
    pass


NAMESILO_ERRORS = {
    '101': HTTPSNotUsed,
    '102': NoVersionSpecified,
    '103': InvalidAPIVersion,
    '104': NoTypeSpecified,
    '105': InvalidAPIType,
    '106': NoOperationSpecified,
    '107': InvalidAPIOperation,
    '108': MissingOperationParameters,
    '109': NoAPIKeySpecified,
    '110': InvalidAPIKey,
    '111': InvalidUser,
    '112': APINotAvailableToSubAccounts,
    '113': InvalidIPAddress,
    '114': InvalidDomainSyntax,
    '115': CentralRegistryNotResponding,
    '116': InvalidSandboxAccount,
    '117': CreditCardProfileDoesNotExist,
    '118': UnverifiedCreditCardProfile,
    '119': InsufficientAccountFunds,
    '120': ApIKeyNotPassedasGet,
    '200': DomainNotActive,
    '201': InteralSystemError,
    '210': NameSiloError,
    '250': DomainAlreadyAutoRenew,
    '251': DomainAlreadyNotAutoReview,
    '252': DomainAlreadyLocked,
    '253': DomainAlreadyUnlocked,
    '254': NameserverUpdateError,
    '255': DomainAlreadyPrivate,
    '256': DomainAlreadyNotPrivate,
    '261': ProcessingError,
    '262': DomainAlreadyActive,
    '263': InvalidNumberOfYears,
    '264': DomainRenewalError,
    '265': DomainTransferError,
    '266': DomainTransferDoesNotExist,
    '267': InvalidDomainName,
    '280': DNSModificationError,
}
