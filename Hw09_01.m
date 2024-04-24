figure(1)
[x,y]=meshgrid(linspace(-10,10,200));
a=1.5;
 z = sin( atan2(x, y) + x + y )/a + exp(-x^2 - y^2)

surf(x,y,z)
shading interp
box on;
xlabel('x');
ylabel('y');
zlabel('z');
axis on vis3d