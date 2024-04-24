clear all
close all 
clc
syms x
x= [0:0.01:2];
f= (x-1)./(x.^32-1);
figure;
hold on
plot(x,subs(f))
axis([0 2 -0.2 1.2])
xlabel('x vals')
ylabel('f(x)')
title('f(x)= (x-1)/(x^32-1)');
xline(1,'--','x=1')
yline(1/32,'--','f(1)=1/32','linewidth', 0.5);
grid on



