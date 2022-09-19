def sleep_in(weekday, vacation):
  if weekday and vacation:
    return True
  elif weekday and not vacation:
    return False
  elif not weekday and vacation:
    return True
  else:
    return True
