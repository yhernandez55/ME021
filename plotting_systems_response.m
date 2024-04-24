clc;
clear all;
radius = 2;
x = 1; y = 1.5;

% convert the degree to radians
d1=deg2rad(135);
d2=deg2rad(270);

% subplot 1
theta = d1:pi/50:d2;
xp = radius * cos(theta) + x;
yp = radius * sin(theta) + y;
%subplot for first plot
subplot(2, 2, 1)
plot(xp, yp, 'r');
hold on
plot(1, 1.5, '+b')

%limits for x and y
ylim([-1 4]);
xlim([-3 3]);
grid on
%for title
title('Arc')
hold off

% subplot 2
% range
x=0:1:10;
% eq for subplot 2
y= 1-exp(-x);
subplot(2,2,2);

% limits
ylim([0,1]);
xlim([0,1]);
plot(x, y, '--r');
hold on
title('Approaching 1')
xlabel('time(sec)')
ylabel('response(m)')
hold off
grid on


% subplot 3
%given t range
t = 0:pi/50:2*pi;
%assign pos
pos = cos(2*t);
%assign vel value
vel = -2*sin(2*t);
%subplot
subplot(2, 2, [3,4])
%plot the third subplot with line width 2
plot(t, pos, '--b', 'LineWidth', 2)
hold on
plot(t, vel, '--m', 'LineWidth', 2)
%legend fro third subplot
legend('position (m)', 'velocity (m/s)','Location', 'northeast','Orientation','vertical')
title('System Response')
xlabel('time(sec)')
ylabel('response (m or m/s)')
grid on
hold off
