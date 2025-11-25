class VibekitToolAdapter:
    def to_vibekit_call(self, plan):
        return {
            "tool_name": f"{plan['protocol']}_{plan['action']}",
            "args": {
                "asset": plan["asset"],
                "amount": plan["amount"],
                "max_slippage_bps": plan["constraints"]["max_slippage_bps"],
                "deadline_seconds": plan["constraints"]["deadline_seconds"]
            }
        }