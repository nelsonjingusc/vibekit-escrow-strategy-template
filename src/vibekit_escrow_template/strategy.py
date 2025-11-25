from typing import Dict, Any
from .config import EscrowIntent
from .decision import DecisionEngine
from .tools import VibekitToolAdapter

class EscrowStrategyTemplate:
    def __init__(self):
        self.engine = DecisionEngine()
        self.adapter = VibekitToolAdapter()

    def run(self, intent: EscrowIntent, market_ctx: Dict[str, Any]):
        plan, intent_snapshot = self.engine.decide(intent, market_ctx)
        call = self.adapter.to_vibekit_call(plan)
        return {
            "plan": plan,
            "vibekit_call": call,
            "intent_snapshot": intent_snapshot
        }