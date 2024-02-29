def antsfunction(ants):

  a_count = 0
  n_count = 0
  t_count = 0
  ant_count = 0

  for i in range(len(ants)):
                                        
    if ants[i] == 'a' and (i >= len(ants)-2 or ants[i+1:i+3] != 'nt'):
      a_count += 1

    elif ants[i] == 'n' and (i >= len(ants)-2 or ants[i+1:i+3] != 'ta'):
      n_count += 1

    elif ants[i] == 't' and (i >= len(ants)-1 or ants[i+1] != 'a'):  
      t_count += 1

    elif i < len(ants)-2 and ants[i:i+3] == 'ant':
      ant_count += 1

  count = max(a_count, n_count, t_count) - ant_count
  
  return count

antsProblem = "...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t"
answer = antsfunction(antsProblem)

print("the number of dead ants is:" , answer)