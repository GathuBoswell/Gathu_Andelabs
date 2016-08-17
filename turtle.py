import turtle as t

def koch (k, order, size):
    if order == 0:
        k.forward(size)
    else:
        for angle in  [60, -120, 60, 0]:
            koch(k, order-1, size/3)
            k.left(angle)
            
            
koch(t, 0, 100)
koch(t, 1, 100)
koch(t, 2, 100)
koch(t, 3, 100)

        