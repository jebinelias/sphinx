def non_linear_convection(nt, nx, ny, tmax, xmax, ymax):
   """
   Returns the velocity field and distance for 2D linear convection
   """
   # Increments
   dt = tmax/(nt-1)
   dx = xmax/(nx-1)
   dy = ymax/(ny-1)

   # Initialise data structures
   import numpy as np
   u = np.zeros(((nx,ny,nt)))
   v = np.zeros(((nx,ny,nt)))
   x = np.zeros(nx)
   y = np.zeros(ny)

   # Boundary conditions
   u[0,:,:] = u[nx-1,:,:] = u[:,0,:] = u[:,ny-1,:] = 1
   v[0,:,:] = v[nx-1,:,:] = v[:,0,:] = v[:,ny-1,:] = 1

   # Initial conditions
   u[:,:,:] = v[:,:,:] = 1
   u[(nx-1)/4:(nx-1)/2,(ny-1)/4:(ny-1)/2,0] = 2
   v[(nx-1)/4:(nx-1)/2,(ny-1)/4:(ny-1)/2,0] = 2

   # Loop
   for n in range(0,nt-1):
      for i in range(1,nx-1):
         for j in range(1,ny-1):
            u[i,j,n+1] = (u[i,j,n]-dt*((u[i,j,n]/dx)*(u[i,j,n]-u[i-1,j,n])+
                                       (v[i,j,n]/dy)*(u[i,j,n]-u[i,j-1,n])))
            v[i,j,n+1] = (v[i,j,n]-dt*((u[i,j,n]/dx)*(v[i,j,n]-v[i-1,j,n])+
                                       (v[i,j,n]/dy)*(v[i,j,n]-v[i,j-1,n])))

   # X Loop
   for i in range(0,nx):
      x[i] = i*dx

   # Y Loop
   for j in range(0,ny):
      y[j] = j*dy

   return u, v, x, y

def plot_initial_conditions_u(u,x,y,nt,ny,title):
   """
   Plots the 2D velocity field
   """

   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   fig=plt.figure(figsize=(11,7),dpi=100)
   ax=fig.gca(projection='3d')
   ax.set_xlabel('x (m)')
   ax.set_ylabel('y (m)')
   ax.set_zlabel('u (m/s)')
   X,Y=np.meshgrid(x,y)
   surf=ax.plot_surface(X,Y,u[:,:,0],rstride=2,cstride=2)
   plt.title(title)
   plt.show()

def plot_final_conditions_u(u,x,y,nt,ny,title):
   """
   Plots the 2D velocity field
   """

   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   fig=plt.figure(figsize=(11,7),dpi=100)
   ax=fig.gca(projection='3d')
   ax.set_xlabel('x (m)')
   ax.set_ylabel('y (m)')
   ax.set_zlabel('u (m/s)')
   X,Y=np.meshgrid(x,y)
   surf=ax.plot_surface(X,Y,u[:,:,nt-1],rstride=2,cstride=2)
   plt.title(title)
   plt.show()

def plot_initial_conditions_v(v,x,y,nt,ny,title):
   """
   Plots the 2D velocity field
   """

   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   fig=plt.figure(figsize=(11,7),dpi=100)
   ax=fig.gca(projection='3d')
   ax.set_xlabel('x (m)')
   ax.set_ylabel('y (m)')
   ax.set_zlabel('v (m/s)')
   X,Y=np.meshgrid(x,y)
   surf=ax.plot_surface(X,Y,v[:,:,0],rstride=2,cstride=2)
   plt.title(title)
   plt.show()

def plot_final_conditions_v(v,x,y,nt,ny,title):
   """
   Plots the 2D velocity field
   """

   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   fig=plt.figure(figsize=(11,7),dpi=100)
   ax=fig.gca(projection='3d')
   ax.set_xlabel('x (m)')
   ax.set_ylabel('y (m)')
   ax.set_zlabel('v (m/s)')
   X,Y=np.meshgrid(x,y)
   surf=ax.plot_surface(X,Y,v[:,:,nt-1],rstride=2,cstride=2)
   plt.title(title)
   plt.show()

u,v,x,y = non_linear_convection(101, 81, 81, 0.5, 2.0, 2.0)

plot_initial_conditions_u(u,x,y,51,81,'Figure 1: c=0.5m/s, nt=101, nx=81, ny=81, t=0sec')
plot_final_conditions_u(u,x,y,51,81,'Figure 2: c=0.5m/s, nt=101, nx=81, ny=81, t=0.5sec')
plot_initial_conditions_v(v,x,y,51,81,'Figure 3: c=0.5m/s, nt=101, nx=81, ny=81, t=0sec')
plot_final_conditions_v(v,x,y,51,81,'Figure 4: c=0.5m/s, nt=101, nx=81, ny=81, t=0.5sec')