clear all;
plot(0,0)
xlim([-10 10])
ylim([-10 10])
axis square
grid on
hold on 
looper=true;
fprintf('Please click a point for the center of the circle\n ')
[xcenter,ycenter] = ginput(1);
pl1 = plot(xcenter,ycenter,'+k');
while looper==true
fprintf('Please click a point for the radius of the circle\n')
[x2,y2]= ginput(1);
r = distance(xcenter,ycenter,x2,y2);
if (xcenter+r)>10||(xcenter-r)<-10||(ycenter+r)>10||(ycenter-r)<-10
    looper=true;
    pause(.2);
    oops=fprintf('Circle too big please try again in the bounds\n');
    
else
    looper=false;
end
end    
[xf,y]=Circlecreate(xcenter,ycenter,r);
circle=plot(xf,y,'b','Linewidth',2);
fprintf('Please click a point for the direction and velocity\n')
[xdir,ydir]=ginput(1);
pl3=plot([xcenter,xdir],[ycenter,ydir],'-._r');
N=10;
dx=(xdir-xcenter)/N;
dy=(ydir-ycenter)/N;
looper=1;
circlecolor='b';
while looper==1
    pause(.09)
   
    if abs(xcenter+dx)+r>=10
        dx=-dx;
        circlecolor='r';
    end
    if abs(ycenter+dy)+r>=10
        dy=-dy;
        circlecolor='r';
    end
    
    xcenter=xcenter+dx;
    ycenter=ycenter+dy;
    
    [xf,y]=Circlecreate(xcenter,ycenter,r);
    delete(pl1);
    delete(pl3);
    delete(circle);
    circle=plot(xf,y,circlecolor,'Linewidth',2);
    circlecolor='b';
end

% function d = distance(xc,yc,x2,y2)
% d=sqrt(((x2-xc)^2)+((y2-yc)^2));
% end 
function [xvals,yvals]=Circlecreate(x,y,r)
theta =0:1:360;
xvals=x+r*cos(theta);
yvals=y+r*sin(theta);

end 








