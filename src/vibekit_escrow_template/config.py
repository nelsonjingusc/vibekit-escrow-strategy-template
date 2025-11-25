from dataclasses import dataclass
from typing import Literal, Optional

RiskLevel = Literal["low", "medium", "high"]

@dataclass
class EscrowIntent:
    action: Literal["deposit", "hold", "release", "cancel"]
    protocol: str
    asset: str
    amount: float
    risk_level: RiskLevel = "medium"
    max_slippage_bps: int = 50
    deadline_seconds: int = 300
    rationale: Optional[str] = None