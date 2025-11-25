from dataclasses import asdict
from typing import Dict, Any
from .config import EscrowIntent

class DecisionEngine:
    def decide(self, intent: EscrowIntent, market_ctx: Dict[str, Any]):
        plan = {
            "action": intent.action,
            "protocol": intent.protocol,
            "asset": intent.asset,
            "amount": intent.amount,
            "constraints": {
                "risk_level": intent.risk_level,
                "max_slippage_bps": intent.max_slippage_bps,
                "deadline_seconds": intent.deadline_seconds
            },
            "explain": intent.rationale or "Escrow plan created with bounded constraints"
        }

        if intent.risk_level == "low":
            plan["constraints"]["max_slippage_bps"] = min(intent.max_slippage_bps, 30)

        if market_ctx.get("volatility_24h", 0) > 0.08:
            plan["constraints"]["max_slippage_bps"] = min(plan["constraints"]["max_slippage_bps"], 25)
            plan["explain"] = plan["explain"] + ", volatility detected"

        return plan, asdict(intent)