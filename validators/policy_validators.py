

class PolicyValidator:

    @staticmethod
    def validate_active_policy(act_policy_num, act_insured_name, act_policy_status, act_policy_type):
        exp_policy_num = "TEST3814TEST"
        # exp_insured_name = "QA Test - Kelley Senger dba Maggio LLC"
        exp_effective_date = "December 14, 2017"
        exp_expiration_date = "January 27, 2018"
        exp_policy_status = "Active"
        exp_policy_type = "New Policy"
        exp_product_name = "Cyber Liability"
        exp_gross_premium = "$450.00"

        assert exp_policy_num == act_policy_num, "ERROR: value was '" + act_policy_num + \
                                                 "' but expected '" + exp_policy_num + "'"

#        assert exp_insured_name == act_insured_name, "ERROR: value was '" + act_insured_name + \
#                                                     "' but expected '" + exp_insured_name + "'"

        assert exp_policy_status == act_policy_status, "ERROR: value was '" + act_policy_status + \
                                                       "' but expected '" + exp_policy_status + "'"

        assert exp_policy_type == act_policy_type, "ERROR: value was '" + act_policy_type + \
                                                   "' but expected '" + exp_policy_type + "'"

