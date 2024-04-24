clear all
close all 
clc

syms y(t) w A B
y(t) = A*cos(w*t) + B*sin(w*t); % equation given
y = diff(y, t, 2) + y % second derivative
fsimplified = simplify(y)
collect1 = collect(fsimplified, [y t])
collect2 = collect(collect1, [y t])
% used pretty instead og latex since its more clear
pretty(collect2)
