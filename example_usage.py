from client import UnifiedGlobalPaymentAcquiringRiskOrchestratorClient

def main():
    client = UnifiedGlobalPaymentAcquiringRiskOrchestratorClient()
    res = client.process_unified_payment(320.0, 'IDEAL')
    print('PSP Ref: ' + res['psp_reference'] + ' -> Status: ' + res['auth_result'])
    print('Direct Acquiring: ' + str(res['direct_acquiring_bin_routing_used']) + ' | Fee: EUR ' + str(res['interchange_plus_plus_fee_eur']))
    print('Smart Retries Boost: +' + str(res['revenue_accelerate_smart_retries_boost_pct']) + '% | Risk Rule: ' + res['custom_risk_scoring_rule'])

if __name__ == '__main__':
    main()
