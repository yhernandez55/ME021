clear all
close all 
clc
syms x
n=input('Enter an integer n: ');
y=1;
for i=0:1:n
k=2^i;
y=y*(x^k+1);
end
y1=simplify((x-1)*y);
fprintf('Our product is %s ',y1)