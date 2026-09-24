# === Stage 57: Add structured result objects for command handlers ===
# Project: PortfolioNotes
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class CommandResult:
    success: bool
    message: str
    data: Optional[Any] = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
        }

    @classmethod
    def ok(cls, message: str = "OK", data: Any = None) -> "CommandResult":
        return cls(success=True, message=message, data=data)

    @classmethod
    def fail(cls, message: str = "Error") -> "CommandResult":
        return cls(success=False, message=message)
