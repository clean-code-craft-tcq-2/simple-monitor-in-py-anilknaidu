signal_soc_status = {"LOW_SOC_BREACH":(0,21),"LOW_SOC_WARNING":(21,25),"NORMAL":(25,76),"HIGH_SOC_WARNING":(76,81),"HIGH_SOC_BREACH":(81,100)}

def battery_is_ok(temperature, soc, charge_rate):
  return(check_battery_temp_range(temperature) and check_battery_soc_range(soc) and check_battery_charge_rate(charge_rate))

def check_battery_soc_status(soc):
  if(soc in range(0,20) or soc >80):
    print("Abnormal SoC detected")
    return(False)

def check_battery_temp_range(temperature):
  temperature = convert_to_celcius(temperature)
  if temperature in range(0,46):
    battery_temperature_warning(temperature)
    return True
  else:
    return False

def check_battery_soc_range(soc):
  report_signal_soc_state(soc)
  if soc in range(20,81):
    battery_soc_warning(soc)
    return(True)
  else: 
    return(False)

def check_battery_charge_rate(charge_rate):
  if charge_rate <= 0.8 and charge_rate>0:
    battery_charge_warning(charge_rate)
    return True
  else:
    return False

def battery_management_system(temperature, soc, charge_rate):
  if(battery_is_ok(temperature, soc, charge_rate)):
    return(True)
  else:
    check_battery_soc_status(soc)
    return("Breach")

def battery_soc_warning(soc):
  if(check_limits_for_warning(soc,76,80)):
    print("Warning: Approaching charge-peak")
  elif(check_limits_for_warning(soc,20,21)):
    print("Warning: Approaching discharge")

def battery_temperature_warning(temperature):
  if(check_limits_for_warning(temperature,43,47)):
    print("Warning: Approaching temperature-peak")
  elif(check_limits_for_warning(temperature,0,3)):
    print("Warning: Approaching low temperature")

def battery_charge_warning(charge):
  if(check_limits_for_warning(charge,0.76,0.80)):
    print("Warning: Approaching High Charging peak")
  elif(check_limits_for_warning(charge,0,0.04)):
    print("Warning: Approaching Low charging")


def report_signal_soc_state(soc):
  for soc_state in signal_soc_status:
    if(soc in range(signal_soc_status[soc_state][0],signal_soc_status[soc_state][1])):
      print("SoC Level: ",soc,": ",soc_state)

def convert_to_celcius(temperature):
  if('f' in temperature.lower() ):
    return((int(temperature.lower().split('f')[0])-32.0)*(5.0/9.0))
  elif('k' in temperature.lower()):
    return(int(temperature.lower().split('k')[0])-273.0)
  elif('c' in temperature.lower()):
    return(int(temperature.lower().split('c')[0]))

def check_limits_for_warning(valueToBeChecked,lower_limit,upper_limit):
  return(int(valueToBeChecked*100) in range(int(lower_limit*100),int(upper_limit*100+1)))

if __name__ == '__main__':
  assert(battery_is_ok('25c', 70, 0.7) is True)
  assert(battery_is_ok('50c', 85, 0) is False)
  #BoundaryConditionTesting
  assert(battery_is_ok('0c', 70, 0.7) is True)
  assert(battery_is_ok('46c', 19, 0.7)is False)
  assert(battery_is_ok('-1c', 20, 0.7) is False)
  assert(battery_is_ok('25c', 79, 0.7) is True)
  assert(battery_is_ok('274k', 80, 0.7) is True)
  assert(battery_is_ok('91F', 81, 0.7) is False)
  assert(battery_is_ok('290K', 21, -1) is False)
  assert(battery_is_ok('25c', -1, 0.81) is False)
  assert(battery_is_ok('14c', 70, 0.0) is False)
  assert(battery_management_system('25',70,0) == "Breach")
