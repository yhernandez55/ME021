% prob 6
clc;
x=-15:15;
slope=1/5;
intercept=5;
y=zeros(1,length(x));
for m=1:length(x)
    y1(m)=straightline(x(m),1,6);
    y2(m)=straightline(x(m),1,9);
end

plot (x,y1,'Linewidth',5)
hold on
plot(x,y2,'Linewidth',5)
hold off
legend('intercept 6', 'intercept 9')

function y=straightline(slope,x,intercept)
    y=slope*x+intercept;
end