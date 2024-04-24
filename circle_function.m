function h = circle()
hold on
th = 0:pi/50:2*pi;
xunit = 2 * cos(th) + 3;
yunit = 2 * sin(th) + 5; %using equation of circle to generate plot points for circle.
h = plot(xunit, yunit,'linewidth', 2, 'Color', 'blue');
axis([0 10 0 10]);
t = text(3,5,'+');
set(t,'Color','blue');
prompt = text(1,9.5,'Click to provide label location. ');
set(gcf, 'Position', [500, 500, 500, 500]);
[x, y] = ginput(1);
delete(prompt);
text(x,y,'Circle(3,5,2)');
prompt = text(1,9.5,'Click to provide end-points of the leader line. ');
[x, y] = ginput(2);
plot(x,y,'--');
delete(prompt);
xunit = 0.5 * cos(th) + 8;
yunit = 0.5 * sin(th) + 7;
h = plot(xunit, yunit,'linewidth', 2, 'Color', 'red');
axis([0 10 0 10]);
t = text(8,7,'+');
set(t,'Color','red');
prompt = text(1,9.5,'Click to provide label location. ');
[x, y] = ginput(1);
delete(prompt);
text(x,y,'Circle(8,7,0.5)');
prompt = text(1,9.5,'Click to provide end-points of the leader line. ');
[x, y] = ginput(2);
plot(x,y,'--','Color','red');
delete(prompt);
end
