
def battery_is_ok(temperature, soc, charge_rate):
  return(check_battery_temp_range(temperature) and check_battery_soc_range(soc) and check_battery_charge_rate(charge_rate))

def check_battery_soc_status(soc):
  if(soc in range(0,20) or soc >80):
    print("Abnormal SoC detected")
    return(False)

def check_battery_temp_range(temperature):
  if temperature in range(0,46):
    return True
  else:
    return False

def check_battery_soc_range(soc):
  if soc in range(20,81):
    return(True)
  else: 
    return(False)

def check_battery_charge_rate(charge_rate):
  if charge_rate <= 0.8 and charge_rate>0:
        return True
  else:
    return False

def battery_management_system(temperature, soc, charge_rate):
  if(battery_is_ok(temperature, soc, charge_rate)):
    return(True)
  else:
    check_battery_soc_status(soc)
    return("Breach")


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  #BoundaryConditionTesting
  assert(battery_is_ok(0, 70, 0.7) is True)
  assert(battery_is_ok(46, 70, 0.7)is False)
  assert(battery_is_ok(-1, 70, 0.7) is False)
  assert(battery_is_ok(25, 20, 0.7) is True)
  assert(battery_is_ok(25, -1, 0.7) is False)
  assert(battery_is_ok(25, 81, 0.7) is False)
  assert(battery_is_ok(25, 70, -1) is False)
  assert(battery_is_ok(25, -1, 0.81) is False)
  assert(battery_is_ok(25, 70, 0.0) is False)
  assert(battery_management_system(25,70,0) == "Breach")
