class ManagementAgentError(Exception):
    """Base exception for the management agent."""
    pass


class TranslationError(ManagementAgentError):
    """Raised when translation fails."""
    pass


class AnalysisError(ManagementAgentError):
    """Raised when management analysis fails."""
    pass