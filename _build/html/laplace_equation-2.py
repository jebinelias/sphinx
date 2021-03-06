def laplace_equation_numerical_2(error_target, niter, nx, ny, xmax, ymax):

   """
   Returns the velocity field and distance for 2D linear convection
   """
   # Increments:
   dx = xmax/(nx-1)
   dy = ymax/(ny-1)

   # Initialise data structures:
   import numpy as np
   p = np.zeros(((nx,ny,niter)))
   x = np.zeros(nx)
   y = np.zeros(ny)
   jpos = np.zeros(ny)
   jneg = np.zeros(ny)

   # X Loop
   for i in range(0,nx):
      x[i] = i*dx

   # Y Loop
   for j in range(0,ny):
      y[j] = j*dy

   # Initial conditions
   p[:,:,0] = 0

   # Dirichlet Boundary Conditions:

   # p boundary, left:
   p[0,:,:] = 0

   # p boundary, right:
   for j in range(0,ny):
      p[nx-1,j,:] = y[j]

   # von Neumann Boundary Conditions:

   # Values for correction at boundaries:
   for j in range(0,ny-1):
      jpos[j] = j + 1
      jneg[j] = j - 1

   # Set Reflection:
   jpos[ny-1] = ny-2
   jneg[0] = 1

   while True:
      for n in range(0,niter-1):
         for i in range(1,nx-1):
            for j in range(0,ny):
               p[i,j,n+1] = (( dy**2 * ( p[i+1,j,n]+p[i-1,j,n] )
                  + dx**2 * ( p[i,jpos[j],n]+p[i,jneg[j],n] ) )
                  / (2*(dx**2 + dy**2)))
               error = np.sum(np.abs(p[i,j,n+1])-np.abs(p[i,j,n]) )
         print "n = " + str(n) + " completed"
         if(error < error_target):
            break
      break

   return p, x, y

def plot_3D_2(p,x,y,time,title,label):
   """
   Plots the 2D velocity field
   """

   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   fig=plt.figure(figsize=(11,7),dpi=100)
   ax=fig.gca(projection='3d')
   ax.set_xlabel('x (m)')
   ax.set_ylabel('y (m)')
   ax.set_zlabel(label)
   ax.set_xlim(0,2)
   ax.set_ylim(0,1)
   ax.view_init(30,225)
   Y,X=np.meshgrid(y,x) #note meshgrid uses y,x not x,y!!!
   surf=ax.plot_surface(X,Y,p[:,:,time], rstride=1, cstride=1)
   plt.title(title)
   plt.show()

def plot_2D_2(p,x,nt,title):
   """
   Plots the 1D velocity field
   """

   import matplotlib.pyplot as plt
   import matplotlib.cm as cm
   plt.figure()
   ax=plt.subplot(111)
   colour=iter(cm.rainbow(np.linspace(0,2,nt)))
   for n in range(0,nt,2):
      c=next(colour)
      ax.plot(x,p[:,-1,n],linestyle='-',c=c,label='n='+str(n)+' numerical')
   box=ax.get_position()
   ax.set_position([box.x0, box.y0, box.width*0.7,box.height])
   ax.legend( bbox_to_anchor=(1.02,1), loc=2)
   plt.xlabel('x (m)')
   plt.ylabel('p (Pa)')
   plt.ylim([0,1.0])
   plt.xlim([0,2.0])
   plt.title(title)
   plt.show()

p2,x2,y2 = laplace_equation_numerical_2(1e-2, 100, 51, 51, 2.0, 1.0)

plot_3D_2(p2,x2,y2,16,'Figure 4: Final Conditions (n=16) nt=100, nx=51, ny=51','p (Pa)')

plot_2D_2(p2,x2,17,'Figure 5: Iterations')