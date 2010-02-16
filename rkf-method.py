
def fun(t,w):
  return w - pow(t,2) +1

def rkf(a, b, alpha, tol, hmax, hmin):
  print "a=%f, b=%f, alpha=%f, tol=%f, hmax=%f, hmin=%f" % (a,b,alpha,tol,hmax,hmin)

  # Step 1
  t = a
  w = alpha
  h = hmax
  flag = True
  print "t=%f, w=%f" % (t,w)

  # Step 2
  while flag:
    
    # Step 3
    K1 = h * fun(t,w)
    K2 = h * fun(t + (1.0/4) * h, w + (1.0/4) * K1)
    K3 = h * fun(t + (3.0/8) * h, w + (3.0/32) * K1 + (9.0/32) * K2)
    K4 = h * fun(t + (12.0/13) * h, w + (1932.0/2197) * K1 - (7200.0/2197) * K2 + (7296.0/2197) * K3)
    K5 = h * fun(t + h, w + (439.0/216) * K1 - 8.0 * K2 + (3680.0/513) * K3 - (845.0/4104) * K4)
    K6 = h * fun(t + 0.5 * h, w - (8.0/27) * K1 + 2.0 * K2 - (3544.0/2565) * K3 + (1859.0/4104) * K4 - (11.0/40) * K5)
    
    #Step 4
    R = abs((1.0/360)*K1 - (128.0/4275)*K3 - (2197.0/75240)*K4 + (1.0/50)*K5 + (2.0/55)*K6)/h

    
    #Step 5
    if R <= tol:
      #Step 6
      t = t + h
      w = w + (25.0/216) * K1 + (1408.0/2565) * K3 + (2197.0/4104) * K4 - (1.0/5) * K5
      #Step 7   
      print "t=%f, w=%f, h=%f" % (t,w,h)
    
    #Step 8
    delta= 0.84 * pow((tol/R),(1.0/4))
    
    #Step 9
    if delta <= 0.1:
      h = 0.1 * h
    elif delta >= 4.0:
      h = 4.0 * h
    else:
      h = delta * h
      
    #Step 10
    if h > hmax:
      h = hmax
      
    #Step 11
    if t >= b:
      flag = False
    elif t + h > b:
      h = b - t
    elif h < hmin:
      flag = False
      print "minimum h exceeded"
      
      
	
rkf(0.0, 2.0, 0.5, pow(10,-5), 0.25, 0.01)
