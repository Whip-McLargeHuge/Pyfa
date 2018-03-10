# ammoSpeedMultiplier
#
# Used by:
# Charges from group: Festival Charges (23 of 23)
# Charges from group: Interdiction Probe (2 of 2)
type = "passive"


def handler(fit, module, context):
    module.multiplyItemAttr("speed", module.getModifiedChargeAttr("speedMultiplier") or 1)
