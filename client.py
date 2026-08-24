class UnifiedGlobalPaymentAcquiringRiskOrchestratorClient:
    def process_unified_payment(self, transaction_amount_eur=145.0, payment_method='APPLE_PAY', merchant_account='MERCH_GLOBAL_LUXURY'):
        return {
            'psp_reference': 'ady_psp_991823746',
            'auth_result': 'AUTHORISED',
            'direct_acquiring_bin_routing_used': True,
            'revenue_accelerate_smart_retries_boost_pct': 1.85,
            'custom_risk_scoring_rule': 'REVENUE_PROTECT_PASS',
            'interchange_plus_plus_fee_eur': 0.88,
            'settlement_currency': 'EUR'
        }
