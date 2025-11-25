from vibekit_escrow_template.strategy import EscrowStrategyTemplate
from vibekit_escrow_template.config import EscrowIntent

def main():
    strat = EscrowStrategyTemplate()

    intent = EscrowIntent(
        action = "deposit",
        protocol = "aave",
        asset = "USDC",
        amount = 500,
        risk_level = "low",
        rationale = "Temporary escrow deposit"
    )

    market = {"volatility_24h": 0.04}

    result = strat.run(intent, market)
    print(result)

if __name__ == "__main__":
    main()